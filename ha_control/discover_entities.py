import os
import datetime
import dotenv
from . import ha_websocket, class_writer
from .discovered import reference


dotenv.load_dotenv()

LOCATION = 'discovered'


date = str(datetime.datetime.now())
ENTITY_MODULE_TMPL = f"""
# Home Assistant entities at {date}
from . import devices
from ..base_classes import BaseEntity
""".strip()

ENTITY_CLASS_TMPL = """


class {class_name}(BaseEntity):
"""


def add_device_reference(entity):
    if entity['device_id'] in reference.devices:
        return f'\n    device = devices.{reference.devices[entity["device_id"]]}'
    return ''


def parse_entities(entities):
    for entity in entities:
        if entity['name'] is None:
            continue
        class_name = class_writer.pythonize(entity['name'])
        class_def = class_writer.generate_class_definition(
            class_name, entity, ENTITY_CLASS_TMPL
        )
        class_def += add_device_reference(entity)
        yield class_def


def write_entities_module(entities, module_path):
    with open(module_path, 'w') as f:
        f.write(ENTITY_MODULE_TMPL)
        for entity in parse_entities(entities):
            f.write(entity)


def run(location=LOCATION):
    response = ha_websocket.get_entities()
    entities_module = os.path.join(location, 'entities.py')
    write_entities_module(response['result'], entities_module)


if __name__ == '__main__':
    run()
