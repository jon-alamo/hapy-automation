



module_tmpl = """
import ha_control.models as models
"""


device_tmpl = """
class {class_name}(models.Device):
    from {quirk_module_route} import {quirk_name} as quirk
    device_id = "{device_id}"
    unique_id = "{unique_id}"
"""


def generate_devices_module(register):
    return ''


def write_devices_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_devices_module(register))
    return module_path
