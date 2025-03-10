from importlib.machinery import SourceFileLoader
import unittest
import hapy.automations as automations
import hapy.events as events
import importlib


entities_path = 'hapy/tests/fixtures/modules/entities.py'
devices_path = 'hapy/tests/fixtures/modules/devices.py'
automations_path = 'hapy/tests/fixtures/modules/automations.py'


new_aut = """

class OnThingReactWhatever(hapy.Automation):

    def init_condition(self):
        return entities.LightLivingDownLight01.state.brightness > 75


    def action(self):
        return entities.LightLivingDownLight.turn_on(brightness_pct=50)

"""


class TestAutomationsBindings(unittest.TestCase):

    def test_automation_bindings(self):
        devices = SourceFileLoader("devices", devices_path).load_module()
        my_aut = SourceFileLoader("my_aut", automations_path).load_module()
        self.assertIn(
            devices.MainSwitch.id,
            automations.AutomationHandler.automation_bindings
        )
        self.assertIn(
            my_aut.OnPressButton,
            automations.AutomationHandler.automation_bindings[devices.MainSwitch.id].values()
        )

    def test_automation_to_run_on_entity_change(self):
        my_aut = SourceFileLoader("my_aut", automations_path).load_module()
        data = {
            'entity_id': 'light.living_down_light_01',
            'new_state': {'state': 'on', 'attributes': {'brightness_pct': 100}}
        }
        events.handle_state_change(data)
        self.assertIn(
            my_aut.OnLivingLightOn,
            [type(c) for c in automations.AutomationHandler.to_check_automations]
        )

    def test_automation_name_has_module_and_class(self):
        import hapy.tests.fixtures.modules.automations as aut
        self.assertEqual(
            aut.OnPressButton.get_id(),
            'hapy.tests.fixtures.modules.automations.OnPressButton'
        )
