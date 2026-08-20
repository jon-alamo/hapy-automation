"""Hapy Automation — run Python-authored Home Assistant automations
(hapy.Automation) natively inside HA's own process, deployed by pointing
the integration at a git repo. See plan doc for the full design."""
from __future__ import annotations

import logging
import os

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.components import webhook
from homeassistant.helpers import config_validation as cv

from .const import (
    CONF_ENABLE_AGENT,
    CONF_ENABLE_WEBHOOK,
    CONF_WEBHOOK_ID,
    DOMAIN,
    SERVICE_EXPORT_STUBS,
    SERVICE_RELOAD,
)
from .coordinator import HapyCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ['sensor', 'button']

SERVICE_EXPORT_STUBS_SCHEMA = vol.Schema({
    vol.Optional('destination'): str,
})


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    coordinator = HapyCoordinator(hass, entry)
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await coordinator.async_start()

    if entry.data.get(CONF_ENABLE_WEBHOOK) and entry.data.get(CONF_WEBHOOK_ID):
        async def _handle_webhook(hass: HomeAssistant, webhook_id: str, request):
            _LOGGER.info('[hapy_automation] webhook trigger received, reloading')
            await coordinator.async_reload()
            return None

        webhook.async_register(
            hass, DOMAIN, 'Hapy Automation reload', entry.data[CONF_WEBHOOK_ID], _handle_webhook
        )

    if entry.data.get(CONF_ENABLE_AGENT):
        from .agent.runner import AgentRunner  # local import: aiohttp-heavy, only needed if enabled
        coordinator.agent_runner = AgentRunner(hass, entry, coordinator)
        coordinator.agent_runner.start()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    _async_register_services(hass)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator: HapyCoordinator = hass.data[DOMAIN][entry.entry_id]
    if getattr(coordinator, 'agent_runner', None) is not None:
        await coordinator.agent_runner.stop()
    await coordinator.async_stop()

    if entry.data.get(CONF_WEBHOOK_ID):
        webhook.async_unregister(hass, entry.data[CONF_WEBHOOK_ID])

    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unloaded


def _async_register_services(hass: HomeAssistant) -> None:
    if hass.services.has_service(DOMAIN, SERVICE_RELOAD):
        return

    async def _async_handle_reload(call: ServiceCall) -> None:
        for coordinator in hass.data.get(DOMAIN, {}).values():
            await coordinator.async_reload(force=True)

    async def _async_handle_export_stubs(call: ServiceCall) -> None:
        destination = call.data.get('destination') or hass.config.path('www', 'hapy_automation_stubs')
        os.makedirs(destination, exist_ok=True)
        for coordinator in hass.data.get(DOMAIN, {}).values():
            for name in ('entities.py', 'devices.py', 'domains.py'):
                src = os.path.join(coordinator.generated_path, name)
                if os.path.isfile(src):
                    dst = os.path.join(destination, name)
                    await hass.async_add_executor_job(_copy_file, src, dst)
        _LOGGER.info('[hapy_automation] exported stub modules to %s', destination)

    hass.services.async_register(DOMAIN, SERVICE_RELOAD, _async_handle_reload)
    hass.services.async_register(
        DOMAIN, SERVICE_EXPORT_STUBS, _async_handle_export_stubs, schema=SERVICE_EXPORT_STUBS_SCHEMA
    )


def _copy_file(src: str, dst: str) -> None:
    import shutil
    shutil.copyfile(src, dst)
