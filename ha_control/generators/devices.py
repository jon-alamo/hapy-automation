import ha_control.helpers as helpers


module_tmpl = """
import ha_control.models as models
from . import entities as my_entities
"""

footer_tmpl = """"""


device_tmpl = '''
class {class_name}(models.Device):
    {import_qrk}
    device_id = "{device_id}"
    unique_id = "{unique_id}"
    
    class entities:
        """Device entities"""
{entities_references}
'''


def get_entities_references(register, device_id, indent_level=2):
    if device_id in register['devices2entities']:
        for entity_id in register['devices2entities'][device_id]:
            if entity_id in register['entities']:
                indent = indent_level * helpers.INDENT
                entity_name = helpers.Pythonize.method_name(entity_id)
                entity_ref = helpers.Pythonize.class_name(entity_id)
                yield f'{" "  * indent}{entity_name} = my_entities.{entity_ref}'


def generate_device_class(register, device_id, device_data):
    class_name = helpers.get_device_class_name(device_data['name'], device_id)
    unique_id = device_data.get('unique_id', None)
    device_title = helpers.get_device_title(
        device_data['manufacturer'], device_data['model']
    )
    entities_references = '\n'.join(get_entities_references(register, device_id))
    if device_title in register['device_signatures']:
        qrk_module, qrk_name = register['device_signatures'][device_title]
        import_qrk = f'from {qrk_module} import {qrk_name} as quirk'
    else:
        import_qrk = 'quirk = None'
    return device_tmpl.format(
        class_name=class_name,
        import_qrk=import_qrk,
        device_id=device_id,
        unique_id=unique_id,
        entities_references=entities_references
    )


def generate_devices_module(register):
    devices = [module_tmpl] + [
        generate_device_class(register, device_name, device_data)
        for device_name, device_data in register['devices'].items()
    ] + [footer_tmpl]
    return '\n'.join(devices)


def write_devices_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_devices_module(register))
    return module_path
