import hapy.register as register
import unittest as ut
import json


class TestFields(ut.TestCase):
    domains_fixture = 'hapy/tests/fixtures/domains.json'
    devices_fixture = 'hapy/tests/fixtures/devices.json'
    entities_fixture = 'hapy/tests/fixtures/entities.json'
    states_fixture = 'hapy/tests/fixtures/states.json'

    @staticmethod
    def get_fixture(path) -> list | dict:
        with open(path, 'r') as f:
            return json.load(f)

    def test_register_domains(self):
        domains = self.get_fixture(self.domains_fixture)
        reg_data = {}
        register.register_domains(domains, reg_data)
        self.assertTrue('domains' in reg_data)
        self.assertTrue('light' in reg_data['domains'])

    def test_register_entities(self):
        entities = self.get_fixture(self.entities_fixture)
        reg_data = {}
        register.register_entities(entities, reg_data)
        self.assertIn('entities', reg_data)

    def test_register_states(self):
        states = self.get_fixture(self.states_fixture)
        reg_data = {}
        register.register_states(states, reg_data)
        self.assertIn('entities', reg_data)

    def test_register_entities_and_states(self):
        entities = self.get_fixture(self.entities_fixture)
        states = self.get_fixture(self.states_fixture)
        reg_data = {}
        register.register_entities(entities, reg_data)
        register.register_states(states, reg_data)
        self.assertIn('entities', reg_data)

    def test_register_devices(self):
        devices = self.get_fixture(self.devices_fixture)
        reg_data = {}
        register.register_devices(devices, reg_data)
        self.assertIn('devices', reg_data)

