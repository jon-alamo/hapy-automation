import zhaquirks
import zigpy.quirks as quirks

import hapy.helpers as helpers
import importlib


# Load all quirks
zhaquirks.setup(zhaquirks.__path__[0])
registry_v1 = quirks._DEVICE_REGISTRY._registry
registry_v2 = quirks._DEVICE_REGISTRY._registry_v2


module_tmpl = """
import hapy.models as models
import hapy.generators.devices as gen_devices
import entities as my_entities
"""

device_tmpl = '''
class {class_name}(models.Device):
    {import_qrk}
    {quirk_attribute}
    device_id = "{device_id}"
    unique_id = "{unique_id}"
    
    class entities:
        """Device entities"""
{entities_references}

{action_references}
'''


def get_device_quirk(manufacturer, model):
    if manufacturer in registry_v1:
        if model in registry_v1[manufacturer]:
            quirk = list(registry_v1[manufacturer][model])[0]
            attribute = 'device_automation_triggers'
            return quirk, attribute
    if (manufacturer, model) in registry_v2:
        quirk = list(registry_v2[(manufacturer, model)])[0]
        attribute = 'device_automation_triggers_metadata'
        return quirk, attribute
    return None, None


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


def get_action_references(quirk, quirk_attribute, indent_level=1):
    indent = indent_level * helpers.INDENT
    if hasattr(quirk, quirk_attribute):
        for action_type, action_name in getattr(quirk, quirk_attribute):
            action = helpers.get_action_name(action_type, action_name)
            yield f'{" " * indent}{action} = False'
    else:
        yield f'{" " * indent}no_action = False'


def generate_device_class(register, device_id, device_data):
    class_name = helpers.get_device_class_name(device_data['name'], device_id)
    unique_id = device_data.get('unique_id', None)
    quirk, quirk_attribute = get_device_quirk(
        device_data['manufacturer'], device_data['model']
    )
    entities_references = '\n'.join(get_entities_references(register, device_id))
    if quirk and device_data['manufacturer']:
        quirk_def_statement = f'quirk = gen_devices.get_device_quirk("{device_data['manufacturer']}", "{device_data['model']}")'
        quirk_attr_statement = f'quirk_attribute = "{quirk_attribute}"'
        action_references = '\n'.join(get_action_references(quirk, quirk_attribute))
    else:
        quirk_def_statement = 'quirk = None'
        quirk_attr_statement = 'quirk_attribute = None'
        action_references = ''
    return device_tmpl.format(
        class_name=class_name,
        import_qrk=quirk_def_statement,
        quirk_attribute=quirk_attr_statement,
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
