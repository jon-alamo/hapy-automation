"""Entity/Device/State/Domain runtime models — ported from hapy/models.py.

Two things changed relative to the original:
  1. Transport: HAInstance (REST+WS client) is replaced by HassBridge, a
     thin thread-safe bridge from the worker thread each running Automation
     executes in, back onto the Home Assistant event loop, using
     asyncio.run_coroutine_threadsafe(). No outbound network calls.
  2. Nothing else. The clock-skew fix in State.changed()/updated() (line
     with abs(...total_seconds()) below) and the thread-local discovery-mode
     machinery that prevents `or`-chain short-circuiting during binding
     discovery are ported verbatim — those are pure logic, not transport.
"""
import asyncio
import logging
import threading
from functools import wraps
from types import FunctionType

from . import helpers

logger = logging.getLogger(__name__)

_discovery_state = threading.local()

_hass = None  # set once via set_hass() during async_setup_entry
_dry_run = False


def set_hass(hass):
    global _hass
    _hass = hass


def get_hass():
    if _hass is None:
        raise RuntimeError(
            "hapy_automation.runtime.models.set_hass() was never called — "
            "the integration must call it during async_setup_entry before "
            "importing any generated entities/devices/domains module."
        )
    return _hass


def set_dry_run(value: bool) -> None:
    global _dry_run
    _dry_run = value


def is_dry_run() -> bool:
    return _dry_run


def enter_discovery_mode():
    """Binding discovery runs init_condition() once, at class-definition
    time, purely to see which entities/devices it touches (via
    EntityHandler/DeviceHandler's access tracking) — the boolean result is
    thrown away. While active, State.changed()/updated() always return
    False so an `or`-chain of `.changed()` checks (the idiomatic way to
    write init_condition) can never short-circuit past a real check just
    because that particular entity happened to change recently — which
    would silently drop the binding for every entity after it in the
    chain. Thread-local so it can't bleed into automation threads running
    concurrently with a reload."""
    _discovery_state.active = True


def exit_discovery_mode():
    _discovery_state.active = False


def in_discovery_mode():
    return getattr(_discovery_state, 'active', False)


def service_call(fcn):
    @wraps(fcn)
    def wrapper(self, *args, **kwargs):
        kwargs['entity_id'] = self.entity_id
        service_name = fcn.__name__
        return self.instance.call_service(
            domain=self.domain_name, service=service_name, data=kwargs
        )
    return wrapper


class DomainFactory(type):
    def __new__(cls, classname, bases, class_dict):
        new_class_dict = {}
        for attributeName, attribute in class_dict.items():
            if isinstance(attribute, FunctionType):
                if not attributeName.startswith('_'):
                    attribute = service_call(attribute)
            new_class_dict[attributeName] = attribute
        return type.__new__(cls, classname, bases, new_class_dict)


class Domain(metaclass=DomainFactory):
    def __init__(self, entity_id, state, instance):
        self.instance = instance
        self.entity_id = entity_id
        self.state = state
        self.domain_name = entity_id.split('.')[0]


class HassBridge:
    """Thread-safe bridge from an Automation's worker thread back onto the
    Home Assistant event loop. Replaces hapy.homeassistant.HAInstance's
    outbound REST/WebSocket calls with in-process hass calls."""

    def __init__(self, hass):
        self.hass = hass

    def call_service(self, domain, service, data, timeout=30):
        if is_dry_run():
            logger.info('[DRY RUN] would call service %s.%s with %s', domain, service, data)
            return None
        future = asyncio.run_coroutine_threadsafe(
            self.hass.services.async_call(domain, service, data, blocking=True),
            self.hass.loop,
        )
        return future.result(timeout=timeout)

    def get_states(self, timeout=30):
        future = asyncio.run_coroutine_threadsafe(
            self._async_get_states(), self.hass.loop
        )
        return future.result(timeout=timeout)

    async def _async_get_states(self):
        return [s.as_dict() for s in self.hass.states.async_all()]


class EntityHandler(type):
    """Metaclass for every generated `Entity` subclass in entities.py.

    `__getattribute__` is overridden so that *any* attribute access on an
    Entity class (e.g. `entities.MyLight.state`) records that class in
    `track_access`. `AutomationHandler.make_bindings` reads `track_access`
    right after calling an automation's `init_condition()` to learn which
    entities it touched — that's how an automation gets bound to the
    entities that should re-trigger it, with no explicit wiring needed.
    `reset_access()` clears it between automations so accesses don't leak
    from one binding pass into the next.
    """
    entities = {}
    track_access = dict()

    @classmethod
    def reset_access(cls):
        cls.track_access = dict()

    @property
    def id(cls):
        # Class-level "property": `entities.MyLight.id` must work on the
        # *class* itself, not an instance. Stacking `@classmethod` +
        # `@property` on the Entity class body (the original approach) was
        # only ever informally supported by CPython and was removed
        # outright in Python 3.13 (the version modern Home Assistant runs
        # on) — it silently returns the class instead of entity_id. A
        # property on the metaclass is the correct, version-stable way to
        # get a class-level property.
        return type.__getattribute__(cls, 'entity_id')

    @property
    def children(cls):
        state = type.__getattribute__(cls, 'state') if hasattr(cls, 'state') else None
        if state is not None and hasattr(state, 'entity_id') and isinstance(state.entity_id, list):
            return [
                cls.entities.get(eid) for eid in state.entity_id
                if cls.entities.get(eid) is not None
            ]
        return []

    def __getattribute__(cls, name):
        try:
            ent_id = type.__getattribute__(cls, 'entity_id')
            type.__getattribute__(cls, 'track_access')[ent_id] = cls
        except AttributeError:
            pass
        return type.__getattribute__(cls, name)

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if 'entity_id' in class_dict:
            cls.entities[class_dict['entity_id']] = new_class
        return new_class

    @classmethod
    def read_states(cls):
        bridge = HassBridge(get_hass())
        states = bridge.get_states()
        for state in states:
            entity_id = state.get('entity_id')
            if entity_id in cls.entities:
                entity = cls.entities.get(entity_id)
                state_attrs = dict(
                    state_value=state.get('state'),
                    last_changed=state.get('last_changed'),
                    last_updated=state.get('last_updated'),
                    **state.get('attributes')
                )
                entity.state.set_state(**state_attrs)


