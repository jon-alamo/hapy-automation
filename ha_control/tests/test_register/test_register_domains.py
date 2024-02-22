import ha_control.register as register
import unittest as ut
import json


class TestFields(ut.TestCase):
    domains_fixture = 'ha_control/tests/fixtures/domains.json'

    def setUp(self) -> None:
        with open(self.domains_fixture, 'r') as f:
            self.domains = json.load(f)

    def test_register_domains(self):
        reg_data = {}
        register.register_domains(self.domains, reg_data)
        self.assertTrue('domains' in reg_data)
        self.assertTrue('light' in reg_data['domains'])
