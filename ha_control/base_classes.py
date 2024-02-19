from . import ha_websocket, ha_restapi
from functools import wraps

allowed_methods = {
    'light': ['turn_on', 'turn_off', 'dim_step', 'set_color',
              'set_temperature', 'set_brightness', 'get_state'],
    'switch': ['turn_on', 'turn_off', 'get_state'],
    'sensor': ['get_state'],
    'binary_sensor': ['get_state']
}


def validate(func):
    @wraps(func)
    def wrapper(cls, *args, **kwargs):
        entity_type = cls.entity_id.split('.')[0]
        if func.__name__ not in allowed_methods[entity_type]:
            raise Exception(f'Invalid method for {entity_type}')
        return func(cls, *args, **kwargs)
    return wrapper


class BaseEntity:
    entity_id = None

    @classmethod
    @validate
    def turn_on(cls):
        ha_websocket.send({
            "id": ha_websocket.get_id(),
            "type": "call_service",
            "domain": "light",
            "service": "turn_on",
            "service_data": {
                "entity_id": cls.entity_id
            }
        })

    @classmethod
    @validate
    def turn_off(cls):
        ha_websocket.send({
            "id": ha_websocket.get_id(),
            "type": "call_service",
            "domain": "light",
            "service": "turn_off",
            "service_data": {
                "entity_id": cls.entity_id
            }
        })

    @classmethod
    @validate
    def dim_step(cls, step_pct):
        ha_websocket.send({
            "id": ha_websocket.get_id(),
            "type": "call_service",
            "domain": "light",
            "service": "turn_on",
            "service_data": {
                "entity_id": cls.entity_id,
                "brightness_step_pct": step_pct
            }
        })

    @classmethod
    @validate
    def get_state(cls):
        return ha_restapi.get_state(cls.entity_id)
