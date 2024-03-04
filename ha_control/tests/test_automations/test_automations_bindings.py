from importlib.machinery import SourceFileLoader
import unittest
import ha_control.automations as automations
import ha_control.event_handler as event_handler


entities_path = 'ha_control/tests/fixtures/modules/entities.py'
devices_path = 'ha_control/tests/fixtures/modules/devices.py'
automations_path = 'ha_control/tests/fixtures/modules/automations.py'


class TestAutomationsBindings(unittest.TestCase):

    def test_automation_bindings(self):
        devices = SourceFileLoader("devices", devices_path).load_module()
        my_aut = SourceFileLoader("my_aut", automations_path).load_module()
        self.assertIn(
            devices.MainSwitch,
            automations.AutomationHandler.automation_bindings
        )
        self.assertIn(
            my_aut.OnPressButton,
            automations.AutomationHandler.automation_bindings[devices.MainSwitch]
        )

    def test_automation_to_run_on_entity_change(self):
        my_aut = SourceFileLoader("my_aut", automations_path).load_module()
        data = {
            'entity_id': 'light.living_down_light_01',
            'new_state': {'state': 'on', 'attributes': {'brightness_pct': 100}}
        }
        event_handler.handle_state_change(data)
        self.assertIn(
            my_aut.OnLivingLightOn,
            automations.AutomationHandler.to_check_automations
        )
