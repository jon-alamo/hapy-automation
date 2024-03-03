import os
import json
import ha_control.register as register
import ha_control.generators as generators
import ha_control.ha_instance as ha_instance
from ha_control.automations import Automation
from ha_control.application import Application


def generate_modules(directory, ha_url, ha_token):
    os.makedirs(directory, exist_ok=True)
    ha = ha_instance.HAInstance(ha_url=ha_url, ha_token=ha_token)
    cur_reg = get_registry(directory)
    reg_data = register.get_registry(ha, directory=directory, reg_data=cur_reg)
    domains_module_path = f'{directory}/domains.py'
    entities_module_path = f'{directory}/entities.py'
    devices_module_path = f'{directory}/devices.py'
    generators.domains.write_domain_module(reg_data, domains_module_path)
    generators.entities.write_entities_module(
        reg_data, entities_module_path,
        domains_route='domains',
        devices_route='devices'
    )
    generators.devices.write_devices_module(reg_data, devices_module_path)


def get_registry(directory='.'):
    if not os.path.exists(f'{directory}/.registry'):
        return None
    with open(f'{directory}/.registry', 'r', encoding="utf-8") as f:
        return json.load(f)
