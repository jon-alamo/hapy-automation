"""Automation base class + AutomationHandler — ported from hapy/automations.py.

Scheduling/registration logic is pure Python and ported verbatim, including
the metaclass-driven implicit registration+binding (`AutomationHandler.__new__`
-> `make_bindings`) and the thread-per-active-automation execution model
(`run_automations` spawns one `threading.Thread` per matched automation,
`handle_exit_conditions`/`check_automations` drive the cycle every time an
event is processed) — none of that depends on HA vs. the old WS transport.

Two additions over the original:
  - `AutomationHandler.dry_run`: when True, automations are still bound and
    `init_condition()`/`exit_condition()` still evaluate for real, but no
    Home Assistant service call actually goes out — see
    runtime.models.HassBridge.call_service, which is where the no-op
    actually happens (not here), so `action()` bodies run unmodified.
  - `AutomationHandler.on_automation_fired`: callables invoked with the
    automation name whenever run_automations() dispatches it, so the
    integration's diagnostic sensor can show "last automation that would
    have fired" without polling.
"""
import logging
import threading
import time

from . import models

logger = logging.getLogger(__name__)


class AutomationHandler(type):
    to_check_automations = []
    to_run_automations = {}
    running_automations = {}
    automation_bindings = {}
    automations = {}
    dry_run = False
    on_automation_fired = []
    _base_class = None

    # {automation_id: {"bound_to": [entity_id/device_id, ...], "error": str|None}}
    # for every automation processed in the *last* reload — reset in
    # reset_automations(), populated by make_bindings(). Exists because
    # binding failures were otherwise invisible to anything but DEBUG logs:
    # a wrong/hallucinated entities.X or devices.X reference inside
    # init_condition() raises AttributeError, which make_bindings() below
    # catches and just logs a warning — the automation ends up with zero
    # bindings, completely inert, while the reload that created it still
    # reports "ok" (nothing actually crashed). Found for real: an agent
    # wrote and pushed two automations referencing devices.DeviceConnected
    # and entities.TotalPeople, neither of which exist — both silently
    # did nothing, and neither the agent nor the user had anything but a
    # DEBUG-level log line to notice from. See agent/tools.py's
    # git_commit_and_push, which now surfaces this dict directly.
    binding_results = {}

    @classmethod
    def make_bindings(cls, new_class):
        # Reset access-tracking BEFORE this pass, not just after it (the
        # original hapy/automations.py only ever reset at the end too —
        # found for real on the Pi: EntityHandler/DeviceHandler.
        # __getattribute__ unconditionally records every Entity/Device
        # attribute access, discovery mode or not, so ordinary automation
        # execution between reloads (real init_condition()/action() calls
        # responding to real events, for however long the process has
        # been running) keeps writing into the same global track_access
        # dicts that only ever got cleared at the end of the *previous*
        # make_bindings() call. Whatever accumulated there in the meantime
        # — hours of unrelated automation activity — silently became the
        # very first automation's "bindings" on the next reload, without
        # this reset. Observed directly: OnOfficeSwitchJoniOn (a pure
        # device-trigger automation) ended up bound to a couple dozen
        # unrelated entities from across the house.
        models.EntityHandler.reset_access()
        models.DeviceHandler.reset_access()
        models.enter_discovery_mode()
        automation_id = new_class.get_id()
        try:
            new_class().init_condition()
        except Exception as e:
            logger.warning(
                '%s not bound to any entity or device due to init_condition error: %s.',
                new_class.__name__, e,
            )
            cls.binding_results[automation_id] = {'bound_to': [], 'error': str(e)}
            return
        finally:
            models.exit_discovery_mode()
        bound_to = []
        for entity_id in models.EntityHandler.track_access:
            cls.automation_bindings.setdefault(entity_id, {})[automation_id] = new_class
            bound_to.append(entity_id)
            logger.debug('[AUTOMATIONS] make_bindings: %s bound to %s.', new_class.__name__, entity_id)
        for device_id in models.DeviceHandler.track_access:
            cls.automation_bindings.setdefault(device_id, {})[automation_id] = new_class
            bound_to.append(device_id)
            logger.debug('[AUTOMATIONS] make_bindings: %s bound to %s.', new_class.__name__, device_id)
        cls.binding_results[automation_id] = {'bound_to': bound_to, 'error': None}
        models.EntityHandler.reset_access()
        models.DeviceHandler.reset_access()

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if cls._base_class is None and classname == 'Automation':
            cls._base_class = new_class
        else:
            cls.automations[new_class.get_id()] = new_class
        cls.make_bindings(new_class)
        return new_class

    @classmethod
    def reset_automations(cls):
        cls.automation_bindings = {}
        cls.automations = {}
        cls.binding_results = {}

    @classmethod
    def handle_exit_conditions(cls):
        for name in list(cls.running_automations.keys()):
            automation = cls.running_automations[name]
            if automation.exit_condition():
                logger.debug('[AUTOMATIONS] handle_exit_conditions: %s leaving.', name)
                automation.force_exit = True
                cls.running_automations.pop(name)

    @classmethod
    def register_change(cls, item):
        if item.id in cls.automation_bindings:
            triggered = [
                automation() for automation in cls.automation_bindings[item.id].values()
            ]
            cls.to_check_automations.extend(triggered)
            logger.debug(
                '[AUTOMATIONS] register_change: %s triggering %d checks.',
                item.id, len(triggered),
            )

    @classmethod
    def check_automations(cls):
        cls.to_run_automations = {
            automation.__class__.__name__: automation
            for automation in cls.to_check_automations
            if automation.init_condition()
        }
        cls.to_check_automations = []
        if cls.to_run_automations:
            logger.info(
                '[AUTOMATIONS] check_automations: %d automations queued (%s).',
                len(cls.to_run_automations), ', '.join(cls.to_run_automations),
            )

    @classmethod
    def run_automations(cls):
        for name, automation in cls.to_run_automations.items():
            prefix = '[DRY RUN] ' if cls.dry_run else ''
            logger.info('[AUTOMATIONS] %srun_automations: executing %s.', prefix, name)
            cls.running_automations[name] = automation
            thread = threading.Thread(target=automation.run, daemon=True)
            thread.start()
            for callback in cls.on_automation_fired:
                try:
                    callback(name)
                except Exception:
                    logger.exception('on_automation_fired callback failed for %s', name)
        cls.to_run_automations = {}


