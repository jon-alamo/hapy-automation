import os
import json
import subprocess

import hapy.register as register
import hapy.generators as generators
import hapy.homeassistant as homeassistant
import hapy.commands as commands
import hapy.git_sync as git_sync


LOCAL_PATH = '.'


def is_project():
    dir_files = os.listdir(LOCAL_PATH)
    if (
            'application.py' not in dir_files
            and 'automations' not in dir_files
            and 'automations.py' not in dir_files

    ):
        return False
    return True


def init_project():
    git_sync.setup_ssh()
    git_sync.pull_repo()
    if not is_project():
        commands.create_update_project(LOCAL_PATH)
        git_sync.push_repo()
    req_file = os.path.join(LOCAL_PATH, 'requirements.txt')
    install_requirements(req_file)


def generate_modules(directory, ha_api_url, ha_ws_url, ha_token):
    os.makedirs(directory, exist_ok=True)
    ha = homeassistant.HAInstance(
        ha_api_url=ha_api_url, ha_ws_url=ha_ws_url, ha_token=ha_token
    )
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


def install_requirements(req_file):
    if os.path.exists(req_file):
        subprocess.check_call(['pip', 'install', '-r', req_file])


def get_registry(directory='.'):
    if not os.path.exists(f'{directory}/.registry'):
        return None
    with open(f'{directory}/.registry', 'r', encoding="utf-8") as f:
        return json.load(f)
