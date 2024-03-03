import json
from functools import wraps
from dataclasses import fields
from types import FunctionType
import ha_control.ha_instance as ha_instance
import ha_control.helpers as helpers
from ha_control.config import settings
import zhaquirks.const as zha_const


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
        state = self.instance.call_service(
            domain=self.domain_name, service=service_name, data=kwargs
        )
        if state and has_new_state(state):
            self.state.set_state(**state[0]['attributes'])
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


class HAInstance(ha_instance.HAInstance):
    def __init__(self):
        super().__init__(ha_url=settings.ha_url, ha_token=settings.ha_token)


class Domain(metaclass=DomainFactory):
    def __init__(self, entity_id, state, instance):
        self.instance = instance
        self.entity_id = entity_id
        self.state = state
        self.domain_name = entity_id.split('.')[0]


class EntityHandler(type):
    entities = {}

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if 'entity_id' in class_dict:
            cls.entities[class_dict['entity_id']] = new_class
        return new_class


class Entity(metaclass=EntityHandler):
    pass


class State:

    def __init__(self, **attributes):
        self.old = {}
        self.set_state(**attributes)

    def set_state(self, **attributes):
        old_attributes = {
            field.name: getattr(self, field.name) for field in fields(self)
        }
        self.old = self.__class__(**old_attributes)
        for key, value in attributes.items():
            setattr(self, key, value)


class DeviceHandler(type):
    devices = {}
    fired_actions = []

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
                setattr(device, action, False)
        cls.fired_actions = []


class Device(metaclass=DeviceHandler):

    @classmethod
    def handle_action_data(cls, data):
        for action_names, action_data in cls.quirk.device_automation_triggers.items():
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

