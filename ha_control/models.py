import json
from functools import wraps
from types import FunctionType
import ha_control.ha_restapi as ha_restapi
import ha_control.ha_instance as ha_instance


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


class State:

    def __init__(self, attributes):
        self._attributes = attributes
        self.set_state(attributes)

    def set_state(self, attributes):
        for k, v in attributes.items():
            setattr(self, k, v)


class Entity:

    def __init__(
            self, instance, entity_id, unique_id, name, device_id,  attributes,
            domain_class
    ):
        self.instance = instance
        self.entity_id = entity_id
        self.unique_id = unique_id
        self.name = name
        self.device_id = device_id
        self._attributes = attributes
        self._domain_class = domain_class
        self.state = State(attributes)
        self.services = None
        if domain_class is not None:
            self.services = domain_class(
                self.entity_id, self.state, self.instance
            )
