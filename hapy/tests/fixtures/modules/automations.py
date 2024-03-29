import hapy
from importlib.machinery import SourceFileLoader

entities_path = __file__.replace("automations.py", "entities.py")
devices_path = __file__.replace("automations.py", "devices.py")

entities = SourceFileLoader("entities", entities_path).load_module()
devices = SourceFileLoader("devices", devices_path).load_module()


class OnPressButton(hapy.Automation):

    def init_condition(self):
        return devices.MainSwitch.remote_button_short_press_turn_on

    def action(self):
        return entities.LightLivingDownLight01.services.turn_on()


class OnLivingLightOn(hapy.Automation):

    def init_condition(self):
        return entities.LightLivingDownLight01.state.brightness > 75


    def action(self):
        return entities.LightLivingDownLight.turn_on(brightness_pct=50)

