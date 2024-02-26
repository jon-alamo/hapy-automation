import json
from functools import wraps
from types import FunctionType
import ha_control.ha_instance as ha_instance


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
        if has_new_state(state):
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
    def __init__(self, secret_file):
        with open(secret_file, 'r') as f:
            secret = json.load(f)
        super().__init__(ha_url=secret['ha_url'], ha_token=secret['ha_token'])


class Domain(metaclass=DomainFactory):
    def __init__(self, entity_id, state, instance):
        self.instance = instance
        self.entity_id = entity_id
        self.state = state
        self.domain_name = entity_id.split('.')[0]


class Entity:
    pass


class State:

    def set_state(self, **attributes):
        for attribute, value in attributes.items():
            setattr(self, attribute, value)


class Device:
    pass

