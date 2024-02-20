import os
import importlib
import logging
from .discovered import devices
from .discovered import entities
from .discovered import reference
from . import discover_devices
from . import discover_entities

logger = logging.getLogger('ha_control')

devices_path = devices.__file__
entities_path = devices.__file__

ha_url = os.getenv('HA_URL', '')
ha_token = os.getenv('HA_TOKEN', '')

if ha_url and ha_token:
    discover_devices.run(location=os.path.dirname(devices_path))
    discover_entities.run(location=os.path.dirname(entities_path))
    devices = importlib.reload(module=devices)
    entities = importlib.reload(module=entities)
    reference = importlib.reload(module=reference)

else:
    logger.warning(
        "No hearing assessment instance found. Please define HA_URL and "
        "HA_TOKEN and reload the ha_control module."
    )

def get_entities():
    return {
        entity['name']: getattr(entities, entity['name'])
        for entity in reference.entities.keys()
    }