class Entity(metaclass=EntityHandler):
    entity_id = None


class State:

    def __init__(self, actual_entity_id=None, ha_instance=None, state_value=None,
                 last_changed=None, last_updated=None, **attributes):
        self.ha_instance = ha_instance
        self.actual_entity_id = actual_entity_id
        self.old = self
        self.state_value = helpers.parse_string_value(state_value)
        self.last_changed = helpers.parse_date(last_changed)
        self.last_updated = helpers.parse_date(last_updated)
        self.set_attributes(**attributes)

    def set_attributes(self, **attributes):
        for key, value in attributes.items():
            pythonized = helpers.Pythonize.parameter_name(key)
            setattr(self, pythonized, value)

    def set_state(self, state_value, last_changed, last_updated, **attributes):
        self.old = State(**self.__dict__)
        self.state_value = helpers.parse_string_value(state_value)
        self.last_changed = helpers.parse_date(last_changed)
        self.last_updated = helpers.parse_date(last_updated)
        self.set_attributes(**attributes)

    def set_from_state_event(self, event_data):
        new_state = event_data.get('new_state')
        state_value = new_state.get('state')
        last_changed = new_state.get('last_changed')
        last_updated = new_state.get('last_updated')
        self.set_state(
            state_value=state_value,
            last_changed=last_changed,
            last_updated=last_updated,
            **new_state.get('attributes')
        )
        old_state_data = event_data.get('old_state') or {}
        old_state_value = old_state_data.get('state')
        old_state_changed = old_state_data.get('last_changed')
        old_state_updated = old_state_data.get('last_updated')
        self.old = State(
            state_value=old_state_value,
            last_changed=old_state_changed,
            last_updated=old_state_updated,
            **(old_state_data.get('attributes') or {})
        )

    def changed(self, old_value=None, new_value=None, offset=60):
        if in_discovery_mode():
            return False
        old_value = old_value if old_value is not None else self.old.state_value
        new_value = new_value if new_value is not None else self.state_value

        return (
            old_value == self.old.state_value
            and new_value == self.state_value
            and new_value != old_value
            # Clock-skew fix: a negative timedelta (local clock a few ms
            # behind the remote timestamp) normalizes to a huge positive
            # `.seconds` value and silently fails this check. abs() on
            # total_seconds() avoids that entirely. Do not revert to
            # `.seconds` — see hapy/tests/test_entities/test_state_changes.py.
            and abs((helpers.get_now() - self.last_changed).total_seconds()) < offset
        )

    def updated(self, attribute, old_value=None, new_value=None, seconds=5):
        if in_discovery_mode():
            return False
        old_value = old_value if old_value is not None else getattr(self.old, attribute)
        new_value = new_value if new_value is not None else getattr(self, attribute)
        return (
            old_value == getattr(self.old, attribute)
            and new_value == getattr(self, attribute)
            and new_value != old_value
            and abs((helpers.get_now() - self.last_updated).total_seconds()) < seconds
        )


class DeviceHandler(type):
    """Metaclass for every generated `Device` subclass in devices.py.

    Same access-tracking trick as `EntityHandler`, but for ZHA device
    action triggers (e.g. `devices.MySwitch.button_press`) instead of
    entity state.
    """
    devices = {}
    fired_actions = []
    track_access = dict()

    @classmethod
    def reset_access(cls):
        cls.track_access = dict()

    @property
    def id(cls):
        # See EntityHandler.id — a property on the metaclass, not
        # @classmethod+@property on the class body (removed in Python 3.13).
        return type.__getattribute__(cls, 'device_id')

    def __getattribute__(cls, name):
        try:
            device_id = type.__getattribute__(cls, 'device_id')
            type.__getattribute__(cls, 'track_access')[device_id] = cls
        except AttributeError:
            pass
        return type.__getattribute__(cls, name)

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if 'device_id' in class_dict:
            cls.devices[class_dict['device_id']] = new_class
        return new_class

    @classmethod
    def reset_fired_actions(cls):
        for device_id, action in cls.fired_actions:
            device = cls.devices.get(device_id)
            if device:
                logger.info(
                    '[ACTION] - reset_fired_actions: %s.%s released',
                    device.__name__, action,
                )
                setattr(device, action, False)
        cls.fired_actions = []


class Device(metaclass=DeviceHandler):
    device_id = None
    quirk = None
    quirk_attribute = None

    @classmethod
    def handle_action_data(cls, data):
        device_automation_triggers = getattr(cls.quirk, cls.quirk_attribute)
        for action_names, action_data in device_automation_triggers.items():
            action = helpers.get_action_name(*action_names)
            for key, value in action_data.items():
                if type(value) is dict:
                    if not all(data.get(key, {}).get(k) == v for k, v in value.items()):
                        break
                elif data.get(key) != value:
                    break
            else:
                if hasattr(cls, action):
                    setattr(cls, action, True)
                    DeviceHandler.fired_actions.append((cls.device_id, action))
                    logger.info(
                        '[ACTION] - handle_action_data: %s.%s fired',
                        cls.devices[cls.device_id].__name__, action,
                    )