class Automation(metaclass=AutomationHandler):
    step_time = 0.5
    timeout = 10

    def __init__(self):
        self.force_exit = False

    def action(self):
        raise NotImplementedError('action method must be implemented')

    def init_condition(self):
        return False

    def exit_condition(self):
        return True

    def is_time_out(self, t0):
        return time.time() - t0 > self.timeout

    def run(self):
        # Locked only around action()/exit_condition() — never around the
        # step_time sleep below — so a running automation's poll loop
        # doesn't stall reload or other automations for its whole
        # lifetime, only for each brief condition check/action call. See
        # models.RUNTIME_LOCK's docstring for why this locking exists at
        # all: these calls touch Entity/Device classes the same way
        # binding discovery does.
        #
        # This whole method is the target of a raw threading.Thread — an
        # uncaught exception here doesn't go through our logger at all
        # (Python's default threading.excepthook writes straight to
        # stderr), and on this deployment that turned out to be
        # invisible even in `ha core logs`. Catch broadly and log through
        # our own logger so a broken action()/exit_condition() in user
        # code is never silently swallowed again.
        try:
            self._run()
        except Exception:
            logger.exception('[AUTOMATIONS] %s crashed', self.__class__.__name__)

    def _run(self):
        with models.RUNTIME_LOCK:
            self.action()
        t0 = time.time()
        loops = 0
        while True:
            with models.RUNTIME_LOCK:
                if self.exit_condition():
                    break
                loops += 1
                self.action()
            time.sleep(self.step_time)
            if self.is_time_out(t0):
                logger.debug('[AUTOMATIONS] %s timed out.', self.__class__.__name__)
                return
            if self.force_exit:
                logger.debug('[AUTOMATIONS] %s was forced to exit.', self.__class__.__name__)
                return
        times = 'once' if loops == 0 else f'{loops + 1} times'
        logger.debug('[AUTOMATIONS] %s action triggered %s.', self.__class__.__name__, times)

    @classmethod
    def get_id(cls):
        return '.'.join([cls.__module__, cls.__name__])
