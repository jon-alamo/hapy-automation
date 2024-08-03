import zhaquirks
import zigpy.quirks as quirks

import hapy.helpers as helpers
import importlib


# Load all quirks
zhaquirks.setup(zhaquirks.__path__[0])
registries = [
    quirks._DEVICE_REGISTRY._registry, quirks._DEVICE_REGISTRY._registry_v2
]


module_tmpl = """
import hapy.models as models
import hapy.generators.devices as gen_devices
import entities as my_entities
"""

device_tmpl = '''
class {class_name}(models.Device):
    {import_qrk}
    device_id = "{device_id}"
    unique_id = "{unique_id}"
    
    class entities:
        """Device entities"""
{entities_references}

{action_references}
'''


def get_device_quirk(manufacturer, model):
    device_key = manufacturer, model
    for registry in registries:
        if device_key in registry:
            return registry[device_key][0]
    return None


def get_entities_references(register, device_id, indent_level=2):
    added_entities = []
    if device_id in register['devices2entities']:
        for entity_id in register['devices2entities'][device_id]:
            if entity_id in register['entities']:
                indent = indent_level * helpers.INDENT
                entity_name = helpers.Pythonize.method_name(entity_id)
                if entity_name not in added_entities:
                    added_entities.append(entity_name)
                    entity_ref = helpers.Pythonize.class_name(entity_id)
                    yield f'{" " * indent}{entity_name} = my_entities.{entity_ref}'


def get_action_references(quirk, indent_level=1):
    indent = indent_level * helpers.INDENT
    if hasattr(quirk, 'device_automation_triggers_metadata'):
        for action_type, action_name in quirk.device_automation_triggers_metadata:
            action = helpers.get_action_name(action_type, action_name)
            yield f'{" " * indent}{action} = False'
    else:
        yield f'{" " * indent}no_action = False'


def generate_device_class(register, device_id, device_data):
    class_name = helpers.get_device_class_name(device_data['name'], device_id)
    unique_id = device_data.get('unique_id', None)
    quirk = get_device_quirk(
        device_data['manufacturer'], device_data['model']
    )
    entities_references = '\n'.join(get_entities_references(register, device_id))
    if quirk:
        import_qrk = f'quirk = gen_devices.get_device_quirk("{device_data['manufacturer']}", "{device_data['model']}")'
        action_references = '\n'.join(get_action_references(quirk))
    else:
        import_qrk = 'quirk = None'
        action_references = ''
    return device_tmpl.format(
        class_name=class_name,
        import_qrk=import_qrk,
        device_id=device_id,
        unique_id=unique_id,
        action_references=action_references,
        entities_references=entities_references
    )


def generate_devices_module(register):
    devices = [module_tmpl] + [
        generate_device_class(register, device_name, device_data)
        for device_name, device_data in register['devices'].items()
    ]
    return '\n'.join(devices)


def write_devices_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_devices_module(register))
    return module_path
