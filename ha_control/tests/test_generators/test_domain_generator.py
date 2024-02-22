import ha_control.register as register
import ha_control.generators as generators
import unittest as ut
import json


class TestFieldGenerator(ut.TestCase):
    domains_fixture = 'ha_control/tests/fixtures/domains.json'

    def setUp(self) -> None:
        with open(self.domains_fixture, 'r') as f:
            self.domains = json.load(f)

    def test_register_domains(self):
        reg_data = {}
        register.register_domains(self.domains, reg_data)
        generators.write_domain_module(reg_data['domains'], 'my_domains.py')
