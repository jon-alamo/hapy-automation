import zhaquirks
import zigpy.quirks as quirks
import zha.quirks as zha_quirks

import hapy.helpers as helpers
import importlib


# Load all quirks
zhaquirks.setup(zhaquirks.__path__[0])
registry_v1 = quirks.DEVICE_REGISTRY.registry_v1
# registry_v2 was removed from newer zigpy releases; degrade gracefully instead of
# crashing the whole app at import time if it's gone. Newer QuirkBuilder-based
# quirks (IKEA, eWeLink, ...) don't register here at all anymore — see
# get_device_quirk()'s zha.quirks fallback below.
registry_v2 = getattr(quirks.DEVICE_REGISTRY, 'registry_v2', {})


class V2QuirkTriggers:
    """Adapter exposing a v2 QuirkBuilder quirk's device_automation_triggers
    as an attribute, matching how v1 quirk classes carry it, so
    get_action_references()/Device.handle_action_data() don't need to care
    which quirk generation produced it."""

    def __init__(self, triggers):
        self.device_automation_triggers = triggers


module_tmpl = """
import hapy.models as models
import hapy.generators.devices as gen_devices
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
    # QuirkBuilder-based (v2) quirks register into a separate registry keyed
    # by ModelInfo(manufacturer, model), each entry's triggers living under
    # zha_device_factory.quirk_definition. This is a private attribute
    # (_registry) because zha.quirks doesn't expose a public static lookup —
    # only device-instance matching (match_entry) — so this may need
    # revisiting on future zha-quirks upgrades.
    key = zha_quirks.ModelInfo(manufacturer, model)
    for entry in zha_quirks.DEVICE_REGISTRY._registry.get(key, []):
        triggers = entry.zha_device_factory.quirk_definition.device_automation_triggers
        if triggers:
            return V2QuirkTriggers(triggers), 'device_automation_triggers'
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
        quirk_def_statement = f"quirk, quirk_attribute = gen_devices.get_device_quirk(\"{device_data['manufacturer']}\", \"{device_data['model']}\")"
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
    devices = [module_tmpl] + [
        generate_device_class(register, device_name, device_data)
        for device_name, device_data in register['devices'].items()
    ]
    return '\n'.join(devices)


def write_devices_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_devices_module(register))
    return module_path
