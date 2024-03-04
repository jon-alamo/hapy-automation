import importlib.util
import ha_control.register as register
import ha_control.generators.domains as domains
import ha_control.generators.entities as entities
import unittest as ut
import json
import os
import shutil
import sys


def execute_module(module_path):
    spec = importlib.util.spec_from_file_location("module_name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


class TestFieldGenerator(ut.TestCase):
    domains_fixture = 'ha_control/tests/fixtures/domains.json'
    devices_fixture = 'ha_control/tests/fixtures/devices.json'
    entities_fixture = 'ha_control/tests/fixtures/entities.json'
    states_fixture = 'ha_control/tests/fixtures/states.json'
    domains_module_path = 'ha_control/tests/modules/my_domains.py'
    entities_module_path = 'ha_control/tests/modules/my_entities.py'

    def tearDown(self) -> None:
        shutil.rmtree(os.path.dirname(self.domains_module_path))

    @staticmethod
    def get_fixture(path) -> list | dict:
        with open(path, 'r') as f:
            return json.load(f)

    def generate_modules(self):
        domain_data = self.get_fixture(self.domains_fixture)
        states_data = self.get_fixture(self.states_fixture)
        entities_data = self.get_fixture(self.entities_fixture)
        devices_data = self.get_fixture(self.devices_fixture)

        reg_data = {}

        register.register_domains(domain_data, reg_data)
        register.register_states(states_data, reg_data)
        register.register_entities(entities_data, reg_data)
        register.register_devices(devices_data, reg_data)
        os.mkdir(os.path.dirname(self.domains_module_path))
        domains_module_path = 'ha_control/tests/modules/my_domains.py'
        entities_module_path = 'ha_control/tests/modules/my_entities.py'
        domains.write_domain_module(reg_data, domains_module_path)

        entities.write_entities_module(
            reg_data, entities_module_path, domains_route='my_domains',
            devices_route='my_devices'
        )

    def tests_domain_generator(self):
        self.generate_modules()
        domain_data = self.get_fixture(self.domains_fixture)
        reg_data = {}
        register.register_domains(domain_data, reg_data)
        module_path = 'ha_control/tests/modules/my_domains.py'
        domains.write_domain_module(reg_data, module_path)
        execute_module(module_path)

    def test_entities_generator(self):
        self.generate_modules()
        append_path = os.path.dirname(self.domains_module_path)
        sys.path.append(append_path)
        execute_module(self.entities_module_path)
