"""Reload orchestration: git sync (polling + webhook), fresh in-memory
self-discovery, atomic module reload with rollback, and the event bridge
from hass.bus into the ported Automation scheduler.

This is the piece that replaces `watchdog` (hapy/application.py's
FileChangeHandler), which is the actual reliability problem this whole
migration exists to fix — see plan doc's "Reload fiable" section. Every
disparo (poll timer, webhook, or the manual `hapy_automation.reload`
service) funnels into `async_reload()`, which is the only place a new
commit ever gets applied.
"""
from __future__ import annotations

import asyncio
import importlib
import logging
import sys
import time
from datetime import datetime, timezone

from homeassistant.core import HomeAssistant, Event, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.dispatcher import async_dispatcher_send, dispatcher_send
from homeassistant.helpers.event import async_track_time_interval

from .const import (
    ALWAYS_INCLUDED_DOMAINS,
    CONF_AUTH_METHOD,
    CONF_BRANCH,
    CONF_DRY_RUN,
    CONF_ENTITY_INCLUDE_PATTERN,
    CONF_PAT,
    CONF_POLL_INTERVAL_MINUTES,
    CONF_REPO_URL,
    CONF_SSH_KEY_PATH,
    GENERATED_SUBDIR,
    REPO_SUBDIR,
    SIGNAL_RELOAD_COMPLETE,
    STATE_EVENT_TYPE,
    STATUS_ERROR,
    STATUS_OK,
    STATUS_UNKNOWN,
    ZHA_EVENT_TYPE,
)
from .git_manager import GitManager, GitOperationError
from .scaffold import write_scaffold
from .runtime import compat, models
from .runtime.automations import AutomationHandler
from .runtime.generators import devices as devices_gen
from .runtime.generators import domains as domains_gen
from .runtime.generators import entities as entities_gen
from .runtime.registry import async_build_register

logger = logging.getLogger(__name__)

_GENERATED_MODULE_NAMES = ('entities', 'devices', 'domains')
_AUTOMATIONS_MODULE_NAME = 'automations'


class ReloadResult:
    def __init__(self, ok: bool, sha: str | None = None, error: str | None = None):
        self.ok = ok
        self.sha = sha
        self.error = error


