import logging
from functools import wraps
from types import FunctionType
import hapy.homeassistant as homeassistant
import hapy.helpers as helpers
from hapy.config import settings


logger = helpers.get_logger('models')


def has_new_state(state):
    if not state:
        return False
    if type(state) is not list:
        return False
    if type(state[0]) is dict and 'attributes' in state[0]:
        return True
    return False


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


class HAInstance(homeassistant.HAInstance):
    def __init__(self):
        super().__init__(ha_api_url=settings.ha_api_url, ha_ws_url=settings.ha_ws_url, ha_token=settings.ha_token)


class Domain(metaclass=DomainFactory):
    def __init__(self, entity_id, state, instance):
        self.instance = instance
        self.entity_id = entity_id
        self.state = state
        self.domain_name = entity_id.split('.')[0]


class EntityHandler(type):
    entities = {}
    homeassistant = HAInstance()
    track_access = dict()

    @classmethod
    def reset_access(cls):
        cls.track_access = dict()

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
        states = cls.homeassistant.get_states()
        for state in states:
            entity_id = state.get('entity_id')
            if entity_id in cls.entities:
                entity = cls.entities.get(entity_id)
                state_attrs = dict(
                    state_value=state.get('state'),
                    last_changed=state.get('last_changed'),
                    last_updated=state.get('last_updated'),
                    ** state.get('attributes')
                )
                entity.state.set_state(**state_attrs)


class Entity(metaclass=EntityHandler):
    entity_id = None

    @classmethod
    @property
    def id(cls):
        return cls.entity_id


class State:

    def __init__(self, state_value=None, last_changed=None, last_updated=None, **attributes):
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
        old_state_data = event_data.get('old_state', {})
        old_state_value = old_state_data.get('state')
        old_state_changed = old_state_data.get('last_changed')
        old_state_updated = old_state_data.get('last_updated')
        self.old = State(
            state_value=old_state_value,
            last_changed=old_state_changed,
            last_updated=old_state_updated,
            **old_state_data.get('attributes', {})
        )

    def changed(self, old_value=None, new_value=None, offset=60):
        old_value = old_value if old_value is not None else self.old.state_value
        new_value = new_value if new_value is not None else self.state_value

        return (
            old_value == self.old.state_value
            and new_value == self.state_value
            and new_value != old_value
            and (helpers.get_now() - self.last_changed).seconds < offset
        )

    def updated(self, attribute, old_value=None, new_value=None, seconds=5):
        old_value = old_value if old_value is not None else getattr(self.old, attribute)
        new_value = new_value if new_value is not None else getattr(self, attribute)
        return (
            old_value == getattr(self.old, attribute)
            and new_value == getattr(self, attribute)
            and new_value != old_value
            and (helpers.get_now() - self.last_updated).seconds < seconds
        )


class DeviceHandler(type):
    devices = {}
    fired_actions = []
    track_access = dict()

    @classmethod
    def reset_access(cls):
        cls.track_access = dict()

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
                    f'reset_fired_actions: {device.__name__}.{action} released'
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
                    if not all(data[key].get(k) == v for k, v in value.items()):
                        break
                elif data.get(key) != value:
                    break
            else:
                if hasattr(cls, action):
                    setattr(cls, action, True)
                    DeviceHandler.fired_actions.append((cls.device_id, action))
                    logger.info(
                        f'handle_action_data: '
                        f'{cls.devices[cls.device_id].__name__}.{action} fired'
                    )


    @classmethod
    @property
    def id(cls):
        return cls.device_id
