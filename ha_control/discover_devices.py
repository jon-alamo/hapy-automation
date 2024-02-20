import os
import datetime
import dotenv
import pprint
from . import ha_websocket, class_writer

dotenv.load_dotenv()

LOCATION = 'discovered'


DEVICE_MODULE_TMPL = f"""
# Home Assistant devices at {str(datetime.datetime.now())}
""".strip()

DEVICE_CLASS_TMPL = """


class {class_name}:
"""


def parse_devices(entities):
    for entity in entities:
        if entity['name_by_user'] is None:
            continue
        class_name = class_writer.pythonize(entity['name_by_user'])
        yield class_writer.generate_class_definition(
            class_name, entity, DEVICE_CLASS_TMPL
        )


def write_devices_module(entities, module_path):
    with open(module_path, 'w') as f:
        f.write(DEVICE_MODULE_TMPL)
        for entity in parse_devices(entities):
            f.write(entity)


def write_devices_reference(devices, reference_module):
    with open(reference_module, 'w') as f:
        f.write(f'# Home Assistant devices at {str(datetime.datetime.now())}\n\n\n')
        reference = {
            device['id']: class_writer.pythonize(device['name_by_user'])
            for device in devices
            if 'name_by_user' in device and device['name_by_user']
        }
        pp = pprint.PrettyPrinter(indent=4)
        f.write(f'devices = {{\n{pp.pformat(reference)[1:-1]}\n}}')


def run(location=LOCATION):
    devices_module = os.path.join(location, 'devices.py')
    reference_module = os.path.join(location, 'reference.py')
    response = ha_websocket.get_devices()
    write_devices_module(response['result'], devices_module)
    write_devices_reference(response['result'], reference_module)


if __name__ == '__main__':
    run()