class HapyCoordinator:
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        self.hass = hass
        self.entry = entry

        self.repo_path = hass.config.path('hapy_automation', entry.entry_id, REPO_SUBDIR)
        self.generated_path = hass.config.path('hapy_automation', entry.entry_id, GENERATED_SUBDIR)

        data = entry.data
        self.git = GitManager(
            repo_path=self.repo_path,
            repo_url=data[CONF_REPO_URL],
            branch=data.get(CONF_BRANCH, 'main'),
            auth_method=data.get(CONF_AUTH_METHOD, 'none'),
            ssh_key_path=data.get(CONF_SSH_KEY_PATH),
            personal_access_token=data.get(CONF_PAT),
        )

        self.current_sha: str | None = entry.data.get('last_good_sha')
        self.last_reload_status = STATUS_UNKNOWN
        self.last_reload_error: str | None = None
        self.last_reload_at: datetime | None = None
        self.last_would_have_fired: tuple[str, datetime] | None = None

        self._lock = asyncio.Lock()
        self._unsub_timer = None
        self._unsub_state = None
        self._unsub_zha = None
        self._paths_ready = False
        self.agent_runner = None  # set by __init__.py if CONF_ENABLE_AGENT

        compat.install()
        models.set_hass(hass)
        models.set_dry_run(bool(data.get(CONF_DRY_RUN, True)))
        AutomationHandler.dry_run = bool(data.get(CONF_DRY_RUN, True))
        AutomationHandler.on_automation_fired = [self._on_automation_fired]

    # -- lifecycle --------------------------------------------------------

    async def async_start(self) -> None:
        await self.async_reload(force=True)
        interval_minutes = self.entry.data.get(CONF_POLL_INTERVAL_MINUTES, 1)
        from datetime import timedelta
        self._unsub_timer = async_track_time_interval(
            self.hass, self._async_poll, timedelta(minutes=interval_minutes)
        )
        self._unsub_state = self.hass.bus.async_listen(STATE_EVENT_TYPE, self._on_state_changed)
        self._unsub_zha = self.hass.bus.async_listen(ZHA_EVENT_TYPE, self._on_zha_event)

    async def async_stop(self) -> None:
        for unsub in (self._unsub_timer, self._unsub_state, self._unsub_zha):
            if unsub:
                unsub()
        self._unsub_timer = self._unsub_state = self._unsub_zha = None

    async def _async_poll(self, _now) -> None:
        logger.debug('[hapy_automation] poll tick at %s', _now)
        await self.async_reload()

    # -- reload -------------------------------------------------------------

    async def async_reload(self, force: bool = False) -> ReloadResult:
        async with self._lock:
            return await self._async_reload_locked(force)

    async def _async_reload_locked(self, force: bool) -> ReloadResult:
        try:
            await self.hass.async_add_executor_job(self.git.ensure_cloned)
            scaffolded = await self.hass.async_add_executor_job(self._maybe_scaffold_repo)
            if scaffolded:
                # A brand-new commit we just pushed ourselves — always do
                # a real reload pass for it, not just a "nothing changed"
                # no-op (there was nothing here to compare against yet).
                force = True
            remote_sha = await self.hass.async_add_executor_job(self.git.fetch_remote_sha)
        except GitOperationError as e:
            self._record_failure(str(e))
            return ReloadResult(False, error=str(e))
        except Exception as e:  # noqa: BLE001 - surfaced to the user via the sensor
            logger.exception('git fetch failed')
            self._record_failure(str(e))
            return ReloadResult(False, error=str(e))

        if not force and remote_sha == self.current_sha:
            return ReloadResult(True, sha=self.current_sha)

        try:
            await self.hass.async_add_executor_job(self.git.checkout_sha, remote_sha)
            register = await async_build_register(
                self.hass,
                self.entry.data.get(CONF_ENTITY_INCLUDE_PATTERN, ''),
                ALWAYS_INCLUDED_DOMAINS,
            )
            await self.hass.async_add_executor_job(self._write_generated_modules, register)
            self._ensure_sys_path()
            await self.hass.async_add_executor_job(self._reload_modules)
        except Exception as e:  # noqa: BLE001
            logger.exception('reload failed at commit %s', remote_sha[:8])
            await self._rollback(e)
            return ReloadResult(False, sha=self.current_sha, error=str(e))

        self.current_sha = remote_sha
        self._record_success(remote_sha)
        self.hass.config_entries.async_update_entry(
            self.entry, data={**self.entry.data, 'last_good_sha': remote_sha}
        )
        async_dispatcher_send(self.hass, SIGNAL_RELOAD_COMPLETE)
        return ReloadResult(True, sha=remote_sha)

    async def _rollback(self, error: Exception) -> None:
        if self.current_sha:
            try:
                await self.hass.async_add_executor_job(self.git.checkout_sha, self.current_sha)
                await self.hass.async_add_executor_job(self._reload_modules)
            except Exception:
                logger.exception(
                    'rollback to previously-good commit %s also failed — '
                    'leaving whatever automations are currently loaded in memory running',
                    self.current_sha[:8] if self.current_sha else '?',
                )
        self._record_failure(str(error))

    def _record_success(self, sha: str) -> None:
        self.last_reload_status = STATUS_OK
        self.last_reload_error = None
        self.last_reload_at = datetime.now(timezone.utc)
        logger.info('[hapy_automation] reload OK, now running commit %s', sha[:8])

    def _record_failure(self, error: str) -> None:
        self.last_reload_status = STATUS_ERROR
        self.last_reload_error = error
        self.last_reload_at = datetime.now(timezone.utc)
        async_dispatcher_send(self.hass, SIGNAL_RELOAD_COMPLETE)
        logger.error('[hapy_automation] reload failed: %s', error)

    # -- repo scaffolding (blocking, executor-only) -------------------------

    def _maybe_scaffold_repo(self) -> bool:
        """If the configured repo/branch has no automations/ package yet
        (a brand-new empty repo, most commonly), write a minimal starter
        layout and push it — so pointing this integration at an empty
        repo just works, instead of requiring the user to hand-create the
        expected structure first. Returns True if a scaffold commit was
        made. A repo that already has an automations/ package (the normal
        case after the first run) is left completely untouched."""
        self.git.ensure_branch_checked_out()
        if self.git.has_automations_package():
            return False
        logger.info(
            '[hapy_automation] %s (rama %s) no tiene automations/ — generando esqueleto inicial',
            self.git.repo_url, self.git.branch,
        )
        write_scaffold(self.git.repo_path)
        sha = self.git.commit_and_push('hapy_automation: scaffold inicial (automations/ vacío)')
        if sha:
            logger.info('[hapy_automation] esqueleto inicial empujado como %s', sha[:8])
        return sha is not None

    # -- codegen / module (re)loading (blocking, executor-only) ------------

    def _write_generated_modules(self, register: dict) -> None:
        import os
        os.makedirs(self.generated_path, exist_ok=True)
        entities_gen.write_entities_module(register, os.path.join(self.generated_path, 'entities.py'))
        devices_gen.write_devices_module(register, os.path.join(self.generated_path, 'devices.py'))
        domains_gen.write_domain_module(register, os.path.join(self.generated_path, 'domains.py'))

    def _ensure_sys_path(self) -> None:
        if self._paths_ready:
            return
        # generated_path must end up ahead of repo_path on sys.path:
        # `import entities`/`devices`/`domains` need to resolve to the
        # freshly-generated modules here, not to any same-named files the
        # user's repo happens to have committed (e.g. home-automations
        # ships its own checked-in entities.py/devices.py/domains.py from
        # the old system, which `import hapy.models` and would shadow
        # ours if it won. Insert repo_path first so generated_path's
        # later insert(0, ...) ends up in front of it.
        for path in (self.repo_path, self.generated_path):
            if path not in sys.path:
                sys.path.insert(0, path)
            else:
                sys.path.remove(path)
                sys.path.insert(0, path)
        self._paths_ready = True

    def _reload_modules(self) -> None:
        """Purge + reimport entities/devices/domains/automations, with a
        full snapshot/rollback of both sys.modules and the in-memory
        registries (AutomationHandler/EntityHandler/DeviceHandler) so a
        broken commit can never leave the process half-updated — either
        the whole reload lands, or nothing about the running automations
        changes at all."""
        purge_names = self._purge_names()
        with models.RUNTIME_LOCK:
            old_modules = {name: sys.modules[name] for name in purge_names if name in sys.modules}
            old_automations = dict(AutomationHandler.automations)
            old_bindings = dict(AutomationHandler.automation_bindings)
            old_entities = dict(models.EntityHandler.entities)
            old_devices = dict(models.DeviceHandler.devices)

            for name in purge_names:
                sys.modules.pop(name, None)

            AutomationHandler.reset_automations()
            models.EntityHandler.entities = {}
            models.DeviceHandler.devices = {}

            try:
                importlib.import_module('entities')
                importlib.import_module('devices')
                importlib.import_module('domains')
                importlib.import_module(_AUTOMATIONS_MODULE_NAME)
                models.EntityHandler.read_states()
            except Exception:
                for name in purge_names:
                    sys.modules.pop(name, None)
                sys.modules.update(old_modules)
                AutomationHandler.automations = old_automations
                AutomationHandler.automation_bindings = old_bindings
                models.EntityHandler.entities = old_entities
                models.DeviceHandler.devices = old_devices
                raise

    def _purge_names(self) -> list[str]:
        names = []
        for existing in list(sys.modules):
            if existing in _GENERATED_MODULE_NAMES or existing == _AUTOMATIONS_MODULE_NAME:
                names.append(existing)
            elif existing.startswith(f'{_AUTOMATIONS_MODULE_NAME}.'):
                names.append(existing)
            elif any(existing.startswith(f'{n}.') for n in _GENERATED_MODULE_NAMES):
                names.append(existing)
        for name in (*_GENERATED_MODULE_NAMES, _AUTOMATIONS_MODULE_NAME):
            if name not in names:
                names.append(name)
        return names

    # -- event bridge --------------------------------------------------

    @callback
    def _on_state_changed(self, event: Event) -> None:
        # Without @callback, Home Assistant's event bus treats this as a
        # blocking sync function and dispatches it via the executor (a
        # worker thread) instead of calling it directly on the event
        # loop. async_add_executor_job() below is itself only safe to
        # call FROM the loop (it does asyncio.current_task() internally)
        # — called from that other worker thread instead, it fails with
        # "RuntimeError: no running event loop". Found for real: this hit
        # on every single state_changed event, hundreds of times a
        # minute on a busy instance, effectively breaking automation
        # dispatch almost entirely.
        self.hass.async_add_executor_job(self._process_state_changed, dict(event.data))

    @callback
    def _on_zha_event(self, event: Event) -> None:
        self.hass.async_add_executor_job(self._process_zha_event, dict(event.data))

    def _process_state_changed(self, data: dict) -> None:
        with models.RUNTIME_LOCK:
            entity_id = data.get('entity_id')
            entity = models.EntityHandler.entities.get(entity_id)
            if entity:
                new_state = data.get('new_state')
                old_state = data.get('old_state')
                AutomationHandler.register_change(entity)
                entity.state.set_from_state_event({
                    'new_state': new_state.as_dict() if hasattr(new_state, 'as_dict') else new_state,
                    'old_state': old_state.as_dict() if hasattr(old_state, 'as_dict') else old_state,
                })
            self._run_automation_cycle()

    def _process_zha_event(self, data: dict) -> None:
        with models.RUNTIME_LOCK:
            device_id = data.get('device_id')
            device = models.DeviceHandler.devices.get(device_id)
            if device and device.quirk is not None:
                AutomationHandler.register_change(device)
                device.handle_action_data(data)
            self._run_automation_cycle()

    def _run_automation_cycle(self) -> None:
        AutomationHandler.handle_exit_conditions()
        AutomationHandler.check_automations()
        models.DeviceHandler.reset_fired_actions()
        AutomationHandler.run_automations()

    def _on_automation_fired(self, name: str) -> None:
        # Called from run_automations(), which itself runs inside the
        # executor job kicked off by _process_state_changed/_process_zha_event
        # — i.e. off the event loop. dispatcher_send() (not the async_
        # variant) is the thread-safe way to notify listeners from here.
        self.last_would_have_fired = (name, datetime.now(timezone.utc))
        dispatcher_send(self.hass, SIGNAL_RELOAD_COMPLETE)
