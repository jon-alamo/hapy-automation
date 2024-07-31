import os as _os
import json as _json
import subprocess as _subprocess

import hapy.register as _register
import hapy.generators as _generators
import hapy.homeassistant as _homeassistant
import hapy.commands as _commands
import hapy.git_sync as _git_sync

from hapy.automations import Automation
from hapy.application import Application

LOCAL_PATH = '.'


def is_project():
    dir_files = _os.listdir(LOCAL_PATH)
    if (
            'application.py' not in dir_files
            and 'automations' not in dir_files
            and 'automations.py' not in dir_files

    ):
        return False
    return True


def init_project():
    _git_sync.setup_ssh()
    _git_sync.pull_repo()
    if not is_project():
        _commands.create_update_project(LOCAL_PATH)
        _git_sync.push_repo()
    req_file = _os.path.join(LOCAL_PATH, 'requirements.txt')
    install_requirements(req_file)


def generate_modules(directory, ha_api_url, ha_ws_url, ha_token):
    _os.makedirs(directory, exist_ok=True)
    ha = _homeassistant.HAInstance(
        ha_api_url=ha_api_url, ha_ws_url=ha_ws_url, ha_token=ha_token
    )
    cur_reg = get_registry(directory)
    reg_data = _register.get_registry(ha, directory=directory, reg_data=cur_reg)
    domains_module_path = f'{directory}/domains.py'
    entities_module_path = f'{directory}/entities.py'
    devices_module_path = f'{directory}/devices.py'
    _generators.domains.write_domain_module(reg_data, domains_module_path)
    _generators.entities.write_entities_module(
        reg_data, entities_module_path,
        domains_route='domains',
        devices_route='devices'
    )
    _generators.devices.write_devices_module(reg_data, devices_module_path)


def install_requirements(req_file):
    if _os.path.exists(req_file):
        _subprocess.check_call(['pip', 'install', '-r', req_file])


def get_registry(directory='.'):
    if not _os.path.exists(f'{directory}/.registry'):
        return None
    with open(f'{directory}/.registry', 'r', encoding="utf-8") as f:
        return _json.load(f)
