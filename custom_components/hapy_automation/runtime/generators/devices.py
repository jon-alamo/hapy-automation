"""Generates the `devices.py` module imported by user automation code
(`import devices`) — ported from hapy/generators/devices.py. Quirk
resolution now lives in runtime/zigbee.py (get_device_quirk), reached from
generated code via the same stable dotted path used for models.
"""
from .. import helpers
from .. import zigbee

RUNTIME_IMPORT = (
    "from custom_components.hapy_automation.runtime import models\n"
    "from custom_components.hapy_automation.runtime import zigbee as gen_devices"
)

module_tmpl = """
{runtime_import}
import entities as my_entities
"""

device_tmpl = '''
class {class_name}(models.Device):
    {quirk_def_statement}
    device_id = "{device_id}"
    unique_id = "{unique_id}"

    class entities:
        """Device entities"""
{entities_references}

{action_references}
'''


def get_entities_references(register, device_id, indent_level=2):
    added_entities = []
    for entity_id in register.get('devices2entities', {}).get(device_id, []):
        if entity_id in register['entities']:
            indent = indent_level * helpers.INDENT
            entity_name = helpers.Pythonize.method_name(entity_id)
            if entity_name not in added_entities:
                added_entities.append(entity_name)
                entity_ref = helpers.Pythonize.class_name(entity_id)
                yield f'{" " * indent}{entity_name} = my_entities.{entity_ref}'


def get_action_references(quirk, quirk_attribute, indent_level=1):
    indent = indent_level * helpers.INDENT
    actions = list(zigbee.get_action_references(quirk, quirk_attribute))
    if actions:
        for action in actions:
            yield f'{" " * indent}{action} = False'
    else:
        yield f'{" " * indent}no_action = False'


def generate_device_class(register, device_id, device_data):
    class_name = helpers.get_device_class_name(device_data['name'], device_id)
    unique_id = device_data.get('unique_id', None)
    quirk, quirk_attribute = zigbee.get_device_quirk(
        device_data['manufacturer'], device_data['model']
    )
    entities_references = '\n'.join(get_entities_references(register, device_id))
    if quirk and device_data['manufacturer']:
        quirk_def_statement = (
            f'quirk, quirk_attribute = gen_devices.get_device_quirk('
            f'"{device_data["manufacturer"]}", "{device_data["model"]}")'
        )
        action_references = '\n'.join(get_action_references(quirk, quirk_attribute))
    else:
        quirk_def_statement = 'quirk, quirk_attribute = None, None'
        action_references = ''
    return device_tmpl.format(
        class_name=class_name,
        quirk_def_statement=quirk_def_statement,
        device_id=device_id,
        unique_id=unique_id,
        action_references=action_references,
        entities_references=entities_references
    )


def generate_devices_module(register):
    header = module_tmpl.format(runtime_import=RUNTIME_IMPORT)
    devices = [header] + [
        generate_device_class(register, device_id, device_data)
        for device_id, device_data in register['devices'].items()
    ]
    return '\n'.join(devices)


def write_devices_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_devices_module(register))
    return module_path
