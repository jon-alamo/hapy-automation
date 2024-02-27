import os
import json
import ha_control.register as register
import ha_control.generators as generators
import ha_control.ha_instance as ha_instance
from ha_control.automations import Automation
from ha_control.application import Application


def generate_modules(directory, ha_url, ha_token):
    os.makedirs(directory, exist_ok=True)
    secret_file = os.path.join(directory, '.secret')
    with open(secret_file, 'w', encoding="utf-8") as f:
        json.dump({'ha_url': ha_url, 'ha_token': ha_token}, f)
    ha = ha_instance.HAInstance(ha_url=ha_url, ha_token=ha_token)
    reg_data = register.get_registry(ha, directory=directory)
    domains_module_path = f'{directory}/domains.py'
    entities_module_path = f'{directory}/entities.py'
    devices_module_path = f'{directory}/devices.py'
    generators.domains.write_domain_module(reg_data, domains_module_path)
    generators.entities.write_entities_module(
        reg_data, entities_module_path, domains_route='domains',
        devices_route='devices', secret_file=secret_file
    )
    generators.devices.write_devices_module(reg_data, devices_module_path)


def get_registry(directory='.'):
    if not os.path.exists(f'{directory}/.registry'):
        return None
    with open(f'{directory}/.registry', 'r', encoding="utf-8") as f:
        return json.load(f)


def get_secrets(directory='.'):
    if not os.path.exists(f'{directory}/.secret'):
        return None
    with open(os.path.join(directory, '.secret'), 'r', encoding="utf-8") as f:
        secrets = json.load(f)
        return secrets['ha_url'], secrets['ha_token']

