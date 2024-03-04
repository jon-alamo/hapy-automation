from importlib.machinery import SourceFileLoader
import ha_control.models as models


entities_path = __file__.replace("devices.py", "entities.py")
my_entities = SourceFileLoader("my_entities", entities_path).load_module()


class MainLight(models.Device):
    quirk = None
    device_id = "8b1994f323e86cd5eee43419ff7c2495"
    unique_id = "None"

    class entities:
        """Device entities"""
        light_living_down_light_01 = my_entities.LightLivingDownLight01


class MainSwitch(models.Device):
    from zhaquirks.ikea.twobtnremote import IkeaTradfriRemote2BtnZLL as quirk
    device_id = "f61b9317af000c4b650b5d686343895e"
    unique_id = "None"

    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi6
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi6
        sensor_bed_main_switch_01_battery = my_entities.SensorBedMainSwitch01Battery
        button_bed_main_switch_01_identify = my_entities.ButtonBedMainSwitch01Identify

    remote_button_short_press_turn_on = False
    remote_button_long_press_dim_up = False
    remote_button_long_release_dim_up = False
    remote_button_short_press_turn_off = False
    remote_button_long_press_dim_down = False
    remote_button_long_release_dim_down = False
