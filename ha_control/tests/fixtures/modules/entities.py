import dataclasses
import typing
from importlib.machinery import SourceFileLoader

import ha_control.models as models

domains_path = __file__.replace("entities.py", "domains.py")
my_domains = SourceFileLoader("my_domains", domains_path).load_module()


my_ha_instance = models.HAInstance()


class LightLivingDownLight01(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity light.living_down_light_01"
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        color_mode: str
        brightness: int
        color_temp_kelvin: int
        color_temp: int
        hs_color: list
        rgb_color: list
        xy_color: list
        effect: typing.Any
        off_with_transition: bool
        off_brightness: typing.Any
        friendly_name: str
        supported_features: int
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'color_mode': 'color_temp', 'brightness': 254, 'color_temp_kelvin': 1801, 'color_temp': 555, 'hs_color': [29.751, 100.0], 'rgb_color': [255, 126, 0], 'xy_color': [0.614, 0.373], 'effect': None, 'off_with_transition': False, 'off_brightness': None, 'friendly_name': 'living-down-light-01 Light', 'supported_features': 44})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_01",
        state=state
    )
    entity_id = "light.living_down_light_01"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1"
    name = "living-down-light-01 Light"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi6(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_6"

        state_value: typing.Any = None

    state = _StateClass(**{})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_6",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_6"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-0-rssi"
    name = "None"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi6(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6"

        state_value: typing.Any = None

    state = _StateClass(**{})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-0-lqi"
    name = "None"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class SensorBedMainSwitch01Battery(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity sensor.bed_main_switch_01_battery"
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.5, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'bed-main-switch-01 Battery'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.bed_main_switch_01_battery",
        state=state
    )
    entity_id = "sensor.bed_main_switch_01_battery"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-1"
    name = "bed-main-switch-01 Battery"
    device_id = "f61b9317af000c4b650b5d686343895e"


class ButtonBedMainSwitch01Identify(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity button.bed_main_switch_01_identify"
        device_class: str
        friendly_name: str
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-main-switch-01 Identify'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_main_switch_01_identify",
        state=state
    )
    entity_id = "button.bed_main_switch_01_identify"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-3"
    name = "bed-main-switch-01 Identify"
    device_id = "f61b9317af000c4b650b5d686343895e"
