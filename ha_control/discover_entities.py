import os
import datetime
import pprint
import dotenv
import importlib
from . import ha_websocket, class_writer
from .discovered import reference

reference = importlib.reload(reference)

dotenv.load_dotenv()

LOCATION = os.path.dirname(__file__)


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


def write_entities_reference(entities, reference_module):
    devices = reference.devices
    with open(reference_module, 'w') as f:
        f.write(f'# Home Assistant devices at {str(datetime.datetime.now())}\n\n\n')
        new_ref = {
            entity['id']: class_writer.pythonize(entity['name'])
            for entity in entities
            if 'name' in entity and entity['name']
        }
        pp = pprint.PrettyPrinter(indent=4)
        f.write(f'devices = {{\n{pp.pformat(devices)[1:-1]}\n}}')
        f.write(f'\n\n\nentities = {{\n{pp.pformat(new_ref)[1:-1]}\n}}')


def write_entities_module(entities, module_path):
    with open(module_path, 'w') as f:
        f.write(ENTITY_MODULE_TMPL)
        for entity in parse_entities(entities):
            f.write(entity)


def run(location=LOCATION):
    response = ha_websocket.get_entities()
    entities_module = os.path.join(location, 'entities.py')
    reference_module = os.path.join(location, 'reference.py')
    write_entities_module(response['result'], entities_module)
    write_entities_reference(response['result'], reference_module)

if __name__ == '__main__':
    run()
