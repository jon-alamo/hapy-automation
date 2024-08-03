
import hapy.models as models
import domains as my_domains
import dataclasses
import typing
from datetime import datetime

my_ha_instance = models.HAInstance()


class BinarySensorRpiPowerStatus(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.rpi_power_status"""
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'problem', 'icon': 'mdi:raspberry-pi', 'friendly_name': 'RPi Power status', 'last_changed': '2024-08-03T10:36:32.178241+00:00', 'last_updated': '2024-08-03T10:36:32.178241+00:00', 'state_value': 'off'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.rpi_power_status",
        state=state
    )
    entity_id = "binary_sensor.rpi_power_status"
    unique_id = "rpi_power"
    name = "RPi Power status"
    device_id = "None"


class UpdateHomeAssistantSupervisorUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.home_assistant_supervisor_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: str
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': True, 'installed_version': '2024.06.2', 'in_progress': False, 'latest_version': '2024.06.2', 'release_summary': None, 'release_url': 'https://github.com/home-assistant/supervisor/releases/tag/2024.06.2', 'skipped_version': None, 'title': 'Home Assistant Supervisor', 'entity_picture': 'https://brands.home-assistant.io/hassio/icon.png', 'friendly_name': 'Home Assistant Supervisor Update', 'supported_features': 1, 'last_changed': '2024-07-25T11:38:29.390754+00:00', 'last_updated': '2024-07-25T11:38:29.390754+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.home_assistant_supervisor_update",
        state=state
    )
    entity_id = "update.home_assistant_supervisor_update"
    unique_id = "home_assistant_supervisor_version_latest"
    name = "Home Assistant Supervisor Update"
    device_id = "d01ab98c93f7e94e7a0f1c31100cc8d6"


class UpdateHomeAssistantCoreUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.home_assistant_core_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: str
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '2024.3.0', 'in_progress': False, 'latest_version': '2024.7.4', 'release_summary': None, 'release_url': 'https://www.home-assistant.io/latest-release-notes/', 'skipped_version': None, 'title': 'Home Assistant Core', 'entity_picture': 'https://brands.home-assistant.io/homeassistant/icon.png', 'friendly_name': 'Home Assistant Core Update', 'supported_features': 11, 'last_changed': '2024-07-25T11:38:29.397016+00:00', 'last_updated': '2024-07-30T11:43:29.861026+00:00', 'state_value': 'on'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.home_assistant_core_update",
        state=state
    )
    entity_id = "update.home_assistant_core_update"
    unique_id = "home_assistant_core_version_latest"
    name = "Home Assistant Core Update"
    device_id = "bac32c0a9033740e54fe621b88d7220b"


class UpdateHomeAssistantOperatingSystemUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.home_assistant_operating_system_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: str
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '12.1', 'in_progress': False, 'latest_version': '12.4', 'release_summary': None, 'release_url': 'https://github.com/home-assistant/operating-system/releases/tag/12.4', 'skipped_version': None, 'title': 'Home Assistant Operating System', 'entity_picture': 'https://brands.home-assistant.io/homeassistant/icon.png', 'friendly_name': 'Home Assistant Operating System Update', 'supported_features': 3, 'last_changed': '2024-07-25T11:38:29.410043+00:00', 'last_updated': '2024-07-25T11:38:29.410043+00:00', 'state_value': 'on'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.home_assistant_operating_system_update",
        state=state
    )
    entity_id = "update.home_assistant_operating_system_update"
    unique_id = "home_assistant_os_version_latest"
    name = "Home Assistant Operating System Update"
    device_id = "1d62450fe5a2c4adc07ab8a4207f276d"


class SensorHomeAssistantOperatingSystemVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_operating_system_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_operating_system_version",
        state=state
    )
    entity_id = "sensor.home_assistant_operating_system_version"
    unique_id = "home_assistant_os_version"
    name = "None"
    device_id = "1d62450fe5a2c4adc07ab8a4207f276d"


class SensorHomeAssistantOperatingSystemNewestVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_operating_system_newest_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_operating_system_newest_version",
        state=state
    )
    entity_id = "sensor.home_assistant_operating_system_newest_version"
    unique_id = "home_assistant_os_version_latest"
    name = "None"
    device_id = "1d62450fe5a2c4adc07ab8a4207f276d"


class PersonJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity person.joni"""
        editable: bool
        id: str
        source: str
        user_id: str
        device_trackers: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'editable': True, 'id': 'joni', 'source': 'device_tracker.s23_joni_wifi', 'user_id': '842a16b5b9494c17a847a59b2555eb80', 'device_trackers': ['device_tracker.s23_joni_wifi'], 'friendly_name': 'joni', 'last_changed': '2024-08-03T07:42:29.744214+00:00', 'last_updated': '2024-08-03T07:42:29.744214+00:00', 'state_value': 'home'})
    services = my_domains.Person(
        instance=my_ha_instance,
        entity_id="person.joni",
        state=state
    )
    entity_id = "person.joni"
    unique_id = "joni"
    name = "joni"
    device_id = "None"


class WeatherForecastCasa(models.Entity):

    class _StateClass(models.State):
        """State class for entity weather.forecast_casa"""
        temperature: float
        dew_point: float
        temperature_unit: str
        humidity: int
        cloud_coverage: float
        pressure: float
        pressure_unit: str
        wind_bearing: float
        wind_speed: float
        wind_speed_unit: str
        visibility_unit: str
        precipitation_unit: str
        forecast: list
        attribution: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'temperature': 27.0, 'dew_point': 16.2, 'temperature_unit': '°C', 'humidity': 51, 'cloud_coverage': 0.0, 'pressure': 1012.7, 'pressure_unit': 'hPa', 'wind_bearing': 110.5, 'wind_speed': 8.6, 'wind_speed_unit': 'km/h', 'visibility_unit': 'km', 'precipitation_unit': 'mm', 'forecast': [{'condition': 'sunny', 'datetime': '2024-08-03T10:00:00+00:00', 'wind_bearing': 137.7, 'temperature': 27.3, 'templow': 25.3, 'wind_speed': 22.0, 'precipitation': 0.0, 'humidity': 53}, {'condition': 'partlycloudy', 'datetime': '2024-08-04T10:00:00+00:00', 'wind_bearing': 122.6, 'temperature': 27.8, 'templow': 22.6, 'wind_speed': 24.8, 'precipitation': 0.2, 'humidity': 76}, {'condition': 'sunny', 'datetime': '2024-08-05T10:00:00+00:00', 'wind_bearing': 189.6, 'temperature': 28.5, 'templow': 21.6, 'wind_speed': 25.9, 'precipitation': 0.0, 'humidity': 60}, {'condition': 'partlycloudy', 'datetime': '2024-08-06T10:00:00+00:00', 'wind_bearing': 173.0, 'temperature': 28.4, 'templow': 22.1, 'wind_speed': 17.6, 'precipitation': 0.0, 'humidity': 60}, {'condition': 'partlycloudy', 'datetime': '2024-08-07T10:00:00+00:00', 'wind_bearing': 121.5, 'temperature': 27.5, 'templow': 23.3, 'wind_speed': 14.8, 'precipitation': 0.0, 'humidity': 67}, {'condition': 'sunny', 'datetime': '2024-08-08T10:00:00+00:00', 'wind_bearing': 142.9, 'temperature': 27.7, 'templow': 23.0, 'wind_speed': 13.3, 'precipitation': 0.0, 'humidity': 69}], 'attribution': 'Weather forecast from met.no, delivered by the Norwegian Meteorological Institute.', 'friendly_name': 'Forecast Casa', 'supported_features': 3, 'last_changed': '2024-08-03T05:39:42.104067+00:00', 'last_updated': '2024-08-03T09:51:42.090364+00:00', 'state_value': 'sunny'})
    services = my_domains.Weather(
        instance=my_ha_instance,
        entity_id="weather.forecast_casa",
        state=state
    )
    entity_id = "weather.forecast_casa"
    unique_id = "home"
    name = "Forecast Casa"
    device_id = "9437d9cf851f6d29ea772ca9a8ccb060"


class SensorInnrRs230CRssi9(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_9"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_9",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-0-rssi"
    name = "None"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class SensorInnrRs230CLqi9(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_9"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_9",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-0-lqi"
    name = "None"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class SensorSonoff01minizbRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sonoff_01minizb_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sonoff_01minizb_rssi",
        state=state
    )
    entity_id = "sensor.sonoff_01minizb_rssi"
    unique_id = "00:12:4b:00:26:b6:fc:1f-1-0-rssi"
    name = "None"
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"


class SensorSonoff01minizbLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sonoff_01minizb_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sonoff_01minizb_lqi",
        state=state
    )
    entity_id = "sensor.sonoff_01minizb_lqi"
    unique_id = "00:12:4b:00:26:b6:fc:1f-1-0-lqi"
    name = "None"
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"


class SensorAwoxTlsr82xxRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.awox_tlsr82xx_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.awox_tlsr82xx_rssi",
        state=state
    )
    entity_id = "sensor.awox_tlsr82xx_rssi"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-0-rssi"
    name = "None"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class SensorAwoxTlsr82xxLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.awox_tlsr82xx_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.awox_tlsr82xx_lqi",
        state=state
    )
    entity_id = "sensor.awox_tlsr82xx_lqi"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-0-lqi"
    name = "None"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class SensorAwoxTlsr82xxRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.awox_tlsr82xx_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.awox_tlsr82xx_rssi_2",
        state=state
    )
    entity_id = "sensor.awox_tlsr82xx_rssi_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-0-rssi"
    name = "None"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class SensorAwoxTlsr82xxLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.awox_tlsr82xx_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.awox_tlsr82xx_lqi_2",
        state=state
    )
    entity_id = "sensor.awox_tlsr82xx_lqi_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-0-lqi"
    name = "None"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class SensorInnrRs230CRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-0-rssi"
    name = "None"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class SensorInnrRs230CLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-0-lqi"
    name = "None"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class SensorInnrRs230CRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_2",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-0-rssi"
    name = "None"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class SensorInnrRs230CLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_2",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-0-lqi"
    name = "None"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class SensorInnrRs230CRssi3(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_3"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_3",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_3"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-0-rssi"
    name = "None"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class SensorInnrRs230CLqi3(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_3"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_3",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_3"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-0-lqi"
    name = "None"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class SensorInnrRs230CRssi4(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_4"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_4",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_4"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-0-rssi"
    name = "None"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class SensorInnrRs230CLqi4(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_4"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_4",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_4"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-0-lqi"
    name = "None"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class SensorInnrRs230CRssi5(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_5"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_5",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_5"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-0-rssi"
    name = "None"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class SensorInnrRs230CLqi5(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_5"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_5",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_5"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-0-lqi"
    name = "None"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class SensorInnrRs230CRssi6(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_6"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_6",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_6"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-0-rssi"
    name = "None"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class SensorInnrRs230CLqi6(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_6"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_6",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_6"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-0-lqi"
    name = "None"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class SensorInnrRs230CRssi7(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_7"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_7",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_7"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-0-rssi"
    name = "None"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class SensorInnrRs230CLqi7(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_7"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_7",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_7"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-0-lqi"
    name = "None"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class SensorInnrRs230CRssi8(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_rssi_8"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_rssi_8",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_rssi_8"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-0-rssi"
    name = "None"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class SensorInnrRs230CLqi8(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.innr_rs_230_c_lqi_8"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.innr_rs_230_c_lqi_8",
        state=state
    )
    entity_id = "sensor.innr_rs_230_c_lqi_8"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-0-lqi"
    name = "None"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class SceneSleep(models.Entity):

    class _StateClass(models.State):
        """State class for entity scene.sleep"""
        entity_id: list
        id: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'entity_id': ['light.all_lights_group'], 'id': '1666015034553', 'icon': 'mdi:bed-clock', 'friendly_name': 'sleep', 'last_changed': '2024-08-02T16:14:53.620075+00:00', 'last_updated': '2024-08-02T16:14:53.620075+00:00', 'state_value': '2024-08-02T16:14:53.619562+00:00'})
    services = my_domains.Scene(
        instance=my_ha_instance,
        entity_id="scene.sleep",
        state=state
    )
    entity_id = "scene.sleep"
    unique_id = "1666015034553"
    name = "sleep"
    device_id = "None"


class SceneParty(models.Entity):

    class _StateClass(models.State):
        """State class for entity scene.party"""
        entity_id: list
        id: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'entity_id': ['light.foco_01', 'light.foco_02', 'light.foco_03', 'light.foco_04', 'light.foco_05', 'light.foco_06', 'light.foco_07', 'light.foco_08', 'light.foco_09', 'light.lampara_01', 'light.lampara_02', 'light.plafones'], 'id': '1666017972394', 'icon': 'mdi:party-popper', 'friendly_name': 'party', 'last_changed': '2024-07-25T11:38:40.822330+00:00', 'last_updated': '2024-07-25T11:38:40.822330+00:00', 'state_value': '2024-03-25T17:26:32.923691+00:00'})
    services = my_domains.Scene(
        instance=my_ha_instance,
        entity_id="scene.party",
        state=state
    )
    entity_id = "scene.party"
    unique_id = "1666017972394"
    name = "party"
    device_id = "None"


class BinarySensorFileEditorRunning(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.file_editor_running"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.file_editor_running",
        state=state
    )
    entity_id = "binary_sensor.file_editor_running"
    unique_id = "core_configurator_state"
    name = "None"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class SensorFileEditorVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.file_editor_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.file_editor_version",
        state=state
    )
    entity_id = "sensor.file_editor_version"
    unique_id = "core_configurator_version"
    name = "None"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class SensorFileEditorNewestVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.file_editor_newest_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.file_editor_newest_version",
        state=state
    )
    entity_id = "sensor.file_editor_newest_version"
    unique_id = "core_configurator_version_latest"
    name = "None"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class SensorFileEditorCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.file_editor_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.file_editor_cpu_percent",
        state=state
    )
    entity_id = "sensor.file_editor_cpu_percent"
    unique_id = "core_configurator_cpu_percent"
    name = "None"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class SensorFileEditorMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.file_editor_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.file_editor_memory_percent",
        state=state
    )
    entity_id = "sensor.file_editor_memory_percent"
    unique_id = "core_configurator_memory_percent"
    name = "None"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class UpdateFileEditorUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.file_editor_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: str
        release_url: typing.Any
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '5.8.0', 'in_progress': False, 'latest_version': '5.8.0', 'release_summary': '# Changelog\n\n## 5.8.0\n\n- Update base image to Alpine 3.19\n\n## 5.7.0\n\n- Use new location for accessing the Home Assistant configuration folder using `/homeassistant`\n- Add access to the new public configuration folders of add-ons\n- Upgrade to Alpine 3.18\n-', 'release_url': None, 'skipped_version': None, 'title': 'File editor', 'entity_picture': '/api/hassio/addons/core_configurator/icon', 'friendly_name': 'File editor Update', 'supported_features': 25, 'last_changed': '2024-07-25T11:38:29.398961+00:00', 'last_updated': '2024-07-25T11:38:29.398961+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.file_editor_update",
        state=state
    )
    entity_id = "update.file_editor_update"
    unique_id = "core_configurator_version_latest"
    name = "File editor Update"
    device_id = "9ef171592ea1010f3661c65633b6cd56"


class MediaPlayerSamsungQ64ba55Tv(models.Entity):

    class _StateClass(models.State):
        """State class for entity media_player.samsung_q64ba_55_tv"""
        source_list: list
        device_class: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_list': ['TV', 'HDMI'], 'device_class': 'tv', 'friendly_name': 'Samsung Q64BA 55 TV', 'supported_features': 20413, 'last_changed': '2024-08-02T22:28:20.262854+00:00', 'last_updated': '2024-08-02T22:28:20.262854+00:00', 'state_value': 'off'})
    services = my_domains.MediaPlayer(
        instance=my_ha_instance,
        entity_id="media_player.samsung_q64ba_55_tv",
        state=state
    )
    entity_id = "media_player.samsung_q64ba_55_tv"
    unique_id = "f9b4c92f-9810-4e85-b012-8aaf8083263c"
    name = "Samsung Q64BA 55 TV"
    device_id = "f3604fa009d16354ba1e2abbb963f8cd"


class BinarySensorTerminalSshRunning(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.terminal_ssh_running"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.terminal_ssh_running",
        state=state
    )
    entity_id = "binary_sensor.terminal_ssh_running"
    unique_id = "core_ssh_state"
    name = "None"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class SensorTerminalSshVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terminal_ssh_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terminal_ssh_version",
        state=state
    )
    entity_id = "sensor.terminal_ssh_version"
    unique_id = "core_ssh_version"
    name = "None"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class SensorTerminalSshNewestVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terminal_ssh_newest_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terminal_ssh_newest_version",
        state=state
    )
    entity_id = "sensor.terminal_ssh_newest_version"
    unique_id = "core_ssh_version_latest"
    name = "None"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class SensorTerminalSshCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terminal_ssh_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terminal_ssh_cpu_percent",
        state=state
    )
    entity_id = "sensor.terminal_ssh_cpu_percent"
    unique_id = "core_ssh_cpu_percent"
    name = "None"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class SensorTerminalSshMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terminal_ssh_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terminal_ssh_memory_percent",
        state=state
    )
    entity_id = "sensor.terminal_ssh_memory_percent"
    unique_id = "core_ssh_memory_percent"
    name = "None"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class UpdateTerminalSshUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.terminal_ssh_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: str
        release_url: typing.Any
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '9.9.0', 'in_progress': False, 'latest_version': '9.14.0', 'release_summary': '# Changelog\n\n## 9.14.0\n\n- Upgrade Home Assistant CLI to 4.34.0\n\n## 9.13.0\n\n- Enable ha command completion for non-login shell (e.g. the web terminal)\n\n## 9.12.0\n\n- Install completions for ha commands\n- Fix bash_history file check in startup\n\n## 9.11.0\n\n- ', 'release_url': None, 'skipped_version': None, 'title': 'Terminal & SSH', 'entity_picture': '/api/hassio/addons/core_ssh/icon', 'friendly_name': 'Terminal & SSH Update', 'supported_features': 25, 'last_changed': '2024-07-25T11:38:29.401591+00:00', 'last_updated': '2024-07-25T11:38:29.401591+00:00', 'state_value': 'on'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.terminal_ssh_update",
        state=state
    )
    entity_id = "update.terminal_ssh_update"
    unique_id = "core_ssh_version_latest"
    name = "Terminal & SSH Update"
    device_id = "e04484f3a56a3f5a79a50f15e3014644"


class PersonClaudia(models.Entity):

    class _StateClass(models.State):
        """State class for entity person.claudia"""
        editable: bool
        id: str
        source: str
        user_id: str
        device_trackers: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'editable': True, 'id': 'claudia', 'source': 'device_tracker.192_168_1_59', 'user_id': '7ca9b75753cd4c09aac8a2e5b26b2d1a', 'device_trackers': ['device_tracker.192_168_1_59'], 'friendly_name': 'clau', 'last_changed': '2024-08-03T00:31:43.539078+00:00', 'last_updated': '2024-08-03T00:31:43.539078+00:00', 'state_value': 'home'})
    services = my_domains.Person(
        instance=my_ha_instance,
        entity_id="person.claudia",
        state=state
    )
    entity_id = "person.claudia"
    unique_id = "claudia"
    name = "clau"
    device_id = "None"


class SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-0-rssi"
    name = "None"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-0-lqi"
    name = "None"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class SensorIkeaOfSwedenTradfriBulbE27Ww806lmRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-0-rssi"
    name = "None"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class SensorIkeaOfSwedenTradfriBulbE27Ww806lmLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-0-lqi"
    name = "None"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class SensorIkeaOfSwedenTradfriBulbE27Ww806lmRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-0-rssi"
    name = "None"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class SensorIkeaOfSwedenTradfriBulbE27Ww806lmLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-0-lqi"
    name = "None"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class SceneAmbience(models.Entity):

    class _StateClass(models.State):
        """State class for entity scene.ambience"""
        entity_id: list
        id: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'entity_id': ['light.living_down_light_07', 'light.dining_main_light_01', 'light.dining_main_light_02', 'light.galery_light_1', 'light.galery_light_2', 'light.living_down_light_04', 'light.office_downlight_joni', 'light.bed_left_light_light', 'light.bed_right_light_light', 'light.living_ambient_sofa_light'], 'id': '1669908278419', 'icon': 'mdi:home-account', 'friendly_name': 'ambience', 'last_changed': '2024-08-03T10:06:53.385946+00:00', 'last_updated': '2024-08-03T10:06:53.385946+00:00', 'state_value': '2024-08-03T10:06:53.385634+00:00'})
    services = my_domains.Scene(
        instance=my_ha_instance,
        entity_id="scene.ambience",
        state=state
    )
    entity_id = "scene.ambience"
    unique_id = "1669908278419"
    name = "ambience"
    device_id = "None"


class BinarySensorRemoteUi(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.remote_ui"""
        restored: bool
        device_class: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'device_class': 'connectivity', 'friendly_name': 'Remote UI', 'supported_features': 0, 'last_changed': '2024-07-25T11:39:37.434142+00:00', 'last_updated': '2024-07-25T11:39:37.434142+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.remote_ui",
        state=state
    )
    entity_id = "binary_sensor.remote_ui"
    unique_id = "cloud-remote-ui-connectivity"
    name = "Remote UI"
    device_id = "None"


class BinarySensorTailscaleRunning(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.tailscale_running"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.tailscale_running",
        state=state
    )
    entity_id = "binary_sensor.tailscale_running"
    unique_id = "a0d7b954_tailscale_state"
    name = "None"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class SensorTailscaleVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tailscale_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tailscale_version",
        state=state
    )
    entity_id = "sensor.tailscale_version"
    unique_id = "a0d7b954_tailscale_version"
    name = "None"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class SensorTailscaleNewestVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tailscale_newest_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tailscale_newest_version",
        state=state
    )
    entity_id = "sensor.tailscale_newest_version"
    unique_id = "a0d7b954_tailscale_version_latest"
    name = "None"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class SensorTailscaleCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tailscale_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tailscale_cpu_percent",
        state=state
    )
    entity_id = "sensor.tailscale_cpu_percent"
    unique_id = "a0d7b954_tailscale_cpu_percent"
    name = "None"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class SensorTailscaleMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tailscale_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tailscale_memory_percent",
        state=state
    )
    entity_id = "sensor.tailscale_memory_percent"
    unique_id = "a0d7b954_tailscale_memory_percent"
    name = "None"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class UpdateTailscaleUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.tailscale_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: str
        release_url: typing.Any
        skipped_version: typing.Any
        title: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0.20.0', 'in_progress': False, 'latest_version': '0.21.0', 'release_summary': '## What’s changed\n\n## ⬆️ Dependency updates\n\n- ⬆️ Update tailscale/tailscale to v1.68.0 @renovate ([#379](https://github.com/hassio-addons/addon-tailscale/pull/379))\n- ⬆️ Update tailscale/tailscale to v1.68.1 @renovate ([#380](https://github.com/hassio-ad', 'release_url': None, 'skipped_version': None, 'title': 'Tailscale', 'entity_picture': '/api/hassio/addons/a0d7b954_tailscale/icon', 'friendly_name': 'Tailscale Update', 'supported_features': 25, 'last_changed': '2024-07-25T11:38:29.404337+00:00', 'last_updated': '2024-07-25T11:38:29.404337+00:00', 'state_value': 'on'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.tailscale_update",
        state=state
    )
    entity_id = "update.tailscale_update"
    unique_id = "a0d7b954_tailscale_version_latest"
    name = "Tailscale Update"
    device_id = "314dd30fce529dbaf8e55aaed367b664"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-0-rssi"
    name = "None"
    device_id = "f61b9317af000c4b650b5d686343895e"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-0-lqi"
    name = "None"
    device_id = "f61b9317af000c4b650b5d686343895e"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_2"
    unique_id = "bc:02:6e:ff:fe:00:3c:36-1-0-rssi"
    name = "None"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_2"
    unique_id = "bc:02:6e:ff:fe:00:3c:36-1-0-lqi"
    name = "None"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi3(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_3"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_3",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_3"
    unique_id = "bc:02:6e:ff:fe:00:2c:8e-1-0-rssi"
    name = "None"
    device_id = "6d1eca1676129527c2ad74b66e39e435"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi3(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_3"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_3",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_3"
    unique_id = "bc:02:6e:ff:fe:00:2c:8e-1-0-lqi"
    name = "None"
    device_id = "6d1eca1676129527c2ad74b66e39e435"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi5(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_5"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_5",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_5"
    unique_id = "bc:02:6e:ff:fe:00:33:7b-1-0-rssi"
    name = "None"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi5(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_5"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_5",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_5"
    unique_id = "bc:02:6e:ff:fe:00:33:7b-1-0-lqi"
    name = "None"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"


class NumberGaleryFlexoLightStartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_flexo_light_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 250, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-flexo-light Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.361161+00:00', 'last_updated': '2024-07-27T14:55:30.361161+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_flexo_light_start_up_color_temperature",
        state=state
    )
    entity_id = "number.galery_flexo_light_start_up_color_temperature"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-768-start_up_color_temperature"
    name = "galery-flexo-light Start-up color temperature"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class ButtonLivingDownLight01Identifybutton9(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_01_identifybutton_9"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-01 Identifybutton', 'last_changed': '2024-07-27T14:55:29.783554+00:00', 'last_updated': '2024-07-27T14:55:29.783554+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_01_identifybutton_9",
        state=state
    )
    entity_id = "button.living_down_light_01_identifybutton_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-3"
    name = "living-down-light-01 Identifybutton"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class LightLivingDownLight01(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_01"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: str
        brightness: int
        color_temp_kelvin: int
        color_temp: int
        hs_color: list
        rgb_color: list
        xy_color: list
        off_with_transition: bool
        off_brightness: typing.Any
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': 'color_temp', 'brightness': 212, 'color_temp_kelvin': 3300, 'color_temp': 303, 'hs_color': [27.395, 49.303], 'rgb_color': [255, 186, 129], 'xy_color': [0.47, 0.377], 'off_with_transition': False, 'off_brightness': None, 'friendly_name': 'living-down-light-01 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:11:02.384917+00:00', 'last_updated': '2024-08-03T10:35:02.366682+00:00', 'state_value': 'on'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_01",
        state=state
    )
    entity_id = "light.living_down_light_01"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1"
    name = "living-down-light-01 Light"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class NumberLivingDownLight01Onlevelconfiguration9(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_01_onlevelconfiguration_9"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-01 Onlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.139377+00:00', 'last_updated': '2024-07-27T14:55:30.139377+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_01_onlevelconfiguration_9",
        state=state
    )
    entity_id = "number.living_down_light_01_onlevelconfiguration_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-8-on_level"
    name = "living-down-light-01 Onlevelconfiguration"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class NumberLivingDownLight01Onofftransitiontimeconfiguration9(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_01_onofftransitiontimeconfiguration_9"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-01 Onofftransitiontimeconfiguration', 'last_changed': '2024-07-27T14:55:30.134387+00:00', 'last_updated': '2024-07-27T14:55:30.134387+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_01_onofftransitiontimeconfiguration_9",
        state=state
    )
    entity_id = "number.living_down_light_01_onofftransitiontimeconfiguration_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-8-on_off_transition_time"
    name = "living-down-light-01 Onofftransitiontimeconfiguration"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class NumberLivingDownLight01StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_01_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-01 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.151865+00:00', 'last_updated': '2024-07-27T14:55:30.151865+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_01_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_01_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-768-start_up_color_temperature"
    name = "living-down-light-01 Start-up color temperature"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class NumberLivingDownLight01Startupcurrentlevelconfiguration9(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_01_startupcurrentlevelconfiguration_9"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-01 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.146289+00:00', 'last_updated': '2024-07-27T14:55:30.146289+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_01_startupcurrentlevelconfiguration_9",
        state=state
    )
    entity_id = "number.living_down_light_01_startupcurrentlevelconfiguration_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-8-start_up_current_level"
    name = "living-down-light-01 Startupcurrentlevelconfiguration"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class SelectLivingDownLight01Startuponoffselect9(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_01_startuponoffselect_9"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-01 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.494241+00:00', 'last_updated': '2024-07-27T14:55:30.494241+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_01_startuponoffselect_9",
        state=state
    )
    entity_id = "select.living_down_light_01_startuponoffselect_9"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-6-StartUpOnOff"
    name = "living-down-light-01 Startuponoffselect"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class LightLivingDownLight02(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_02"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 94, 'friendly_name': 'living-down-light-02 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:04.696591+00:00', 'last_updated': '2024-08-03T10:07:04.696591+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_02",
        state=state
    )
    entity_id = "light.living_down_light_02"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1"
    name = "living-down-light-02 Light"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class NumberLivingDownLight02StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_02_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-02 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.199636+00:00', 'last_updated': '2024-07-27T14:55:30.199636+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_02_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_02_start_up_color_temperature"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-768-start_up_color_temperature"
    name = "living-down-light-02 Start-up color temperature"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class ButtonLivingDownLight03Identifybutton2(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_03_identifybutton_2"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-03 Identifybutton', 'last_changed': '2024-07-27T14:55:29.827928+00:00', 'last_updated': '2024-07-27T14:55:29.827928+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_03_identifybutton_2",
        state=state
    )
    entity_id = "button.living_down_light_03_identifybutton_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-3"
    name = "living-down-light-03 Identifybutton"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class LightLivingDownLight03(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_03"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 16, 'friendly_name': 'living-down-light-03 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:05.792114+00:00', 'last_updated': '2024-08-03T10:07:05.792114+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_03",
        state=state
    )
    entity_id = "light.living_down_light_03"
    unique_id = "04:cd:15:ff:fe:34:01:38-1"
    name = "living-down-light-03 Light"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class NumberLivingDownLight03Onlevelconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_03_onlevelconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-03 Onlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.210911+00:00', 'last_updated': '2024-07-27T14:55:30.210911+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_03_onlevelconfiguration_2",
        state=state
    )
    entity_id = "number.living_down_light_03_onlevelconfiguration_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-8-on_level"
    name = "living-down-light-03 Onlevelconfiguration"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class NumberLivingDownLight03Onofftransitiontimeconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_03_onofftransitiontimeconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-03 Onofftransitiontimeconfiguration', 'last_changed': '2024-07-27T14:55:30.206380+00:00', 'last_updated': '2024-07-27T14:55:30.206380+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_03_onofftransitiontimeconfiguration_2",
        state=state
    )
    entity_id = "number.living_down_light_03_onofftransitiontimeconfiguration_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-8-on_off_transition_time"
    name = "living-down-light-03 Onofftransitiontimeconfiguration"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class NumberLivingDownLight03StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_03_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-03 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.220642+00:00', 'last_updated': '2024-07-27T14:55:30.220642+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_03_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_03_start_up_color_temperature"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-768-start_up_color_temperature"
    name = "living-down-light-03 Start-up color temperature"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class NumberLivingDownLight03Startupcurrentlevelconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_03_startupcurrentlevelconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-03 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.215350+00:00', 'last_updated': '2024-07-27T14:55:30.215350+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_03_startupcurrentlevelconfiguration_2",
        state=state
    )
    entity_id = "number.living_down_light_03_startupcurrentlevelconfiguration_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-8-start_up_current_level"
    name = "living-down-light-03 Startupcurrentlevelconfiguration"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class SelectLivingDownLight03Startuponoffselect2(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_03_startuponoffselect_2"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-03 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.515450+00:00', 'last_updated': '2024-07-27T14:55:30.515450+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_03_startuponoffselect_2",
        state=state
    )
    entity_id = "select.living_down_light_03_startuponoffselect_2"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-6-StartUpOnOff"
    name = "living-down-light-03 Startuponoffselect"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class LightLivingDownLight04(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_04"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 51, 'friendly_name': 'living-down-light-04 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:11.247253+00:00', 'last_updated': '2024-08-03T10:07:11.247253+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_04",
        state=state
    )
    entity_id = "light.living_down_light_04"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1"
    name = "living-down-light-04 Light"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class NumberLivingDownLight04StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_04_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-04 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.235883+00:00', 'last_updated': '2024-07-27T14:55:30.235883+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_04_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_04_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-768-start_up_color_temperature"
    name = "living-down-light-04 Start-up color temperature"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class LightLivingDownLight05(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_05"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 94, 'friendly_name': 'living-down-light-05 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:04.656594+00:00', 'last_updated': '2024-08-03T10:07:04.656594+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_05",
        state=state
    )
    entity_id = "light.living_down_light_05"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1"
    name = "living-down-light-05 Light"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class NumberLivingDownLight05StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_05_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-05 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.259891+00:00', 'last_updated': '2024-07-27T14:55:30.259891+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_05_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_05_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-768-start_up_color_temperature"
    name = "living-down-light-05 Start-up color temperature"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class ButtonLivingDownLight06Identifybutton4(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_06_identifybutton_4"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-06 Identifybutton', 'last_changed': '2024-07-27T14:55:29.841264+00:00', 'last_updated': '2024-07-27T14:55:29.841264+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_06_identifybutton_4",
        state=state
    )
    entity_id = "button.living_down_light_06_identifybutton_4"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-3"
    name = "living-down-light-06 Identifybutton"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class LightLivingDownLight06(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_06"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 94, 'friendly_name': 'living-down-light-06 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:03.787515+00:00', 'last_updated': '2024-08-03T10:07:03.787515+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_06",
        state=state
    )
    entity_id = "light.living_down_light_06"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1"
    name = "living-down-light-06 Light"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class NumberLivingDownLight06Onlevelconfiguration4(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_06_onlevelconfiguration_4"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-06 Onlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.269079+00:00', 'last_updated': '2024-07-27T14:55:30.269079+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_06_onlevelconfiguration_4",
        state=state
    )
    entity_id = "number.living_down_light_06_onlevelconfiguration_4"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-8-on_level"
    name = "living-down-light-06 Onlevelconfiguration"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class NumberLivingDownLight06Onofftransitiontimeconfiguration4(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_06_onofftransitiontimeconfiguration_4"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-06 Onofftransitiontimeconfiguration', 'last_changed': '2024-07-27T14:55:30.265146+00:00', 'last_updated': '2024-07-27T14:55:30.265146+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_06_onofftransitiontimeconfiguration_4",
        state=state
    )
    entity_id = "number.living_down_light_06_onofftransitiontimeconfiguration_4"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-8-on_off_transition_time"
    name = "living-down-light-06 Onofftransitiontimeconfiguration"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class NumberLivingDownLight06StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_06_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-06 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.279617+00:00', 'last_updated': '2024-07-27T14:55:30.279617+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_06_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_06_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-768-start_up_color_temperature"
    name = "living-down-light-06 Start-up color temperature"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class NumberLivingDownLight06Startupcurrentlevelconfiguration4(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_06_startupcurrentlevelconfiguration_4"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-06 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.273147+00:00', 'last_updated': '2024-07-27T14:55:30.273147+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_06_startupcurrentlevelconfiguration_4",
        state=state
    )
    entity_id = "number.living_down_light_06_startupcurrentlevelconfiguration_4"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-8-start_up_current_level"
    name = "living-down-light-06 Startupcurrentlevelconfiguration"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class SelectLivingDownLight06Startuponoffselect4(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_06_startuponoffselect_4"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-06 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.531577+00:00', 'last_updated': '2024-07-27T14:55:30.531577+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_06_startuponoffselect_4",
        state=state
    )
    entity_id = "select.living_down_light_06_startuponoffselect_4"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-6-StartUpOnOff"
    name = "living-down-light-06 Startuponoffselect"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class LightLivingDownLight07(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_07"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 128, 'friendly_name': 'living-down-light-07 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:11.046963+00:00', 'last_updated': '2024-08-03T10:07:11.046963+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_07",
        state=state
    )
    entity_id = "light.living_down_light_07"
    unique_id = "0c:43:14:ff:fe:74:10:96-1"
    name = "living-down-light-07 Light"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class NumberLivingDownLight07StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_07_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-07 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.297302+00:00', 'last_updated': '2024-07-27T14:55:30.297302+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_07_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_07_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-768-start_up_color_temperature"
    name = "living-down-light-07 Start-up color temperature"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class LightLivingDownLight08(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_08"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 94, 'friendly_name': 'living-down-light-08 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:03.741528+00:00', 'last_updated': '2024-08-03T10:07:03.741528+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_08",
        state=state
    )
    entity_id = "light.living_down_light_08"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1"
    name = "living-down-light-08 Light"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class NumberLivingDownLight08StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_08_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-08 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.317282+00:00', 'last_updated': '2024-07-27T14:55:30.317282+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_08_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_08_start_up_color_temperature"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-768-start_up_color_temperature"
    name = "living-down-light-08 Start-up color temperature"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class ButtonLivingDownLight09Identifybutton6(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_09_identifybutton_6"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-09 Identifybutton', 'last_changed': '2024-07-27T14:55:29.856661+00:00', 'last_updated': '2024-07-27T14:55:29.856661+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_09_identifybutton_6",
        state=state
    )
    entity_id = "button.living_down_light_09_identifybutton_6"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-3"
    name = "living-down-light-09 Identifybutton"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class LightLivingDownLight09(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_down_light_09"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 94, 'friendly_name': 'living-down-light-09 Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:03.858064+00:00', 'last_updated': '2024-08-03T10:07:03.858064+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_down_light_09",
        state=state
    )
    entity_id = "light.living_down_light_09"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1"
    name = "living-down-light-09 Light"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class NumberLivingDownLight09Onlevelconfiguration6(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_09_onlevelconfiguration_6"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-09 Onlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.328771+00:00', 'last_updated': '2024-07-27T14:55:30.328771+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_09_onlevelconfiguration_6",
        state=state
    )
    entity_id = "number.living_down_light_09_onlevelconfiguration_6"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-8-on_level"
    name = "living-down-light-09 Onlevelconfiguration"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class NumberLivingDownLight09Onofftransitiontimeconfiguration6(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_09_onofftransitiontimeconfiguration_6"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-09 Onofftransitiontimeconfiguration', 'last_changed': '2024-07-27T14:55:30.321206+00:00', 'last_updated': '2024-07-27T14:55:30.321206+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_09_onofftransitiontimeconfiguration_6",
        state=state
    )
    entity_id = "number.living_down_light_09_onofftransitiontimeconfiguration_6"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-8-on_off_transition_time"
    name = "living-down-light-09 Onofftransitiontimeconfiguration"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class NumberLivingDownLight09StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_09_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 555, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-09 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.339437+00:00', 'last_updated': '2024-07-27T14:55:30.339437+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_09_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_down_light_09_start_up_color_temperature"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-768-start_up_color_temperature"
    name = "living-down-light-09 Start-up color temperature"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class NumberLivingDownLight09Startupcurrentlevelconfiguration6(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_09_startupcurrentlevelconfiguration_6"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-09 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.332704+00:00', 'last_updated': '2024-07-27T14:55:30.332704+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_09_startupcurrentlevelconfiguration_6",
        state=state
    )
    entity_id = "number.living_down_light_09_startupcurrentlevelconfiguration_6"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-8-start_up_current_level"
    name = "living-down-light-09 Startupcurrentlevelconfiguration"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class SelectLivingDownLight09Startuponoffselect6(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_09_startuponoffselect_6"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-09 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.546660+00:00', 'last_updated': '2024-07-27T14:55:30.546660+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_09_startuponoffselect_6",
        state=state
    )
    entity_id = "select.living_down_light_09_startuponoffselect_6"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-6-StartUpOnOff"
    name = "living-down-light-09 Startuponoffselect"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class ButtonKitchenMainLightIdentifybutton(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.kitchen_main_light_identifybutton"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'kitchen-main-light Identifybutton', 'last_changed': '2024-07-27T14:55:29.808453+00:00', 'last_updated': '2024-07-27T14:55:29.808453+00:00', 'state_value': '2022-10-24T08:54:02.595974+00:00'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.kitchen_main_light_identifybutton",
        state=state
    )
    entity_id = "button.kitchen_main_light_identifybutton"
    unique_id = "00:12:4b:00:26:b6:fc:1f-1-3"
    name = "kitchen-main-light Identifybutton"
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"


class LightKitchenMainLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.kitchen_main_light"""
        supported_color_modes: list
        color_mode: typing.Any
        off_with_transition: bool
        off_brightness: typing.Any
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'supported_color_modes': ['onoff'], 'color_mode': None, 'off_with_transition': False, 'off_brightness': None, 'friendly_name': 'kitchen-main-light Light', 'supported_features': 8, 'last_changed': '2024-08-02T22:30:28.765772+00:00', 'last_updated': '2024-08-02T22:30:28.765772+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.kitchen_main_light",
        state=state
    )
    entity_id = "light.kitchen_main_light"
    unique_id = "00:12:4b:00:26:b6:fc:1f-1"
    name = "kitchen-main-light Light"
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"


class ButtonDiningMainLight01Identifybutton(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.dining_main_light_01_identifybutton"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'dining-main-light-01 Identifybutton', 'last_changed': '2024-07-27T14:55:29.812517+00:00', 'last_updated': '2024-07-27T14:55:29.812517+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.dining_main_light_01_identifybutton",
        state=state
    )
    entity_id = "button.dining_main_light_01_identifybutton"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-3"
    name = "dining-main-light-01 Identifybutton"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class LightDiningMainLight01(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.dining_main_light_01"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 89, 'friendly_name': 'dining-main-light-01 Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.478958+00:00', 'last_updated': '2024-08-03T10:07:11.478958+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.dining_main_light_01",
        state=state
    )
    entity_id = "light.dining_main_light_01"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1"
    name = "dining-main-light-01 Light"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class BinarySensorDiningMainLight01Opening(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.dining_main_light_01_opening"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'opening', 'friendly_name': 'dining-main-light-01 Opening', 'last_changed': '2024-07-27T14:55:29.764342+00:00', 'last_updated': '2024-07-27T14:55:29.764342+00:00', 'state_value': 'off'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.dining_main_light_01_opening",
        state=state
    )
    entity_id = "binary_sensor.dining_main_light_01_opening"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-6"
    name = "dining-main-light-01 Opening"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class NumberDiningMainLight01StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.dining_main_light_01_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'dining-main-light-01 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.164209+00:00', 'last_updated': '2024-07-27T14:55:30.164209+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.dining_main_light_01_start_up_color_temperature",
        state=state
    )
    entity_id = "number.dining_main_light_01_start_up_color_temperature"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-768-start_up_color_temperature"
    name = "dining-main-light-01 Start-up color temperature"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class NumberDiningMainLight01Startupcurrentlevelconfiguration(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.dining_main_light_01_startupcurrentlevelconfiguration"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'dining-main-light-01 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.159239+00:00', 'last_updated': '2024-07-27T14:55:30.159239+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.dining_main_light_01_startupcurrentlevelconfiguration",
        state=state
    )
    entity_id = "number.dining_main_light_01_startupcurrentlevelconfiguration"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-8-start_up_current_level"
    name = "dining-main-light-01 Startupcurrentlevelconfiguration"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class SelectDiningMainLight01Startuponoffselect(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.dining_main_light_01_startuponoffselect"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'dining-main-light-01 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.498671+00:00', 'last_updated': '2024-07-27T14:55:30.498671+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.dining_main_light_01_startuponoffselect",
        state=state
    )
    entity_id = "select.dining_main_light_01_startuponoffselect"
    unique_id = "a4:c1:38:2e:d0:91:42:c8-1-6-StartUpOnOff"
    name = "dining-main-light-01 Startuponoffselect"
    device_id = "9d81f0e2fef987777e18692b538612ff"


class ButtonDiningMainLight02Identifybutton2(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.dining_main_light_02_identifybutton_2"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'dining-main-light-02 Identifybutton', 'last_changed': '2024-07-27T14:55:29.818377+00:00', 'last_updated': '2024-07-27T14:55:29.818377+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.dining_main_light_02_identifybutton_2",
        state=state
    )
    entity_id = "button.dining_main_light_02_identifybutton_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-3"
    name = "dining-main-light-02 Identifybutton"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class LightDiningMainLight02(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.dining_main_light_02"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 105, 'friendly_name': 'dining-main-light-02 Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.436478+00:00', 'last_updated': '2024-08-03T10:07:11.436478+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.dining_main_light_02",
        state=state
    )
    entity_id = "light.dining_main_light_02"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1"
    name = "dining-main-light-02 Light"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class BinarySensorDiningMainLight02Opening2(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.dining_main_light_02_opening_2"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'opening', 'friendly_name': 'dining-main-light-02 Opening', 'last_changed': '2024-07-27T14:55:29.771952+00:00', 'last_updated': '2024-07-27T14:55:29.771952+00:00', 'state_value': 'off'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.dining_main_light_02_opening_2",
        state=state
    )
    entity_id = "binary_sensor.dining_main_light_02_opening_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-6"
    name = "dining-main-light-02 Opening"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class NumberDiningMainLight02StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.dining_main_light_02_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'dining-main-light-02 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.178146+00:00', 'last_updated': '2024-07-27T14:55:30.178146+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.dining_main_light_02_start_up_color_temperature",
        state=state
    )
    entity_id = "number.dining_main_light_02_start_up_color_temperature"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-768-start_up_color_temperature"
    name = "dining-main-light-02 Start-up color temperature"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class NumberDiningMainLight02Startupcurrentlevelconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.dining_main_light_02_startupcurrentlevelconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'dining-main-light-02 Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.168764+00:00', 'last_updated': '2024-07-27T14:55:30.168764+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.dining_main_light_02_startupcurrentlevelconfiguration_2",
        state=state
    )
    entity_id = "number.dining_main_light_02_startupcurrentlevelconfiguration_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-8-start_up_current_level"
    name = "dining-main-light-02 Startupcurrentlevelconfiguration"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class SelectDiningMainLight02Startuponoffselect2(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.dining_main_light_02_startuponoffselect_2"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'dining-main-light-02 Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.505564+00:00', 'last_updated': '2024-07-27T14:55:30.505564+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.dining_main_light_02_startuponoffselect_2",
        state=state
    )
    entity_id = "select.dining_main_light_02_startuponoffselect_2"
    unique_id = "a4:c1:38:ca:b8:de:51:93-1-6-StartUpOnOff"
    name = "dining-main-light-02 Startuponoffselect"
    device_id = "8d875e28eff5aec83b6791c1ccf12195"


class ButtonOfficeMainLightIdentifybutton2(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_main_light_identifybutton_2"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'office-main-light Identifybutton', 'last_changed': '2024-07-27T14:55:29.870085+00:00', 'last_updated': '2024-07-27T14:55:29.870085+00:00', 'state_value': '2022-11-30T21:52:29.203985+00:00'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_main_light_identifybutton_2",
        state=state
    )
    entity_id = "button.office_main_light_identifybutton_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-3"
    name = "office-main-light Identifybutton"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class LightOfficeMainLightLight2(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.office_main_light_light_2"""
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'supported_color_modes': ['brightness'], 'color_mode': None, 'brightness': None, 'off_with_transition': True, 'off_brightness': 254, 'friendly_name': 'office-main-light Light', 'supported_features': 40, 'last_changed': '2024-08-02T14:47:27.711501+00:00', 'last_updated': '2024-08-02T14:47:27.711501+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.office_main_light_light_2",
        state=state
    )
    entity_id = "light.office_main_light_light_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1"
    name = "office-main-light Light"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class NumberOfficeMainLightOnlevelconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_main_light_onlevelconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-main-light Onlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.386781+00:00', 'last_updated': '2024-07-27T14:55:30.386781+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_main_light_onlevelconfiguration_2",
        state=state
    )
    entity_id = "number.office_main_light_onlevelconfiguration_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-8-on_level"
    name = "office-main-light Onlevelconfiguration"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class NumberOfficeMainLightOnofftransitiontimeconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_main_light_onofftransitiontimeconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-main-light Onofftransitiontimeconfiguration', 'last_changed': '2024-07-27T14:55:30.381373+00:00', 'last_updated': '2024-07-27T14:55:30.381373+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_main_light_onofftransitiontimeconfiguration_2",
        state=state
    )
    entity_id = "number.office_main_light_onofftransitiontimeconfiguration_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-8-on_off_transition_time"
    name = "office-main-light Onofftransitiontimeconfiguration"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class NumberOfficeMainLightStartupcurrentlevelconfiguration2(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_main_light_startupcurrentlevelconfiguration_2"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-main-light Startupcurrentlevelconfiguration', 'last_changed': '2024-07-27T14:55:30.394176+00:00', 'last_updated': '2024-07-27T14:55:30.394176+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_main_light_startupcurrentlevelconfiguration_2",
        state=state
    )
    entity_id = "number.office_main_light_startupcurrentlevelconfiguration_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-8-start_up_current_level"
    name = "office-main-light Startupcurrentlevelconfiguration"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class SelectOfficeMainLightStartuponoffselect2(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.office_main_light_startuponoffselect_2"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'office-main-light Startuponoffselect', 'last_changed': '2024-07-27T14:55:30.558766+00:00', 'last_updated': '2024-07-27T14:55:30.558766+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.office_main_light_startuponoffselect_2",
        state=state
    )
    entity_id = "select.office_main_light_startuponoffselect_2"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-6-StartUpOnOff"
    name = "office-main-light Startuponoffselect"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class SensorIkeaOfSwedenRemoteControlN2Rssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_remote_control_n2_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_remote_control_n2_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_remote_control_n2_rssi"
    unique_id = "00:3c:84:ff:fe:df:f8:31-1-0-rssi"
    name = "None"
    device_id = "a701fbed4393032c83f56e66d56c2a83"


class SensorIkeaOfSwedenRemoteControlN2Lqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_remote_control_n2_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_remote_control_n2_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_remote_control_n2_lqi"
    unique_id = "00:3c:84:ff:fe:df:f8:31-1-0-lqi"
    name = "None"
    device_id = "a701fbed4393032c83f56e66d56c2a83"


class SensorLivingMainControlBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.living_main_control_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'AAA', 'battery_quantity': 2, 'battery_voltage': 3.0, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'living-main-control Battery', 'last_changed': '2024-08-03T10:03:44.644482+00:00', 'last_updated': '2024-08-03T10:03:44.644482+00:00', 'state_value': 100})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.living_main_control_battery",
        state=state
    )
    entity_id = "sensor.living_main_control_battery"
    unique_id = "00:3c:84:ff:fe:df:f8:31-1-1"
    name = "living-main-control Battery"
    device_id = "a701fbed4393032c83f56e66d56c2a83"


class ButtonLivingMainControlIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_main_control_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-main-control Identify', 'last_changed': '2024-08-03T10:03:44.654444+00:00', 'last_updated': '2024-08-03T10:03:44.654444+00:00', 'state_value': '2024-07-31T20:52:13.539541+00:00'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_main_control_identify",
        state=state
    )
    entity_id = "button.living_main_control_identify"
    unique_id = "00:3c:84:ff:fe:df:f8:31-1-3"
    name = "living-main-control Identify"
    device_id = "a701fbed4393032c83f56e66d56c2a83"


class LightLivingGroupMid(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_group_mid"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.living_down_light_02', 'light.living_down_light_05'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'living-group-mid', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:04.709209+00:00', 'last_updated': '2024-08-03T10:07:04.709209+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_group_mid",
        state=state
    )
    entity_id = "light.living_group_mid"
    unique_id = "19953a5b9669186fe91d8fbdfe18d919"
    name = "living-group-mid"
    device_id = "None"


class LightLivingGroupExt(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_group_ext"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.living_down_light_06', 'light.living_down_light_08', 'light.living_down_light_09'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'living-group-ext', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:03.868920+00:00', 'last_updated': '2024-08-03T10:07:03.868920+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_group_ext",
        state=state
    )
    entity_id = "light.living_group_ext"
    unique_id = "98016814e0821d203e2a523b40997c79"
    name = "living-group-ext"
    device_id = "None"


class LightLivingGroupInt(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_group_int"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.living_down_light_03'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'living-group-int', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:05.799767+00:00', 'last_updated': '2024-08-03T10:07:05.799767+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_group_int",
        state=state
    )
    entity_id = "light.living_group_int"
    unique_id = "d410ae46b15b54a34e24c841e36b3ed5"
    name = "living-group-int"
    device_id = "None"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi6(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_6"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
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

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_6"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-0-lqi"
    name = "None"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class SensorDiningMainSwitchBattery6(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.dining_main_switch_battery_6"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'dining-main-switch Battery', 'last_changed': '2024-08-02T18:27:54.603976+00:00', 'last_updated': '2024-08-02T18:27:54.603976+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.dining_main_switch_battery_6",
        state=state
    )
    entity_id = "sensor.dining_main_switch_battery_6"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-1"
    name = "dining-main-switch Battery"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class ButtonDiningMainSwitchIdentify4(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.dining_main_switch_identify_4"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'dining-main-switch Identify', 'last_changed': '2024-08-02T18:27:54.602662+00:00', 'last_updated': '2024-08-02T18:27:54.602662+00:00', 'state_value': 'unavailable'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.dining_main_switch_identify_4",
        state=state
    )
    entity_id = "button.dining_main_switch_identify_4"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-3"
    name = "dining-main-switch Identify"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class SensorIkeaOfSwedenTradfribulbgu10ws345lmRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi_2"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-0-rssi"
    name = "None"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class SensorIkeaOfSwedenTradfribulbgu10ws345lmLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi_2"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-0-lqi"
    name = "None"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi7(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_7"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_7",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_7"
    unique_id = "6c:5c:b1:ff:fe:13:39:54-1-0-rssi"
    name = "None"
    device_id = "df2045cfeac2943e4f94fa9a24723277"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi7(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_7"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_7",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_7"
    unique_id = "6c:5c:b1:ff:fe:13:39:54-1-0-lqi"
    name = "None"
    device_id = "df2045cfeac2943e4f94fa9a24723277"


class SwitchWakeOnLan(models.Entity):

    class _StateClass(models.State):
        """State class for entity switch.wake_on_lan"""
        assumed_state: bool
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'assumed_state': True, 'friendly_name': 'Wake on LAN', 'last_changed': '2024-07-25T11:38:45.111589+00:00', 'last_updated': '2024-07-25T11:38:45.111589+00:00', 'state_value': 'off'})
    services = my_domains.Switch(
        instance=my_ha_instance,
        entity_id="switch.wake_on_lan",
        state=state
    )
    entity_id = "switch.wake_on_lan"
    unique_id = "b4:2e:99:e5:48:44"
    name = "Wake on LAN"
    device_id = "None"


class SensorTvGamingButtonBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tv_gaming_button_battery"""
        state_class: str
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_voltage': 3.0, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'tv-gaming-button Battery', 'last_changed': '2024-07-27T14:55:30.760504+00:00', 'last_updated': '2024-07-27T14:55:30.760504+00:00', 'state_value': 100})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tv_gaming_button_battery",
        state=state
    )
    entity_id = "sensor.tv_gaming_button_battery"
    unique_id = "00:12:4b:00:25:20:d2:98-1-1"
    name = "tv-gaming-button Battery"
    device_id = "1fc43fcc44e909a2a6d39ee73f257b9a"


class ButtonTvGamingButtonIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.tv_gaming_button_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'tv-gaming-button Identify', 'last_changed': '2024-07-27T14:55:29.916047+00:00', 'last_updated': '2024-07-27T14:55:29.916047+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.tv_gaming_button_identify",
        state=state
    )
    entity_id = "button.tv_gaming_button_identify"
    unique_id = "00:12:4b:00:25:20:d2:98-1-3"
    name = "tv-gaming-button Identify"
    device_id = "1fc43fcc44e909a2a6d39ee73f257b9a"


class SensorTvGamingButtonLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tv_gaming_button_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tv_gaming_button_lqi",
        state=state
    )
    entity_id = "sensor.tv_gaming_button_lqi"
    unique_id = "00:12:4b:00:25:20:d2:98-1-0-lqi"
    name = "None"
    device_id = "1fc43fcc44e909a2a6d39ee73f257b9a"


class SensorTvGamingButtonRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tv_gaming_button_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tv_gaming_button_rssi",
        state=state
    )
    entity_id = "sensor.tv_gaming_button_rssi"
    unique_id = "00:12:4b:00:25:20:d2:98-1-0-rssi"
    name = "None"
    device_id = "1fc43fcc44e909a2a6d39ee73f257b9a"


class MediaPlayerSamsungQ64ba55Tv2(models.Entity):

    class _StateClass(models.State):
        """State class for entity media_player.samsung_q64ba_55_tv_2"""
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'friendly_name': 'Samsung Q64BA 55 TV', 'supported_features': 0, 'last_changed': '2024-08-02T22:30:26.010934+00:00', 'last_updated': '2024-08-02T22:30:26.010934+00:00', 'state_value': 'unavailable'})
    services = my_domains.MediaPlayer(
        instance=my_ha_instance,
        entity_id="media_player.samsung_q64ba_55_tv_2",
        state=state
    )
    entity_id = "media_player.samsung_q64ba_55_tv_2"
    unique_id = "uuid:b24ea32e-f679-4606-8fba-f466b2426e6b"
    name = "Samsung Q64BA 55 TV"
    device_id = "d9210728a89d2af02be858974aed07fe"


class SensorEwelinkWb01Rssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_wb01_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_wb01_rssi",
        state=state
    )
    entity_id = "sensor.ewelink_wb01_rssi"
    unique_id = "00:12:4b:00:25:20:d2:8a-1-0-rssi"
    name = "None"
    device_id = "ee80cf293d694022cf00e664a062c06f"


class SensorEwelinkWb01Lqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_wb01_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_wb01_lqi",
        state=state
    )
    entity_id = "sensor.ewelink_wb01_lqi"
    unique_id = "00:12:4b:00:25:20:d2:8a-1-0-lqi"
    name = "None"
    device_id = "ee80cf293d694022cf00e664a062c06f"


class SensorIkeaOfSwedenTradfriBulbE14Cws470lmRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_rssi"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-0-rssi"
    name = "None"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class SensorIkeaOfSwedenTradfriBulbE14Cws470lmLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_bulb_e14_cws_470lm_lqi"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-0-lqi"
    name = "None"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi_2"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-0-rssi"
    name = "None"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi_2",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi_2"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-0-lqi"
    name = "None"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class SensorIkeaOfSwedenTradfribulbgu10ws345lmRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbgu10ws345lm_rssi"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-0-rssi"
    name = "None"
    device_id = "4235267e075fb2a70160bdc771810295"


class SensorIkeaOfSwedenTradfribulbgu10ws345lmLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfribulbgu10ws345lm_lqi"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-0-lqi"
    name = "None"
    device_id = "4235267e075fb2a70160bdc771810295"


class SensorIkeaOfSwedenTradfriOnOffSwitchRssi4(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_4"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_4",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_rssi_4"
    unique_id = "bc:02:6e:ff:fe:00:3c:3c-1-0-rssi"
    name = "None"
    device_id = "83f3a2ec56c0e312b046b46446691791"


class SensorIkeaOfSwedenTradfriOnOffSwitchLqi4(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_4"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_4",
        state=state
    )
    entity_id = "sensor.ikea_of_sweden_tradfri_on_off_switch_lqi_4"
    unique_id = "bc:02:6e:ff:fe:00:3c:3c-1-0-lqi"
    name = "None"
    device_id = "83f3a2ec56c0e312b046b46446691791"


class SensorLocalIp(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.local_ip"""
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'icon': 'mdi:ip', 'friendly_name': 'Local IP', 'last_changed': '2024-07-25T11:38:44.096781+00:00', 'last_updated': '2024-07-25T11:38:44.096781+00:00', 'state_value': '192.168.1.20'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.local_ip",
        state=state
    )
    entity_id = "sensor.local_ip"
    unique_id = "address"
    name = "Local IP"
    device_id = "None"


class SensorHacs(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.hacs"""
        repositories: list
        unit_of_measurement: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'repositories': [{'name': 'guerrerotook/securitas-direct-new-api', 'display_name': 'Securitas Direct Alarm', 'installed_version': 'v2.6.0.0', 'available_version': 'v2.7.6.1'}], 'unit_of_measurement': 'pending update(s)', 'icon': 'hacs:hacs', 'friendly_name': 'hacs', 'last_changed': '2024-07-25T11:39:39.708097+00:00', 'last_updated': '2024-07-25T11:39:39.708097+00:00', 'state_value': 1})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.hacs",
        state=state
    )
    entity_id = "sensor.hacs"
    unique_id = "0717a0cd-745c-48fd-9b16-c8534c9704f9-bc944b0f-fd42-4a58-a072-ade38d1444cd"
    name = "hacs"
    device_id = "80cd8633ed3f38ed19b86bf2fa1df6b1"


class SensorTz3210Dksca8p8Ts0505bRssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tz3210_dksca8p8_ts0505b_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tz3210_dksca8p8_ts0505b_rssi",
        state=state
    )
    entity_id = "sensor.tz3210_dksca8p8_ts0505b_rssi"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1-0-rssi"
    name = "None"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class SensorTz3210Dksca8p8Ts0505bLqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tz3210_dksca8p8_ts0505b_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tz3210_dksca8p8_ts0505b_lqi",
        state=state
    )
    entity_id = "sensor.tz3210_dksca8p8_ts0505b_lqi"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1-0-lqi"
    name = "None"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class LightGaleryLight1(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.galery_light_1"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2000, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 500, 'supported_color_modes': ['color_temp', 'xy'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 254, 'friendly_name': 'galery-light-1 Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.605993+00:00', 'last_updated': '2024-08-03T10:07:11.605993+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.galery_light_1",
        state=state
    )
    entity_id = "light.galery_light_1"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1"
    name = "galery-light-1 Light"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class SensorTz3210Dksca8p8Ts0505bRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tz3210_dksca8p8_ts0505b_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tz3210_dksca8p8_ts0505b_rssi_2",
        state=state
    )
    entity_id = "sensor.tz3210_dksca8p8_ts0505b_rssi_2"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1-0-rssi"
    name = "None"
    device_id = "773311fd39675f914631c4de4261699b"


class SensorTz3210Dksca8p8Ts0505bLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tz3210_dksca8p8_ts0505b_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tz3210_dksca8p8_ts0505b_lqi_2",
        state=state
    )
    entity_id = "sensor.tz3210_dksca8p8_ts0505b_lqi_2"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1-0-lqi"
    name = "None"
    device_id = "773311fd39675f914631c4de4261699b"


class LightGaleryLight2(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.galery_light_2"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2000, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 500, 'supported_color_modes': ['color_temp', 'xy'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 254, 'friendly_name': 'galery-light-2 Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.550312+00:00', 'last_updated': '2024-08-03T10:07:11.550312+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.galery_light_2",
        state=state
    )
    entity_id = "light.galery_light_2"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1"
    name = "galery-light-2 Light"
    device_id = "773311fd39675f914631c4de4261699b"


class SensorHomeAssistantCoreCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_core_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_core_cpu_percent",
        state=state
    )
    entity_id = "sensor.home_assistant_core_cpu_percent"
    unique_id = "home_assistant_core_cpu_percent"
    name = "None"
    device_id = "bac32c0a9033740e54fe621b88d7220b"


class SensorHomeAssistantCoreMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_core_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_core_memory_percent",
        state=state
    )
    entity_id = "sensor.home_assistant_core_memory_percent"
    unique_id = "home_assistant_core_memory_percent"
    name = "None"
    device_id = "bac32c0a9033740e54fe621b88d7220b"


class SensorHomeAssistantSupervisorCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_supervisor_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_supervisor_cpu_percent",
        state=state
    )
    entity_id = "sensor.home_assistant_supervisor_cpu_percent"
    unique_id = "home_assistant_supervisor_cpu_percent"
    name = "None"
    device_id = "d01ab98c93f7e94e7a0f1c31100cc8d6"


class SensorHomeAssistantSupervisorMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_supervisor_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_supervisor_memory_percent",
        state=state
    )
    entity_id = "sensor.home_assistant_supervisor_memory_percent"
    unique_id = "home_assistant_supervisor_memory_percent"
    name = "None"
    device_id = "d01ab98c93f7e94e7a0f1c31100cc8d6"


class SensorHomeAssistantHostOsAgentVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_host_os_agent_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_host_os_agent_version",
        state=state
    )
    entity_id = "sensor.home_assistant_host_os_agent_version"
    unique_id = "home_assistant_host_agent_version"
    name = "None"
    device_id = "ab3e5233df6ae2e3386598f445678b02"


class SensorHomeAssistantHostApparmorVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_host_apparmor_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_host_apparmor_version",
        state=state
    )
    entity_id = "sensor.home_assistant_host_apparmor_version"
    unique_id = "home_assistant_host_apparmor_version"
    name = "None"
    device_id = "ab3e5233df6ae2e3386598f445678b02"


class SensorHomeAssistantHostDiskTotal(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_host_disk_total"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_host_disk_total",
        state=state
    )
    entity_id = "sensor.home_assistant_host_disk_total"
    unique_id = "home_assistant_host_disk_total"
    name = "None"
    device_id = "ab3e5233df6ae2e3386598f445678b02"


class SensorHomeAssistantHostDiskUsed(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_host_disk_used"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_host_disk_used",
        state=state
    )
    entity_id = "sensor.home_assistant_host_disk_used"
    unique_id = "home_assistant_host_disk_used"
    name = "None"
    device_id = "ab3e5233df6ae2e3386598f445678b02"


class SensorHomeAssistantHostDiskFree(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.home_assistant_host_disk_free"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.home_assistant_host_disk_free",
        state=state
    )
    entity_id = "sensor.home_assistant_host_disk_free"
    unique_id = "home_assistant_host_disk_free"
    name = "None"
    device_id = "ab3e5233df6ae2e3386598f445678b02"


class SensorSunNextDawn(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_dawn"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next dawn', 'last_changed': '2024-08-03T04:14:40.475705+00:00', 'last_updated': '2024-08-03T04:14:40.475705+00:00', 'state_value': '2024-08-04T04:15:46+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_dawn",
        state=state
    )
    entity_id = "sensor.sun_next_dawn"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_dawn"
    name = "Sun Next dawn"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunNextDusk(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_dusk"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next dusk', 'last_changed': '2024-08-02T19:40:54.985543+00:00', 'last_updated': '2024-08-02T19:40:54.985543+00:00', 'state_value': '2024-08-03T19:39:38+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_dusk",
        state=state
    )
    entity_id = "sensor.sun_next_dusk"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_dusk"
    name = "Sun Next dusk"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunNextMidnight(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_midnight"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next midnight', 'last_changed': '2024-08-02T23:57:33.016615+00:00', 'last_updated': '2024-08-02T23:57:33.016615+00:00', 'state_value': '2024-08-03T23:57:27+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_midnight",
        state=state
    )
    entity_id = "sensor.sun_next_midnight"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_midnight"
    name = "Sun Next midnight"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunNextNoon(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_noon"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next noon', 'last_changed': '2024-08-02T11:57:39.016629+00:00', 'last_updated': '2024-08-02T11:57:39.016629+00:00', 'state_value': '2024-08-03T11:57:34+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_noon",
        state=state
    )
    entity_id = "sensor.sun_next_noon"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_noon"
    name = "Sun Next noon"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunNextRising(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_rising"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next rising', 'last_changed': '2024-08-03T04:46:37.358219+00:00', 'last_updated': '2024-08-03T04:46:37.358219+00:00', 'state_value': '2024-08-04T04:47:37+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_rising",
        state=state
    )
    entity_id = "sensor.sun_next_rising"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_rising"
    name = "Sun Next rising"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunNextSetting(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_next_setting"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'timestamp', 'friendly_name': 'Sun Next setting', 'last_changed': '2024-08-02T19:08:59.076655+00:00', 'last_updated': '2024-08-02T19:08:59.076655+00:00', 'state_value': '2024-08-03T19:07:48+00:00'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_next_setting",
        state=state
    )
    entity_id = "sensor.sun_next_setting"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-next_setting"
    name = "Sun Next setting"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunSolarElevation(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_solar_elevation"""
        state_class: str
        unit_of_measurement: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '°', 'friendly_name': 'Sun Solar elevation', 'last_changed': '2024-08-03T10:39:02.129027+00:00', 'last_updated': '2024-08-03T10:39:02.129027+00:00', 'state_value': 60.6})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_solar_elevation",
        state=state
    )
    entity_id = "sensor.sun_solar_elevation"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-solar_elevation"
    name = "Sun Solar elevation"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunSolarAzimuth(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_solar_azimuth"""
        state_class: str
        unit_of_measurement: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '°', 'friendly_name': 'Sun Solar azimuth', 'last_changed': '2024-08-03T10:39:02.130310+00:00', 'last_updated': '2024-08-03T10:39:02.130310+00:00', 'state_value': 139.22})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_solar_azimuth",
        state=state
    )
    entity_id = "sensor.sun_solar_azimuth"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-solar_azimuth"
    name = "Sun Solar azimuth"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class SensorSunSolarRising(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sun_solar_rising"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sun_solar_rising",
        state=state
    )
    entity_id = "sensor.sun_solar_rising"
    unique_id = "ba152e0da1c8679742d0b19b49a4ca7f-solar_rising"
    name = "None"
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"


class RemoteSamsungQ64ba55Tv(models.Entity):

    class _StateClass(models.State):
        """State class for entity remote.samsung_q64ba_55_tv"""
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'friendly_name': 'Samsung Q64BA 55 TV', 'supported_features': 0, 'last_changed': '2024-07-25T11:39:10.147468+00:00', 'last_updated': '2024-07-25T11:39:10.147468+00:00', 'state_value': 'unknown'})
    services = my_domains.Remote(
        instance=my_ha_instance,
        entity_id="remote.samsung_q64ba_55_tv",
        state=state
    )
    entity_id = "remote.samsung_q64ba_55_tv"
    unique_id = "f9b4c92f-9810-4e85-b012-8aaf8083263c"
    name = "Samsung Q64BA 55 TV"
    device_id = "f3604fa009d16354ba1e2abbb963f8cd"


class SensorEwelinkTh01Rssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_th01_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_th01_rssi",
        state=state
    )
    entity_id = "sensor.ewelink_th01_rssi"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-0-rssi"
    name = "None"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class SensorEwelinkTh01Lqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_th01_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_th01_lqi",
        state=state
    )
    entity_id = "sensor.ewelink_th01_lqi"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-0-lqi"
    name = "None"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class SensorOfficeTemperature01Battery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.office_temperature_01_battery"""
        state_class: str
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_voltage': 3.0, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'office-temperature-01 Battery', 'last_changed': '2024-07-27T14:55:30.813306+00:00', 'last_updated': '2024-07-27T14:55:30.813306+00:00', 'state_value': 100})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.office_temperature_01_battery",
        state=state
    )
    entity_id = "sensor.office_temperature_01_battery"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-1"
    name = "office-temperature-01 Battery"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class SensorOfficeTemperature01Humidity(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.office_temperature_01_humidity"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'humidity', 'friendly_name': 'office-temperature-01 Humidity', 'last_changed': '2024-08-03T10:32:53.723571+00:00', 'last_updated': '2024-08-03T10:32:53.723571+00:00', 'state_value': 44.3})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.office_temperature_01_humidity",
        state=state
    )
    entity_id = "sensor.office_temperature_01_humidity"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-1029"
    name = "office-temperature-01 Humidity"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class ButtonOfficeTemperature01Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_temperature_01_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'office-temperature-01 Identify', 'last_changed': '2024-07-27T14:55:29.955702+00:00', 'last_updated': '2024-07-27T14:55:29.955702+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_temperature_01_identify",
        state=state
    )
    entity_id = "button.office_temperature_01_identify"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-3"
    name = "office-temperature-01 Identify"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class SensorOfficeTemperature01Temperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.office_temperature_01_temperature"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '°C', 'device_class': 'temperature', 'friendly_name': 'office-temperature-01 Temperature', 'last_changed': '2024-08-03T10:08:59.504539+00:00', 'last_updated': '2024-08-03T10:08:59.504539+00:00', 'state_value': 27.2})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.office_temperature_01_temperature",
        state=state
    )
    entity_id = "sensor.office_temperature_01_temperature"
    unique_id = "00:12:4b:00:29:2f:bd:cf-1-1026"
    name = "office-temperature-01 Temperature"
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"


class SensorEwelinkTh01Rssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_th01_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_th01_rssi_2",
        state=state
    )
    entity_id = "sensor.ewelink_th01_rssi_2"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-0-rssi"
    name = "None"
    device_id = "6284013aec649bd4b35a3e5405239898"


class SensorEwelinkTh01Lqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.ewelink_th01_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.ewelink_th01_lqi_2",
        state=state
    )
    entity_id = "sensor.ewelink_th01_lqi_2"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-0-lqi"
    name = "None"
    device_id = "6284013aec649bd4b35a3e5405239898"


class SensorLivingTemperature01Battery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.living_temperature_01_battery"""
        state_class: str
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_voltage': 3.0, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'living-temperature-01 Battery', 'last_changed': '2024-07-27T14:55:30.834228+00:00', 'last_updated': '2024-07-27T14:55:30.834228+00:00', 'state_value': 100})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.living_temperature_01_battery",
        state=state
    )
    entity_id = "sensor.living_temperature_01_battery"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-1"
    name = "living-temperature-01 Battery"
    device_id = "6284013aec649bd4b35a3e5405239898"


class SensorLivingTemperature01Humidity(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.living_temperature_01_humidity"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'humidity', 'friendly_name': 'living-temperature-01 Humidity', 'last_changed': '2024-08-03T10:34:10.079301+00:00', 'last_updated': '2024-08-03T10:34:10.079301+00:00', 'state_value': 47.2})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.living_temperature_01_humidity",
        state=state
    )
    entity_id = "sensor.living_temperature_01_humidity"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-1029"
    name = "living-temperature-01 Humidity"
    device_id = "6284013aec649bd4b35a3e5405239898"


class ButtonLivingTemperature01Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_temperature_01_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-temperature-01 Identify', 'last_changed': '2024-07-27T14:55:29.962192+00:00', 'last_updated': '2024-07-27T14:55:29.962192+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_temperature_01_identify",
        state=state
    )
    entity_id = "button.living_temperature_01_identify"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-3"
    name = "living-temperature-01 Identify"
    device_id = "6284013aec649bd4b35a3e5405239898"


class SensorLivingTemperature01Temperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.living_temperature_01_temperature"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '°C', 'device_class': 'temperature', 'friendly_name': 'living-temperature-01 Temperature', 'last_changed': '2024-08-03T09:01:17.034414+00:00', 'last_updated': '2024-08-03T09:01:17.034414+00:00', 'state_value': 27.5})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.living_temperature_01_temperature",
        state=state
    )
    entity_id = "sensor.living_temperature_01_temperature"
    unique_id = "00:12:4b:00:2a:4e:83:79-1-1026"
    name = "living-temperature-01 Temperature"
    device_id = "6284013aec649bd4b35a3e5405239898"


class SensorTemperaturePl0Salon(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.temperature_pl_0_salon"""
        restored: bool
        device_class: str
        friendly_name: str
        supported_features: int
        unit_of_measurement: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'device_class': 'temperature', 'friendly_name': 'Centro Salón', 'supported_features': 0, 'unit_of_measurement': '°C', 'last_changed': '2024-07-25T11:39:37.435235+00:00', 'last_updated': '2024-07-25T11:39:37.435235+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.temperature_pl_0_salon",
        state=state
    )
    entity_id = "sensor.temperature_pl_0_salon"
    unique_id = "Pl_0_Salon_temperature_7"
    name = "Centro Salón"
    device_id = "ec3e3827a6a81d3071786de7cb8ca680"


class SensorHumidityPl0Salon(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.humidity_pl_0_salon"""
        restored: bool
        device_class: str
        friendly_name: str
        supported_features: int
        unit_of_measurement: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'device_class': 'humidity', 'friendly_name': 'Humidity Pl_0_salon', 'supported_features': 0, 'unit_of_measurement': '%', 'last_changed': '2024-07-25T11:39:37.435627+00:00', 'last_updated': '2024-07-25T11:39:37.435627+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.humidity_pl_0_salon",
        state=state
    )
    entity_id = "sensor.humidity_pl_0_salon"
    unique_id = "Pl_0_Salon_humidity_7"
    name = "Humidity Pl_0_salon"
    device_id = "4f013eba2fcfd4795f85f9b0130abeb9"


class SensorAirQualityPl0Salon(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.air_quality_pl_0_salon"""
        restored: bool
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'friendly_name': 'Air Quality Pl_0_salon', 'supported_features': 0, 'last_changed': '2024-07-25T11:39:37.435976+00:00', 'last_updated': '2024-07-25T11:39:37.435976+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.air_quality_pl_0_salon",
        state=state
    )
    entity_id = "sensor.air_quality_pl_0_salon"
    unique_id = "Pl_0_Salonairquality_7"
    name = "Air Quality Pl_0_salon"
    device_id = "2100636d63fed89f2b2b054d952461bf"


class AlarmControlPanelAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity alarm_control_panel.alarm"""
        code_format: str
        changed_by: typing.Any
        code_arm_required: bool
        message: str
        response_data: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'code_format': 'number', 'changed_by': None, 'code_arm_required': False, 'message': 'alarm-manager.inactive_alarm', 'response_data': '2024-08-03T10:31:32Z', 'friendly_name': 'alarm', 'supported_features': 23, 'last_changed': '2024-07-25T11:38:55.149452+00:00', 'last_updated': '2024-08-03T10:31:32.815257+00:00', 'state_value': 'disarmed'})
    services = my_domains.AlarmControlPanel(
        instance=my_ha_instance,
        entity_id="alarm_control_panel.alarm",
        state=state
    )
    entity_id = "alarm_control_panel.alarm"
    unique_id = "securitas_direct.5267533"
    name = "alarm"
    device_id = "b09d2f2d32403ec4d251307f236106f2"


class DeviceTrackerJoniS23(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.joni_s23"""
        source_type: str
        latitude: float
        longitude: float
        gps_accuracy: int
        altitude: int
        course: int
        speed: int
        vertical_accuracy: int
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'gps', 'latitude': 41.4205064, 'longitude': 2.1577951, 'gps_accuracy': 100, 'altitude': 208, 'course': 0, 'speed': 0, 'vertical_accuracy': 100, 'friendly_name': 's23-joni', 'last_changed': '2024-08-03T10:26:01.502343+00:00', 'last_updated': '2024-08-03T10:26:01.502343+00:00', 'state_value': 'home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.joni_s23",
        state=state
    )
    entity_id = "device_tracker.joni_s23"
    unique_id = "39c4820c78d42c07"
    name = "s23-joni"
    device_id = "86116456e47329aee683359d5dde4d65"


class ButtonOfficeDownlightJoniIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_downlight_joni_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'button-office-downlight-joni-identify', 'last_changed': '2024-07-27T14:55:29.925653+00:00', 'last_updated': '2024-07-27T14:55:29.925653+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_downlight_joni_identify",
        state=state
    )
    entity_id = "button.office_downlight_joni_identify"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-3"
    name = "button-office-downlight-joni-identify"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class LightOfficeDownlightJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.office_downlight_joni"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 135, 'friendly_name': 'office-downlight-joni Light', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:10.669003+00:00', 'last_updated': '2024-08-03T10:07:10.669003+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.office_downlight_joni",
        state=state
    )
    entity_id = "light.office_downlight_joni"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1"
    name = "office-downlight-joni Light"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class NumberOfficeDownlightJoniOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_downlight_joni_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-downlight-joni On level', 'last_changed': '2024-07-27T14:55:30.418427+00:00', 'last_updated': '2024-07-27T14:55:30.418427+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_downlight_joni_on_level",
        state=state
    )
    entity_id = "number.office_downlight_joni_on_level"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-8-on_level"
    name = "office-downlight-joni On level"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class SelectOfficeDownlightJoniStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.office_downlight_joni_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'office-downlight-joni Start-up behavior', 'last_changed': '2024-07-27T14:55:30.566191+00:00', 'last_updated': '2024-07-27T14:55:30.566191+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.office_downlight_joni_start_up_behavior",
        state=state
    )
    entity_id = "select.office_downlight_joni_start_up_behavior"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-6-StartUpOnOff"
    name = "office-downlight-joni Start-up behavior"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class NumberOfficeDownlightJoniStartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_downlight_joni_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 250, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-downlight-joni Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.431893+00:00', 'last_updated': '2024-07-27T14:55:30.431893+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_downlight_joni_start_up_color_temperature",
        state=state
    )
    entity_id = "number.office_downlight_joni_start_up_color_temperature"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-768-start_up_color_temperature"
    name = "office-downlight-joni Start-up color temperature"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class NumberOfficeDownlightJoniStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.office_downlight_joni_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'office-downlight-joni Start-up current level', 'last_changed': '2024-07-27T14:55:30.423376+00:00', 'last_updated': '2024-07-27T14:55:30.423376+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.office_downlight_joni_start_up_current_level",
        state=state
    )
    entity_id = "number.office_downlight_joni_start_up_current_level"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-8-start_up_current_level"
    name = "office-downlight-joni Start-up current level"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class SensorOfficeMainSwitch01Battery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.office_main_switch_01_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.5, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'office-main-switch-01 Battery', 'last_changed': '2024-08-03T08:17:09.632715+00:00', 'last_updated': '2024-08-03T08:17:09.632715+00:00', 'state_value': 11})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.office_main_switch_01_battery",
        state=state
    )
    entity_id = "sensor.office_main_switch_01_battery"
    unique_id = "bc:02:6e:ff:fe:00:3c:36-1-1"
    name = "office-main-switch-01 Battery"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"


class ButtonOfficeMainSwitch01Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_main_switch_01_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'office-main-switch-01 Identify', 'last_changed': '2024-08-03T08:17:09.639399+00:00', 'last_updated': '2024-08-03T08:17:09.639399+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_main_switch_01_identify",
        state=state
    )
    entity_id = "button.office_main_switch_01_identify"
    unique_id = "bc:02:6e:ff:fe:00:3c:36-1-3"
    name = "office-main-switch-01 Identify"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"


class ButtonBedLeftLightIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.bed_left_light_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-left-light Identify', 'last_changed': '2024-07-27T14:55:29.935322+00:00', 'last_updated': '2024-07-27T14:55:29.935322+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_left_light_identify",
        state=state
    )
    entity_id = "button.bed_left_light_identify"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-3"
    name = "bed-left-light Identify"
    device_id = "4235267e075fb2a70160bdc771810295"


class LightBedLeftLightLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.bed_left_light_light"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 89, 'friendly_name': 'bed-left-light Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:10.576014+00:00', 'last_updated': '2024-08-03T10:07:10.576014+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.bed_left_light_light",
        state=state
    )
    entity_id = "light.bed_left_light_light"
    unique_id = "90:35:ea:ff:fe:00:96:29-1"
    name = "bed-left-light Light"
    device_id = "4235267e075fb2a70160bdc771810295"


class NumberBedLeftLightOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_left_light_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-left-light On level', 'last_changed': '2024-07-27T14:55:30.462767+00:00', 'last_updated': '2024-07-27T14:55:30.462767+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_left_light_on_level",
        state=state
    )
    entity_id = "number.bed_left_light_on_level"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-8-on_level"
    name = "bed-left-light On level"
    device_id = "4235267e075fb2a70160bdc771810295"


class NumberBedLeftLightOnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_left_light_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-left-light On/Off transition time', 'last_changed': '2024-07-27T14:55:30.458818+00:00', 'last_updated': '2024-07-27T14:55:30.458818+00:00', 'state_value': 5})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_left_light_on_off_transition_time",
        state=state
    )
    entity_id = "number.bed_left_light_on_off_transition_time"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-8-on_off_transition_time"
    name = "bed-left-light On/Off transition time"
    device_id = "4235267e075fb2a70160bdc771810295"


class SelectBedLeftLightStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.bed_left_light_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'bed-left-light Start-up behavior', 'last_changed': '2024-07-27T14:55:30.576996+00:00', 'last_updated': '2024-07-27T14:55:30.576996+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.bed_left_light_start_up_behavior",
        state=state
    )
    entity_id = "select.bed_left_light_start_up_behavior"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-6-StartUpOnOff"
    name = "bed-left-light Start-up behavior"
    device_id = "4235267e075fb2a70160bdc771810295"


class NumberBedLeftLightStartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_left_light_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 250, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-left-light Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.473383+00:00', 'last_updated': '2024-07-27T14:55:30.473383+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_left_light_start_up_color_temperature",
        state=state
    )
    entity_id = "number.bed_left_light_start_up_color_temperature"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-768-start_up_color_temperature"
    name = "bed-left-light Start-up color temperature"
    device_id = "4235267e075fb2a70160bdc771810295"


class NumberBedLeftLightStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_left_light_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-left-light Start-up current level', 'last_changed': '2024-07-27T14:55:30.469628+00:00', 'last_updated': '2024-07-27T14:55:30.469628+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_left_light_start_up_current_level",
        state=state
    )
    entity_id = "number.bed_left_light_start_up_current_level"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-8-start_up_current_level"
    name = "bed-left-light Start-up current level"
    device_id = "4235267e075fb2a70160bdc771810295"


class ButtonBedMainLightIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.bed_main_light_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-main-light Identify', 'last_changed': '2024-07-27T14:55:29.866271+00:00', 'last_updated': '2024-07-27T14:55:29.866271+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_main_light_identify",
        state=state
    )
    entity_id = "button.bed_main_light_identify"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-3"
    name = "bed-main-light Identify"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class LightBedMainLightLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.bed_main_light_light"""
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'supported_color_modes': ['brightness'], 'color_mode': None, 'brightness': None, 'off_with_transition': False, 'off_brightness': 254, 'friendly_name': 'bed-main-light Light', 'supported_features': 40, 'last_changed': '2024-08-02T18:45:14.512148+00:00', 'last_updated': '2024-08-02T18:45:14.512148+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.bed_main_light_light",
        state=state
    )
    entity_id = "light.bed_main_light_light"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1"
    name = "bed-main-light Light"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class NumberBedMainLightOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_main_light_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-main-light On level', 'last_changed': '2024-07-27T14:55:30.370365+00:00', 'last_updated': '2024-07-27T14:55:30.370365+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_main_light_on_level",
        state=state
    )
    entity_id = "number.bed_main_light_on_level"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-8-on_level"
    name = "bed-main-light On level"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class NumberBedMainLightOnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_main_light_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-main-light On/Off transition time', 'last_changed': '2024-07-27T14:55:30.366239+00:00', 'last_updated': '2024-07-27T14:55:30.366239+00:00', 'state_value': 1})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_main_light_on_off_transition_time",
        state=state
    )
    entity_id = "number.bed_main_light_on_off_transition_time"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-8-on_off_transition_time"
    name = "bed-main-light On/Off transition time"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class SelectBedMainLightStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.bed_main_light_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'bed-main-light Start-up behavior', 'last_changed': '2024-07-27T14:55:30.554616+00:00', 'last_updated': '2024-07-27T14:55:30.554616+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.bed_main_light_start_up_behavior",
        state=state
    )
    entity_id = "select.bed_main_light_start_up_behavior"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-6-StartUpOnOff"
    name = "bed-main-light Start-up behavior"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class NumberBedMainLightStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_main_light_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-main-light Start-up current level', 'last_changed': '2024-07-27T14:55:30.376894+00:00', 'last_updated': '2024-07-27T14:55:30.376894+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_main_light_start_up_current_level",
        state=state
    )
    entity_id = "number.bed_main_light_start_up_current_level"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-8-start_up_current_level"
    name = "bed-main-light Start-up current level"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class SensorBedMainSwitch01Battery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.bed_main_switch_01_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.2, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'bed-main-switch-01 Battery', 'last_changed': '2024-08-03T09:13:42.634395+00:00', 'last_updated': '2024-08-03T09:13:42.634395+00:00', 'state_value': 0})
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

    class _StateClass(models.State):
        """State class for entity button.bed_main_switch_01_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-main-switch-01 Identify', 'last_changed': '2024-08-03T09:13:42.646860+00:00', 'last_updated': '2024-08-03T09:13:42.646860+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_main_switch_01_identify",
        state=state
    )
    entity_id = "button.bed_main_switch_01_identify"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-3"
    name = "bed-main-switch-01 Identify"
    device_id = "f61b9317af000c4b650b5d686343895e"


class ButtonBedRightLightIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.bed_right_light_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-right-light Identify', 'last_changed': '2024-07-27T14:55:29.906227+00:00', 'last_updated': '2024-07-27T14:55:29.906227+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_right_light_identify",
        state=state
    )
    entity_id = "button.bed_right_light_identify"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-3"
    name = "bed-right-light Identify"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class LightBedRightLightLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.bed_right_light_light"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 89, 'friendly_name': 'bed-right-light Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:10.519790+00:00', 'last_updated': '2024-08-03T10:07:10.519790+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.bed_right_light_light",
        state=state
    )
    entity_id = "light.bed_right_light_light"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1"
    name = "bed-right-light Light"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class NumberBedRightLightOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_right_light_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-right-light On level', 'last_changed': '2024-07-27T14:55:30.403069+00:00', 'last_updated': '2024-07-27T14:55:30.403069+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_right_light_on_level",
        state=state
    )
    entity_id = "number.bed_right_light_on_level"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-8-on_level"
    name = "bed-right-light On level"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class NumberBedRightLightOnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_right_light_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-right-light On/Off transition time', 'last_changed': '2024-07-27T14:55:30.398005+00:00', 'last_updated': '2024-07-27T14:55:30.398005+00:00', 'state_value': 5})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_right_light_on_off_transition_time",
        state=state
    )
    entity_id = "number.bed_right_light_on_off_transition_time"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-8-on_off_transition_time"
    name = "bed-right-light On/Off transition time"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class SelectBedRightLightStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.bed_right_light_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'bed-right-light Start-up behavior', 'last_changed': '2024-07-27T14:55:30.562554+00:00', 'last_updated': '2024-07-27T14:55:30.562554+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.bed_right_light_start_up_behavior",
        state=state
    )
    entity_id = "select.bed_right_light_start_up_behavior"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-6-StartUpOnOff"
    name = "bed-right-light Start-up behavior"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class NumberBedRightLightStartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_right_light_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 250, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-right-light Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.411801+00:00', 'last_updated': '2024-07-27T14:55:30.411801+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_right_light_start_up_color_temperature",
        state=state
    )
    entity_id = "number.bed_right_light_start_up_color_temperature"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-768-start_up_color_temperature"
    name = "bed-right-light Start-up color temperature"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class NumberBedRightLightStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.bed_right_light_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'bed-right-light Start-up current level', 'last_changed': '2024-07-27T14:55:30.407397+00:00', 'last_updated': '2024-07-27T14:55:30.407397+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.bed_right_light_start_up_current_level",
        state=state
    )
    entity_id = "number.bed_right_light_start_up_current_level"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-8-start_up_current_level"
    name = "bed-right-light Start-up current level"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class SensorBedRightSwitchBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.bed_right_switch_battery"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'bed-right-switch Battery', 'last_changed': '2024-08-03T04:05:39.874691+00:00', 'last_updated': '2024-08-03T04:05:39.874691+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.bed_right_switch_battery",
        state=state
    )
    entity_id = "sensor.bed_right_switch_battery"
    unique_id = "6c:5c:b1:ff:fe:13:39:54-1-1"
    name = "bed-right-switch Battery"
    device_id = "df2045cfeac2943e4f94fa9a24723277"


class ButtonBedRightSwitchIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.bed_right_switch_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-right-switch Identify', 'last_changed': '2024-08-03T04:05:39.874277+00:00', 'last_updated': '2024-08-03T04:05:39.874277+00:00', 'state_value': 'unavailable'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_right_switch_identify",
        state=state
    )
    entity_id = "button.bed_right_switch_identify"
    unique_id = "6c:5c:b1:ff:fe:13:39:54-1-3"
    name = "bed-right-switch Identify"
    device_id = "df2045cfeac2943e4f94fa9a24723277"


class ButtonGaleryFlexoLightIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.galery_flexo_light_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'galery-flexo-light Identify', 'last_changed': '2024-07-27T14:55:29.860450+00:00', 'last_updated': '2024-07-27T14:55:29.860450+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.galery_flexo_light_identify",
        state=state
    )
    entity_id = "button.galery_flexo_light_identify"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-3"
    name = "galery-flexo-light Identify"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class NumberGaleryFlexoLightOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_flexo_light_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-flexo-light On level', 'last_changed': '2024-07-27T14:55:30.349757+00:00', 'last_updated': '2024-07-27T14:55:30.349757+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_flexo_light_on_level",
        state=state
    )
    entity_id = "number.galery_flexo_light_on_level"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-8-on_level"
    name = "galery-flexo-light On level"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class NumberGaleryFlexoLightOnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_flexo_light_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-flexo-light On/Off transition time', 'last_changed': '2024-07-27T14:55:30.345317+00:00', 'last_updated': '2024-07-27T14:55:30.345317+00:00', 'state_value': 5})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_flexo_light_on_off_transition_time",
        state=state
    )
    entity_id = "number.galery_flexo_light_on_off_transition_time"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-8-on_off_transition_time"
    name = "galery-flexo-light On/Off transition time"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class SelectGaleryFlexoLightStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.galery_flexo_light_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'galery-flexo-light Start-up behavior', 'last_changed': '2024-07-27T14:55:30.550767+00:00', 'last_updated': '2024-07-27T14:55:30.550767+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.galery_flexo_light_start_up_behavior",
        state=state
    )
    entity_id = "select.galery_flexo_light_start_up_behavior"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-6-StartUpOnOff"
    name = "galery-flexo-light Start-up behavior"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class NumberGaleryFlexoLightStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_flexo_light_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-flexo-light Start-up current level', 'last_changed': '2024-07-27T14:55:30.354065+00:00', 'last_updated': '2024-07-27T14:55:30.354065+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_flexo_light_start_up_current_level",
        state=state
    )
    entity_id = "number.galery_flexo_light_start_up_current_level"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-8-start_up_current_level"
    name = "galery-flexo-light Start-up current level"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class SensorKitchenMainSwitchBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.kitchen_main_switch_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.9, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'kitchen-main-switch Battery', 'last_changed': '2024-08-03T06:04:55.067791+00:00', 'last_updated': '2024-08-03T06:04:55.067791+00:00', 'state_value': 87})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.kitchen_main_switch_battery",
        state=state
    )
    entity_id = "sensor.kitchen_main_switch_battery"
    unique_id = "bc:02:6e:ff:fe:00:3c:3c-1-1"
    name = "kitchen-main-switch Battery"
    device_id = "83f3a2ec56c0e312b046b46446691791"


class ButtonKitchenMainSwitchIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.kitchen_main_switch_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'kitchen-main-switch Identify', 'last_changed': '2024-08-03T06:04:55.075424+00:00', 'last_updated': '2024-08-03T06:04:55.075424+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.kitchen_main_switch_identify",
        state=state
    )
    entity_id = "button.kitchen_main_switch_identify"
    unique_id = "bc:02:6e:ff:fe:00:3c:3c-1-3"
    name = "kitchen-main-switch Identify"
    device_id = "83f3a2ec56c0e312b046b46446691791"


class ButtonLivingAmbientSofaIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_ambient_sofa_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-ambient-sofa Identify', 'last_changed': '2024-07-27T14:55:29.931441+00:00', 'last_updated': '2024-07-27T14:55:29.931441+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_ambient_sofa_identify",
        state=state
    )
    entity_id = "button.living_ambient_sofa_identify"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-3"
    name = "living-ambient-sofa Identify"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class LightLivingAmbientSofaLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_ambient_sofa_light"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 148, 'friendly_name': 'living-ambient-sofa Light', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:08.339844+00:00', 'last_updated': '2024-08-03T10:07:08.339844+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_ambient_sofa_light",
        state=state
    )
    entity_id = "light.living_ambient_sofa_light"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1"
    name = "living-ambient-sofa Light"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class NumberLivingAmbientSofaOnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_ambient_sofa_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-ambient-sofa On level', 'last_changed': '2024-07-27T14:55:30.442780+00:00', 'last_updated': '2024-07-27T14:55:30.442780+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_ambient_sofa_on_level",
        state=state
    )
    entity_id = "number.living_ambient_sofa_on_level"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-8-on_level"
    name = "living-ambient-sofa On level"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class NumberLivingAmbientSofaOnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_ambient_sofa_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-ambient-sofa On/Off transition time', 'last_changed': '2024-07-27T14:55:30.438105+00:00', 'last_updated': '2024-07-27T14:55:30.438105+00:00', 'state_value': 5})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_ambient_sofa_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_ambient_sofa_on_off_transition_time"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-8-on_off_transition_time"
    name = "living-ambient-sofa On/Off transition time"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class SelectLivingAmbientSofaStartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_ambient_sofa_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-ambient-sofa Start-up behavior', 'last_changed': '2024-07-27T14:55:30.570822+00:00', 'last_updated': '2024-07-27T14:55:30.570822+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_ambient_sofa_start_up_behavior",
        state=state
    )
    entity_id = "select.living_ambient_sofa_start_up_behavior"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-6-StartUpOnOff"
    name = "living-ambient-sofa Start-up behavior"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class NumberLivingAmbientSofaStartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_ambient_sofa_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 250, 'max': 454, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-ambient-sofa Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.453612+00:00', 'last_updated': '2024-07-27T14:55:30.453612+00:00', 'state_value': 65535})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_ambient_sofa_start_up_color_temperature",
        state=state
    )
    entity_id = "number.living_ambient_sofa_start_up_color_temperature"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-768-start_up_color_temperature"
    name = "living-ambient-sofa Start-up color temperature"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class NumberLivingAmbientSofaStartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_ambient_sofa_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-ambient-sofa Start-up current level', 'last_changed': '2024-07-27T14:55:30.447138+00:00', 'last_updated': '2024-07-27T14:55:30.447138+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_ambient_sofa_start_up_current_level",
        state=state
    )
    entity_id = "number.living_ambient_sofa_start_up_current_level"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-8-start_up_current_level"
    name = "living-ambient-sofa Start-up current level"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class ButtonGaleryLight1Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.galery_light_1_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'galery-light-1 Identify', 'last_changed': '2024-07-27T14:55:29.944983+00:00', 'last_updated': '2024-07-27T14:55:29.944983+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.galery_light_1_identify",
        state=state
    )
    entity_id = "button.galery_light_1_identify"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1-3"
    name = "galery-light-1 Identify"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class NumberGaleryLight1StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_light_1_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 500, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-light-1 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.478330+00:00', 'last_updated': '2024-07-27T14:55:30.478330+00:00', 'state_value': 153})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_light_1_start_up_color_temperature",
        state=state
    )
    entity_id = "number.galery_light_1_start_up_color_temperature"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1-768-start_up_color_temperature"
    name = "galery-light-1 Start-up color temperature"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class ButtonGaleryLight2Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.galery_light_2_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'galery-light-2 Identify', 'last_changed': '2024-07-27T14:55:29.951973+00:00', 'last_updated': '2024-07-27T14:55:29.951973+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.galery_light_2_identify",
        state=state
    )
    entity_id = "button.galery_light_2_identify"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1-3"
    name = "galery-light-2 Identify"
    device_id = "773311fd39675f914631c4de4261699b"


class NumberGaleryLight2StartUpColorTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.galery_light_2_start_up_color_temperature"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 153, 'max': 500, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'galery-light-2 Start-up color temperature', 'last_changed': '2024-07-27T14:55:30.485191+00:00', 'last_updated': '2024-07-27T14:55:30.485191+00:00', 'state_value': 153})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.galery_light_2_start_up_color_temperature",
        state=state
    )
    entity_id = "number.galery_light_2_start_up_color_temperature"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1-768-start_up_color_temperature"
    name = "galery-light-2 Start-up color temperature"
    device_id = "773311fd39675f914631c4de4261699b"


class SensorJoniDeskButtonBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.joni_desk_button_battery"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'joni-desk-button Battery', 'last_changed': '2024-07-26T17:49:48.463690+00:00', 'last_updated': '2024-07-27T14:55:30.768241+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.joni_desk_button_battery",
        state=state
    )
    entity_id = "sensor.joni_desk_button_battery"
    unique_id = "00:12:4b:00:25:20:d2:8a-1-1"
    name = "joni-desk-button Battery"
    device_id = "ee80cf293d694022cf00e664a062c06f"


class ButtonJoniDeskButtonIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.joni_desk_button_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'joni-desk-button Identify', 'last_changed': '2024-07-26T17:49:48.464620+00:00', 'last_updated': '2024-07-27T14:55:29.921820+00:00', 'state_value': 'unavailable'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.joni_desk_button_identify",
        state=state
    )
    entity_id = "button.joni_desk_button_identify"
    unique_id = "00:12:4b:00:25:20:d2:8a-1-3"
    name = "joni-desk-button Identify"
    device_id = "ee80cf293d694022cf00e664a062c06f"


class ButtonLivingDownLight02Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_02_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-02 Identify', 'last_changed': '2024-07-27T14:55:29.822260+00:00', 'last_updated': '2024-07-27T14:55:29.822260+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_02_identify",
        state=state
    )
    entity_id = "button.living_down_light_02_identify"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-3"
    name = "living-down-light-02 Identify"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class NumberLivingDownLight02OnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_02_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-02 On level', 'last_changed': '2024-07-27T14:55:30.189418+00:00', 'last_updated': '2024-07-27T14:55:30.189418+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_02_on_level",
        state=state
    )
    entity_id = "number.living_down_light_02_on_level"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-8-on_level"
    name = "living-down-light-02 On level"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class NumberLivingDownLight02OnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_02_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-02 On/Off transition time', 'last_changed': '2024-07-27T14:55:30.182218+00:00', 'last_updated': '2024-07-27T14:55:30.182218+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_02_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_down_light_02_on_off_transition_time"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-8-on_off_transition_time"
    name = "living-down-light-02 On/Off transition time"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class SelectLivingDownLight02StartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_02_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-02 Start-up behavior', 'last_changed': '2024-07-27T14:55:30.511049+00:00', 'last_updated': '2024-07-27T14:55:30.511049+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_02_start_up_behavior",
        state=state
    )
    entity_id = "select.living_down_light_02_start_up_behavior"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-6-StartUpOnOff"
    name = "living-down-light-02 Start-up behavior"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class NumberLivingDownLight02StartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_02_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-02 Start-up current level', 'last_changed': '2024-07-27T14:55:30.195064+00:00', 'last_updated': '2024-07-27T14:55:30.195064+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_02_start_up_current_level",
        state=state
    )
    entity_id = "number.living_down_light_02_start_up_current_level"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-8-start_up_current_level"
    name = "living-down-light-02 Start-up current level"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class ButtonLivingDownLight04Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_04_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-04 Identify', 'last_changed': '2024-07-27T14:55:29.831787+00:00', 'last_updated': '2024-07-27T14:55:29.831787+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_04_identify",
        state=state
    )
    entity_id = "button.living_down_light_04_identify"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-3"
    name = "living-down-light-04 Identify"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class NumberLivingDownLight04OnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_04_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-04 On level', 'last_changed': '2024-07-27T14:55:30.228245+00:00', 'last_updated': '2024-07-27T14:55:30.228245+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_04_on_level",
        state=state
    )
    entity_id = "number.living_down_light_04_on_level"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-8-on_level"
    name = "living-down-light-04 On level"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class NumberLivingDownLight04OnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_04_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-04 On/Off transition time', 'last_changed': '2024-07-27T14:55:30.224428+00:00', 'last_updated': '2024-07-27T14:55:30.224428+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_04_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_down_light_04_on_off_transition_time"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-8-on_off_transition_time"
    name = "living-down-light-04 On/Off transition time"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class SelectLivingDownLight04StartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_04_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-04 Start-up behavior', 'last_changed': '2024-07-27T14:55:30.522237+00:00', 'last_updated': '2024-07-27T14:55:30.522237+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_04_start_up_behavior",
        state=state
    )
    entity_id = "select.living_down_light_04_start_up_behavior"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-6-StartUpOnOff"
    name = "living-down-light-04 Start-up behavior"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class NumberLivingDownLight04StartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_04_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-04 Start-up current level', 'last_changed': '2024-07-27T14:55:30.232090+00:00', 'last_updated': '2024-07-27T14:55:30.232090+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_04_start_up_current_level",
        state=state
    )
    entity_id = "number.living_down_light_04_start_up_current_level"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-8-start_up_current_level"
    name = "living-down-light-04 Start-up current level"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class ButtonLivingDownLight05Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_05_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-05 Identify', 'last_changed': '2024-07-27T14:55:29.837487+00:00', 'last_updated': '2024-07-27T14:55:29.837487+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_05_identify",
        state=state
    )
    entity_id = "button.living_down_light_05_identify"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-3"
    name = "living-down-light-05 Identify"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class NumberLivingDownLight05OnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_05_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-05 On level', 'last_changed': '2024-07-27T14:55:30.247833+00:00', 'last_updated': '2024-07-27T14:55:30.247833+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_05_on_level",
        state=state
    )
    entity_id = "number.living_down_light_05_on_level"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-8-on_level"
    name = "living-down-light-05 On level"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class NumberLivingDownLight05OnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_05_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-05 On/Off transition time', 'last_changed': '2024-07-27T14:55:30.242558+00:00', 'last_updated': '2024-07-27T14:55:30.242558+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_05_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_down_light_05_on_off_transition_time"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-8-on_off_transition_time"
    name = "living-down-light-05 On/Off transition time"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class NumberLivingDownLight05StartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_05_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-05 Start-up current level', 'last_changed': '2024-07-27T14:55:30.254664+00:00', 'last_updated': '2024-07-27T14:55:30.254664+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_05_start_up_current_level",
        state=state
    )
    entity_id = "number.living_down_light_05_start_up_current_level"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-8-start_up_current_level"
    name = "living-down-light-05 Start-up current level"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class SelectLivingDownLight05StartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_05_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-05 Start-up behavior', 'last_changed': '2024-07-27T14:55:30.527677+00:00', 'last_updated': '2024-07-27T14:55:30.527677+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_05_start_up_behavior",
        state=state
    )
    entity_id = "select.living_down_light_05_start_up_behavior"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-6-StartUpOnOff"
    name = "living-down-light-05 Start-up behavior"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class ButtonLivingDownLight07Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_07_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-07 Identify', 'last_changed': '2024-07-27T14:55:29.847134+00:00', 'last_updated': '2024-07-27T14:55:29.847134+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_07_identify",
        state=state
    )
    entity_id = "button.living_down_light_07_identify"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-3"
    name = "living-down-light-07 Identify"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class NumberLivingDownLight07OnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_07_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-07 On level', 'last_changed': '2024-07-27T14:55:30.289145+00:00', 'last_updated': '2024-07-27T14:55:30.289145+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_07_on_level",
        state=state
    )
    entity_id = "number.living_down_light_07_on_level"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-8-on_level"
    name = "living-down-light-07 On level"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class NumberLivingDownLight07OnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_07_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-07 On/Off transition time', 'last_changed': '2024-07-27T14:55:30.283754+00:00', 'last_updated': '2024-07-27T14:55:30.283754+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_07_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_down_light_07_on_off_transition_time"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-8-on_off_transition_time"
    name = "living-down-light-07 On/Off transition time"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class SelectLivingDownLight07StartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_07_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-07 Start-up behavior', 'last_changed': '2024-07-27T14:55:30.536504+00:00', 'last_updated': '2024-07-27T14:55:30.536504+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_07_start_up_behavior",
        state=state
    )
    entity_id = "select.living_down_light_07_start_up_behavior"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-6-StartUpOnOff"
    name = "living-down-light-07 Start-up behavior"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class NumberLivingDownLight07StartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_07_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-07 Start-up current level', 'last_changed': '2024-07-27T14:55:30.293270+00:00', 'last_updated': '2024-07-27T14:55:30.293270+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_07_start_up_current_level",
        state=state
    )
    entity_id = "number.living_down_light_07_start_up_current_level"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-8-start_up_current_level"
    name = "living-down-light-07 Start-up current level"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class ButtonLivingDownLight08Identify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.living_down_light_08_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'living-down-light-08 Identify', 'last_changed': '2024-07-27T14:55:29.850888+00:00', 'last_updated': '2024-07-27T14:55:29.850888+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.living_down_light_08_identify",
        state=state
    )
    entity_id = "button.living_down_light_08_identify"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-3"
    name = "living-down-light-08 Identify"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class NumberLivingDownLight08OnLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_08_on_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-08 On level', 'last_changed': '2024-07-27T14:55:30.307978+00:00', 'last_updated': '2024-07-27T14:55:30.307978+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_08_on_level",
        state=state
    )
    entity_id = "number.living_down_light_08_on_level"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-8-on_level"
    name = "living-down-light-08 On level"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class NumberLivingDownLight08OnOffTransitionTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_08_on_off_transition_time"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 65535, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-08 On/Off transition time', 'last_changed': '2024-07-27T14:55:30.303850+00:00', 'last_updated': '2024-07-27T14:55:30.303850+00:00', 'state_value': 0})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_08_on_off_transition_time",
        state=state
    )
    entity_id = "number.living_down_light_08_on_off_transition_time"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-8-on_off_transition_time"
    name = "living-down-light-08 On/Off transition time"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class SelectLivingDownLight08StartUpBehavior(models.Entity):

    class _StateClass(models.State):
        """State class for entity select.living_down_light_08_start_up_behavior"""
        options: list
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['Off', 'On', 'Toggle', 'PreviousValue'], 'friendly_name': 'living-down-light-08 Start-up behavior', 'last_changed': '2024-07-27T14:55:30.540516+00:00', 'last_updated': '2024-07-27T14:55:30.540516+00:00', 'state_value': 'On'})
    services = my_domains.Select(
        instance=my_ha_instance,
        entity_id="select.living_down_light_08_start_up_behavior",
        state=state
    )
    entity_id = "select.living_down_light_08_start_up_behavior"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-6-StartUpOnOff"
    name = "living-down-light-08 Start-up behavior"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class NumberLivingDownLight08StartUpCurrentLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity number.living_down_light_08_start_up_current_level"""
        min: int
        max: int
        step: float
        mode: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min': 0, 'max': 255, 'step': 1.0, 'mode': 'auto', 'friendly_name': 'living-down-light-08 Start-up current level', 'last_changed': '2024-07-27T14:55:30.312927+00:00', 'last_updated': '2024-07-27T14:55:30.312927+00:00', 'state_value': 255})
    services = my_domains.Number(
        instance=my_ha_instance,
        entity_id="number.living_down_light_08_start_up_current_level",
        state=state
    )
    entity_id = "number.living_down_light_08_start_up_current_level"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-8-start_up_current_level"
    name = "living-down-light-08 Start-up current level"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class LightGaleryFlexoLightLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.galery_flexo_light_light"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        off_with_transition: bool
        off_brightness: int
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'off_with_transition': False, 'off_brightness': 240, 'friendly_name': 'galery-flexo-light Light', 'supported_features': 40, 'last_changed': '2024-07-27T14:55:30.068940+00:00', 'last_updated': '2024-07-27T14:55:30.068940+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.galery_flexo_light_light",
        state=state
    )
    entity_id = "light.galery_flexo_light_light"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1"
    name = "galery-flexo-light Light"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class LightDiningLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.dining_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.dining_main_light_01', 'light.dining_main_light_02'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'dining-lights-group', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.502076+00:00', 'last_updated': '2024-08-03T10:07:11.502076+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.dining_lights_group",
        state=state
    )
    entity_id = "light.dining_lights_group"
    unique_id = "e563ce91670646ec8c16181daa154435"
    name = "dining-lights-group"
    device_id = "None"


class LightGaleryLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.galery_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2000, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 500, 'supported_color_modes': ['color_temp', 'xy'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.galery_light_1', 'light.galery_light_2', 'light.galery_flexo_light_light'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'galery-lights-group', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.610106+00:00', 'last_updated': '2024-08-03T10:07:11.610106+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.galery_lights_group",
        state=state
    )
    entity_id = "light.galery_lights_group"
    unique_id = "8fd24b70c2d80149f9365feb307750f8"
    name = "galery-lights-group"
    device_id = "None"


class LightAmbientLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.ambient_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.galery_downlights_group', 'light.dining_lights_group', 'light.living_ambient_sofa_light', 'light.bed_left_light_light', 'light.bed_right_light_light', 'light.living_down_light_04', 'light.living_down_light_07', 'light.office_downlight_joni'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'ambient-lights-group', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:11.641999+00:00', 'last_updated': '2024-08-03T10:07:11.641999+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.ambient_lights_group",
        state=state
    )
    entity_id = "light.ambient_lights_group"
    unique_id = "8db729ec740700d3cf825ba9151d46e0"
    name = "ambient-lights-group"
    device_id = "None"


class LightBedroomLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.bedroom_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2202, 'max_color_temp_kelvin': 4000, 'min_mireds': 250, 'max_mireds': 454, 'supported_color_modes': ['color_temp'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.bed_left_light_light', 'light.bed_main_light_light', 'light.bed_right_light_light'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'bedroom-lights-group', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:10.595543+00:00', 'last_updated': '2024-08-03T10:07:10.595543+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.bedroom_lights_group",
        state=state
    )
    entity_id = "light.bedroom_lights_group"
    unique_id = "e3efd9bfa4654c4c733498389465c177"
    name = "bedroom-lights-group"
    device_id = "None"


class LightOfficeLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.office_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: str
        brightness: int
        color_temp_kelvin: int
        color_temp: int
        hs_color: list
        rgb_color: list
        xy_color: list
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': 'color_temp', 'brightness': 212, 'color_temp_kelvin': 3300, 'color_temp': 303, 'hs_color': [27.395, 49.303], 'rgb_color': [255, 186, 129], 'xy_color': [0.47, 0.377], 'entity_id': ['light.office_downlight_joni', 'light.office_main_light_light_2', 'light.living_down_light_01'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'office-lights-group', 'supported_features': 44, 'last_changed': '2024-08-03T10:11:02.394672+00:00', 'last_updated': '2024-08-03T10:35:02.374112+00:00', 'state_value': 'on'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.office_lights_group",
        state=state
    )
    entity_id = "light.office_lights_group"
    unique_id = "834b4b19643d13226f86fc2d0fbe036a"
    name = "office-lights-group"
    device_id = "None"


class LightAllLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.all_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: str
        brightness: int
        color_temp_kelvin: int
        color_temp: int
        hs_color: list
        rgb_color: list
        xy_color: list
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': 'color_temp', 'brightness': 212, 'color_temp_kelvin': 3300, 'color_temp': 303, 'hs_color': [27.395, 49.303], 'rgb_color': [255, 186, 129], 'xy_color': [0.47, 0.377], 'entity_id': ['light.living_lights_group', 'light.dining_lights_group', 'light.kitchen_main_light', 'light.galery_lights_group', 'light.bedroom_lights_group', 'light.ambient_lights_group', 'light.office_lights_group'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'all-lights-group', 'supported_features': 44, 'last_changed': '2024-08-03T10:11:02.405044+00:00', 'last_updated': '2024-08-03T10:35:02.384928+00:00', 'state_value': 'on'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.all_lights_group",
        state=state
    )
    entity_id = "light.all_lights_group"
    unique_id = "47a9bf8ed1c8348e369b1e9f7d27e2c0"
    name = "all-lights-group"
    device_id = "None"


class LightLivingLightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.living_lights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        effect_list: list
        supported_color_modes: list
        effect: typing.Any
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 1801, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 555, 'effect_list': ['colorloop'], 'supported_color_modes': ['color_temp', 'xy'], 'effect': None, 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.living_ambient_sofa_light', 'light.living_group_ext', 'light.living_group_mid', 'light.living_group_int'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'living-lights-group', 'supported_features': 44, 'last_changed': '2024-08-03T10:07:08.349653+00:00', 'last_updated': '2024-08-03T10:07:08.349653+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.living_lights_group",
        state=state
    )
    entity_id = "light.living_lights_group"
    unique_id = "798e755d684fea516043925996d5aa89"
    name = "living-lights-group"
    device_id = "None"


class LightGaleryDownlightsGroup(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.galery_downlights_group"""
        min_color_temp_kelvin: int
        max_color_temp_kelvin: int
        min_mireds: int
        max_mireds: int
        supported_color_modes: list
        color_mode: typing.Any
        brightness: typing.Any
        color_temp_kelvin: typing.Any
        color_temp: typing.Any
        hs_color: typing.Any
        rgb_color: typing.Any
        xy_color: typing.Any
        entity_id: list
        icon: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'min_color_temp_kelvin': 2000, 'max_color_temp_kelvin': 6535, 'min_mireds': 153, 'max_mireds': 500, 'supported_color_modes': ['color_temp', 'xy'], 'color_mode': None, 'brightness': None, 'color_temp_kelvin': None, 'color_temp': None, 'hs_color': None, 'rgb_color': None, 'xy_color': None, 'entity_id': ['light.galery_light_1', 'light.galery_light_2'], 'icon': 'mdi:lightbulb-group', 'friendly_name': 'galery-downlights-group', 'supported_features': 40, 'last_changed': '2024-08-03T10:07:11.613411+00:00', 'last_updated': '2024-08-03T10:07:11.613411+00:00', 'state_value': 'off'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.galery_downlights_group",
        state=state
    )
    entity_id = "light.galery_downlights_group"
    unique_id = "63d3967bc8c9395858d9434be07f8165"
    name = "galery-downlights-group"
    device_id = "None"


class SensorBedLeftSwitchBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.bed_left_switch_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.6, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'bed-left-switch Battery', 'last_changed': '2024-08-03T09:37:25.734540+00:00', 'last_updated': '2024-08-03T09:37:25.734540+00:00', 'state_value': 16})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.bed_left_switch_battery",
        state=state
    )
    entity_id = "sensor.bed_left_switch_battery"
    unique_id = "bc:02:6e:ff:fe:00:33:7b-1-1"
    name = "bed-left-switch Battery"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"


class ButtonBedLeftSwitchIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.bed_left_switch_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'bed-left-switch Identify', 'last_changed': '2024-08-03T09:37:25.745620+00:00', 'last_updated': '2024-08-03T09:37:25.745620+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.bed_left_switch_identify",
        state=state
    )
    entity_id = "button.bed_left_switch_identify"
    unique_id = "bc:02:6e:ff:fe:00:33:7b-1-3"
    name = "bed-left-switch Identify"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"


class BinarySensorMacbookJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.macbook_joni"""
        round_trip_time_avg: float
        round_trip_time_max: float
        round_trip_time_mdev: str
        round_trip_time_min: float
        device_class: str
        friendly_name: str
        delay_off: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'round_trip_time_avg': 52.89, 'round_trip_time_max': 126.934, 'round_trip_time_mdev': '', 'round_trip_time_min': 4.924, 'device_class': 'presence', 'friendly_name': 'macbook-joni', 'delay_off': 1, 'last_changed': '2024-08-03T00:30:19.836051+00:00', 'last_updated': '2024-08-03T10:40:12.780485+00:00', 'state_value': 'on'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.macbook_joni",
        state=state
    )
    entity_id = "binary_sensor.macbook_joni"
    unique_id = "083e08fbd57b61e09dea12af125c9d02"
    name = "macbook-joni"
    device_id = "None"


class DeviceTrackerMacbookJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.macbook_joni"""
        source_type: str
        ip: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'router', 'ip': '192.168.1.14', 'friendly_name': 'macbook-joni', 'last_changed': '2024-08-03T00:30:19.836616+00:00', 'last_updated': '2024-08-03T00:30:19.836616+00:00', 'state_value': 'home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.macbook_joni",
        state=state
    )
    entity_id = "device_tracker.macbook_joni"
    unique_id = "083e08fbd57b61e09dea12af125c9d02"
    name = "macbook-joni"
    device_id = "None"


class BinarySensorPcJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pc_joni"""
        device_class: str
        friendly_name: str
        delay_off: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'presence', 'friendly_name': 'pc-joni', 'delay_off': 1, 'last_changed': '2024-08-02T19:31:45.430236+00:00', 'last_updated': '2024-08-02T19:31:45.430236+00:00', 'state_value': 'off'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pc_joni",
        state=state
    )
    entity_id = "binary_sensor.pc_joni"
    unique_id = "78c9fa4c30970673ec45dd3d268ce395"
    name = "pc-joni"
    device_id = "None"


class DeviceTrackerPcJoni(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.pc_joni"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.pc_joni",
        state=state
    )
    entity_id = "device_tracker.pc_joni"
    unique_id = "78c9fa4c30970673ec45dd3d268ce395"
    name = "None"
    device_id = "None"


class UpdateLivingDownLight01Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_01_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-01 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.894525+00:00', 'last_updated': '2024-07-27T14:55:30.894525+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_01_firmware",
        state=state
    )
    entity_id = "update.living_down_light_01_firmware"
    unique_id = "0c:43:14:ff:fe:73:ea:99-1-25-firmware_update"
    name = "living-down-light-01 Firmware"
    device_id = "5faab9fdb078d8eb9823828e963d4880"


class UpdateKitchenMainLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.kitchen_main_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00002000', 'in_progress': False, 'latest_version': '0x00002000', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'kitchen-main-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.900162+00:00', 'last_updated': '2024-07-27T14:55:30.900162+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.kitchen_main_light_firmware",
        state=state
    )
    entity_id = "update.kitchen_main_light_firmware"
    unique_id = "00:12:4b:00:26:b6:fc:1f-1-25-firmware_update"
    name = "kitchen-main-light Firmware"
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"


class UpdateLivingDownLight02Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_02_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-02 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.904421+00:00', 'last_updated': '2024-07-27T14:55:30.904421+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_02_firmware",
        state=state
    )
    entity_id = "update.living_down_light_02_firmware"
    unique_id = "04:cd:15:ff:fe:85:7b:e3-1-25-firmware_update"
    name = "living-down-light-02 Firmware"
    device_id = "28a55a6e1112de03c235ed13f265e5a9"


class UpdateLivingDownLight03Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_03_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-03 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.911150+00:00', 'last_updated': '2024-07-27T14:55:30.911150+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_03_firmware",
        state=state
    )
    entity_id = "update.living_down_light_03_firmware"
    unique_id = "04:cd:15:ff:fe:34:01:38-1-25-firmware_update"
    name = "living-down-light-03 Firmware"
    device_id = "724db7afb158e737b318f8f6a25be76c"


class UpdateLivingDownLight04Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_04_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-04 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.914983+00:00', 'last_updated': '2024-07-27T14:55:30.914983+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_04_firmware",
        state=state
    )
    entity_id = "update.living_down_light_04_firmware"
    unique_id = "0c:43:14:ff:fe:73:f1:99-1-25-firmware_update"
    name = "living-down-light-04 Firmware"
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"


class UpdateLivingDownLight05Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_05_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-05 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.919058+00:00', 'last_updated': '2024-07-27T14:55:30.919058+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_05_firmware",
        state=state
    )
    entity_id = "update.living_down_light_05_firmware"
    unique_id = "0c:43:14:ff:fe:7c:8c:ba-1-25-firmware_update"
    name = "living-down-light-05 Firmware"
    device_id = "382a4339e445922e7979bf4fbc7c47b6"


class UpdateLivingDownLight06Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_06_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-06 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.923982+00:00', 'last_updated': '2024-07-27T14:55:30.923982+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_06_firmware",
        state=state
    )
    entity_id = "update.living_down_light_06_firmware"
    unique_id = "0c:43:14:ff:fe:73:f3:7e-1-25-firmware_update"
    name = "living-down-light-06 Firmware"
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"


class UpdateLivingDownLight07Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_07_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-07 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.928087+00:00', 'last_updated': '2024-07-27T14:55:30.928087+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_07_firmware",
        state=state
    )
    entity_id = "update.living_down_light_07_firmware"
    unique_id = "0c:43:14:ff:fe:74:10:96-1-25-firmware_update"
    name = "living-down-light-07 Firmware"
    device_id = "ec5ebd77800a011201aad0123c4d91bd"


class UpdateLivingDownLight08Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_08_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-08 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.934218+00:00', 'last_updated': '2024-07-27T14:55:30.934218+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_08_firmware",
        state=state
    )
    entity_id = "update.living_down_light_08_firmware"
    unique_id = "04:cd:15:ff:fe:33:ff:6e-1-25-firmware_update"
    name = "living-down-light-08 Firmware"
    device_id = "8b1994f323e86cd5eee43419ff7c2495"


class UpdateLivingDownLight09Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_down_light_09_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10a06500', 'in_progress': False, 'latest_version': '0x10a06500', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-down-light-09 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.938331+00:00', 'last_updated': '2024-07-27T14:55:30.938331+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_down_light_09_firmware",
        state=state
    )
    entity_id = "update.living_down_light_09_firmware"
    unique_id = "0c:43:14:ff:fe:73:dc:d6-1-25-firmware_update"
    name = "living-down-light-09 Firmware"
    device_id = "884dfdc10561d0534b50d884aad3b132"


class UpdateGaleryFlexoLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.galery_flexo_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00010012', 'in_progress': False, 'latest_version': '0x00010012', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'galery-flexo-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.943213+00:00', 'last_updated': '2024-07-27T14:55:30.943213+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.galery_flexo_light_firmware",
        state=state
    )
    entity_id = "update.galery_flexo_light_firmware"
    unique_id = "84:ba:20:ff:fe:ad:9c:63-1-25-firmware_update"
    name = "galery-flexo-light Firmware"
    device_id = "22dba118ea8c1a7086ad4479d1e95712"


class UpdateBedMainLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_main_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x21022631', 'in_progress': False, 'latest_version': '0x21022631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-main-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.949020+00:00', 'last_updated': '2024-07-27T14:55:30.949020+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_main_light_firmware",
        state=state
    )
    entity_id = "update.bed_main_light_firmware"
    unique_id = "50:32:5f:ff:fe:71:eb:db-1-25-firmware_update"
    name = "bed-main-light Firmware"
    device_id = "176891a7db6daf1e864a9e578cea3388"


class UpdateOfficeMainLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.office_main_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x21022631', 'in_progress': False, 'latest_version': '0x21022631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'office-main-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.955266+00:00', 'last_updated': '2024-07-27T14:55:30.955266+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.office_main_light_firmware",
        state=state
    )
    entity_id = "update.office_main_light_firmware"
    unique_id = "0c:43:14:ff:fe:9c:fd:a9-1-25-firmware_update"
    name = "office-main-light Firmware"
    device_id = "6a38306ec46728170175ef7cac3ea4ea"


class UpdateBedMainSwitch01Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_main_switch_01_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x22010631', 'in_progress': False, 'latest_version': '0x22010631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-main-switch-01 Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T09:13:41.553429+00:00', 'last_updated': '2024-08-03T09:13:41.553429+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_main_switch_01_firmware",
        state=state
    )
    entity_id = "update.bed_main_switch_01_firmware"
    unique_id = "bc:02:6e:ff:fe:00:33:8c-1-25-firmware_update"
    name = "bed-main-switch-01 Firmware"
    device_id = "f61b9317af000c4b650b5d686343895e"


class UpdateOfficeMainSwitch01Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.office_main_switch_01_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x22010631', 'in_progress': False, 'latest_version': '0x22010631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'office-main-switch-01 Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T08:17:09.640108+00:00', 'last_updated': '2024-08-03T08:17:09.640108+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.office_main_switch_01_firmware",
        state=state
    )
    entity_id = "update.office_main_switch_01_firmware"
    unique_id = "bc:02:6e:ff:fe:00:3c:36-1-25-firmware_update"
    name = "office-main-switch-01 Firmware"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"


class UpdateBedLeftSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_left_switch_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x22010631', 'in_progress': False, 'latest_version': '0x22010631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-left-switch Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T09:37:24.656049+00:00', 'last_updated': '2024-08-03T09:37:24.656049+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_left_switch_firmware",
        state=state
    )
    entity_id = "update.bed_left_switch_firmware"
    unique_id = "bc:02:6e:ff:fe:00:33:7b-1-25-firmware_update"
    name = "bed-left-switch Firmware"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"


class UpdateLivingMainControlFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_main_control_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00010024', 'in_progress': False, 'latest_version': '0x00010024', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-main-control Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T10:03:44.655563+00:00', 'last_updated': '2024-08-03T10:03:44.655563+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_main_control_firmware",
        state=state
    )
    entity_id = "update.living_main_control_firmware"
    unique_id = "00:3c:84:ff:fe:df:f8:31-1-25-firmware_update"
    name = "living-main-control Firmware"
    device_id = "a701fbed4393032c83f56e66d56c2a83"


class UpdateDiningMainSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.dining_main_switch_firmware"""
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'dining-main-switch Firmware', 'supported_features': 7, 'last_changed': '2024-08-02T18:27:54.604780+00:00', 'last_updated': '2024-08-02T18:27:54.604780+00:00', 'state_value': 'unavailable'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.dining_main_switch_firmware",
        state=state
    )
    entity_id = "update.dining_main_switch_firmware"
    unique_id = "bc:02:6e:ff:fe:00:37:17-1-25-firmware_update"
    name = "dining-main-switch Firmware"
    device_id = "2851603edfb42a65d6925eb41f784bbb"


class UpdateBedRightLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_right_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00010012', 'in_progress': False, 'latest_version': '0x00010012', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-right-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.987270+00:00', 'last_updated': '2024-07-27T14:55:30.987270+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_right_light_firmware",
        state=state
    )
    entity_id = "update.bed_right_light_firmware"
    unique_id = "90:35:ea:ff:fe:d5:0e:a6-1-25-firmware_update"
    name = "bed-right-light Firmware"
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"


class UpdateBedRightSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_right_switch_firmware"""
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-right-switch Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T04:05:39.875027+00:00', 'last_updated': '2024-08-03T04:05:39.875027+00:00', 'state_value': 'unavailable'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_right_switch_firmware",
        state=state
    )
    entity_id = "update.bed_right_switch_firmware"
    unique_id = "6c:5c:b1:ff:fe:13:39:54-1-25-firmware_update"
    name = "bed-right-switch Firmware"
    device_id = "df2045cfeac2943e4f94fa9a24723277"


class UpdateOfficeDownlightJoniFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.office_downlight_joni_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x10021655', 'in_progress': False, 'latest_version': '0x10021655', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'office-downlight-joni Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.997874+00:00', 'last_updated': '2024-07-27T14:55:30.997874+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.office_downlight_joni_firmware",
        state=state
    )
    entity_id = "update.office_downlight_joni_firmware"
    unique_id = "6c:5c:b1:ff:fe:06:e6:cc-1-25-firmware_update"
    name = "office-downlight-joni Firmware"
    device_id = "d41fe84161aac5e954aa7d78d91b1819"


class UpdateLivingAmbientSofaFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.living_ambient_sofa_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00010012', 'in_progress': False, 'latest_version': '0x00010012', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'living-ambient-sofa Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.003037+00:00', 'last_updated': '2024-07-27T14:55:31.003037+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.living_ambient_sofa_firmware",
        state=state
    )
    entity_id = "update.living_ambient_sofa_firmware"
    unique_id = "6c:5c:b1:ff:fe:30:a5:da-1-25-firmware_update"
    name = "living-ambient-sofa Firmware"
    device_id = "20524a8c01e94ae3e70f83771ade00f7"


class UpdateBedLeftLightFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.bed_left_light_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00010012', 'in_progress': False, 'latest_version': '0x00010012', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'bed-left-light Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.007277+00:00', 'last_updated': '2024-07-27T14:55:31.007277+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.bed_left_light_firmware",
        state=state
    )
    entity_id = "update.bed_left_light_firmware"
    unique_id = "90:35:ea:ff:fe:00:96:29-1-25-firmware_update"
    name = "bed-left-light Firmware"
    device_id = "4235267e075fb2a70160bdc771810295"


class UpdateKitchenMainSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.kitchen_main_switch_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x22010631', 'in_progress': False, 'latest_version': '0x22010631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'kitchen-main-switch Firmware', 'supported_features': 7, 'last_changed': '2024-08-03T06:04:52.948064+00:00', 'last_updated': '2024-08-03T06:04:52.948064+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.kitchen_main_switch_firmware",
        state=state
    )
    entity_id = "update.kitchen_main_switch_firmware"
    unique_id = "bc:02:6e:ff:fe:00:3c:3c-1-25-firmware_update"
    name = "kitchen-main-switch Firmware"
    device_id = "83f3a2ec56c0e312b046b46446691791"


class UpdateGaleryLight1Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.galery_light_1_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x0000005e', 'in_progress': False, 'latest_version': '0x0000005e', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'galery-light-1 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.018694+00:00', 'last_updated': '2024-07-27T14:55:31.018694+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.galery_light_1_firmware",
        state=state
    )
    entity_id = "update.galery_light_1_firmware"
    unique_id = "a4:c1:38:f6:7a:e9:e9:9a-1-25-firmware_update"
    name = "galery-light-1 Firmware"
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"


class UpdateGaleryLight2Firmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.galery_light_2_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x0000005e', 'in_progress': False, 'latest_version': '0x0000005e', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'galery-light-2 Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.023632+00:00', 'last_updated': '2024-07-27T14:55:31.023632+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.galery_light_2_firmware",
        state=state
    )
    entity_id = "update.galery_light_2_firmware"
    unique_id = "a4:c1:38:88:68:ac:e8:7b-1-25-firmware_update"
    name = "galery-light-2 Firmware"
    device_id = "773311fd39675f914631c4de4261699b"


class DeviceTrackerMi9Clau(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.mi9_clau"""
        source_type: str
        latitude: float
        longitude: float
        gps_accuracy: int
        altitude: int
        course: int
        speed: int
        vertical_accuracy: int
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'gps', 'latitude': 41.4205493, 'longitude': 2.1578256, 'gps_accuracy': 100, 'altitude': 208, 'course': 0, 'speed': 0, 'vertical_accuracy': 100, 'friendly_name': 'mi9-clau', 'last_changed': '2024-07-25T11:39:10.225508+00:00', 'last_updated': '2024-07-25T11:39:10.225508+00:00', 'state_value': 'home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.mi9_clau",
        state=state
    )
    entity_id = "device_tracker.mi9_clau"
    unique_id = "154d8abe70553aa6"
    name = "mi9-clau"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauDetectedActivity(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_detected_activity"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_detected_activity",
        state=state
    )
    entity_id = "sensor.mi9_clau_detected_activity"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_detected_activity"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauSleepConfidence(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_sleep_confidence"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_sleep_confidence",
        state=state
    )
    entity_id = "sensor.mi9_clau_sleep_confidence"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_sleep_confidence"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauSleepSegment(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_sleep_segment"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_sleep_segment",
        state=state
    )
    entity_id = "sensor.mi9_clau_sleep_segment"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_sleep_segment"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauAndroidAuto(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_android_auto"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_android_auto",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_android_auto"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_android_auto"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauOsVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_os_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_os_version",
        state=state
    )
    entity_id = "sensor.mi9_clau_os_version"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_android_os_version"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauSecurityPatch(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_security_patch"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_security_patch",
        state=state
    )
    entity_id = "sensor.mi9_clau_security_patch"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_android_os_security_patch"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCurrentVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_current_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_current_version",
        state=state
    )
    entity_id = "sensor.mi9_clau_current_version"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_current_version"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAppRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_app_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_app_rx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_app_rx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_rx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAppTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_app_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_app_tx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_app_tx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_tx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAppMemory(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_app_memory"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_app_memory",
        state=state
    )
    entity_id = "sensor.mi9_clau_app_memory"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_memory"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauAppInactive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_app_inactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_app_inactive",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_app_inactive"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_inactive"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAppStandbyBucket(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_app_standby_bucket"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_app_standby_bucket",
        state=state
    )
    entity_id = "sensor.mi9_clau_app_standby_bucket"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_standby_bucket"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAppImportance(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_app_importance"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_app_importance",
        state=state
    )
    entity_id = "sensor.mi9_clau_app_importance"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_app_importance"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauRingerMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_ringer_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_ringer_mode",
        state=state
    )
    entity_id = "sensor.mi9_clau_ringer_mode"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_audio_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauAudioMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_audio_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_audio_mode",
        state=state
    )
    entity_id = "sensor.mi9_clau_audio_mode"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_audio_mode"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauHeadphones(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_headphones"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_headphones",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_headphones"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_headphone_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauMicMuted(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_mic_muted"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_mic_muted",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_mic_muted"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_mic_muted"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauSpeakerphone(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_speakerphone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_speakerphone",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_speakerphone"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_speakerphone_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauMusicActive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_music_active"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_music_active",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_music_active"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_music_active"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_alarm",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_alarm"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_alarm"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelCall(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_call"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_call",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_call"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_call"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelMusic(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_music"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_music",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_music"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_music"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelRinger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_ringer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_ringer",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_ringer"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_ring"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_notification",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_notification"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_notification"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelSystem(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_system"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_system",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_system"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_system"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelDtmf(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_dtmf"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_dtmf",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_dtmf"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_dtmf"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauVolumeLevelAccessibility(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_volume_level_accessibility"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_volume_level_accessibility",
        state=state
    )
    entity_id = "sensor.mi9_clau_volume_level_accessibility"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_volume_accessibility"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBatteryLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_battery_level"""
        unit_of_measurement: str
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'unit_of_measurement': '%', 'device_class': 'battery', 'icon': 'mdi:battery-outline', 'friendly_name': 'mi9-clau Battery level', 'last_changed': '2024-07-25T11:39:10.240185+00:00', 'last_updated': '2024-07-25T11:39:10.240185+00:00', 'state_value': 1})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_battery_level",
        state=state
    )
    entity_id = "sensor.mi9_clau_battery_level"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_battery_level"
    name = "mi9-clau Battery level"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBatteryState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_battery_state"""
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'icon': 'mdi:battery-minus', 'friendly_name': 'mi9-clau Battery state', 'last_changed': '2024-07-25T11:39:10.243699+00:00', 'last_updated': '2024-07-25T11:39:10.243699+00:00', 'state_value': 'discharging'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_battery_state",
        state=state
    )
    entity_id = "sensor.mi9_clau_battery_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_battery_state"
    name = "mi9-clau Battery state"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauIsCharging(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_is_charging"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_is_charging",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_is_charging"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_is_charging"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauChargerType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_charger_type"""
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'icon': 'mdi:battery', 'friendly_name': 'mi9-clau Charger type', 'last_changed': '2024-07-25T11:39:10.246651+00:00', 'last_updated': '2024-07-25T11:39:10.246651+00:00', 'state_value': 'none'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_charger_type",
        state=state
    )
    entity_id = "sensor.mi9_clau_charger_type"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_charger_type"
    name = "mi9-clau Charger type"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBatteryHealth(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_battery_health"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_battery_health",
        state=state
    )
    entity_id = "sensor.mi9_clau_battery_health"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_battery_health"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBatteryTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_battery_temperature"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_battery_temperature",
        state=state
    )
    entity_id = "sensor.mi9_clau_battery_temperature"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_battery_temperature"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBatteryPower(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_battery_power"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_battery_power",
        state=state
    )
    entity_id = "sensor.mi9_clau_battery_power"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_battery_power"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBluetoothConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_bluetooth_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_bluetooth_connection",
        state=state
    )
    entity_id = "sensor.mi9_clau_bluetooth_connection"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_bluetooth_connection"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauBluetoothState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_bluetooth_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_bluetooth_state",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_bluetooth_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_bluetooth_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBleTransmitter(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_ble_transmitter"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_ble_transmitter",
        state=state
    )
    entity_id = "sensor.mi9_clau_ble_transmitter"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_ble_emitter"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauBeaconMonitor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_beacon_monitor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_beacon_monitor",
        state=state
    )
    entity_id = "sensor.mi9_clau_beacon_monitor"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_beacon_monitor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_battery"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_battery",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_battery"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_battery"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarName(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_name"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_name",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_name"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_name"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarChargingStatus(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_charging_status"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_charging_status",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_charging_status"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_charging_status"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarEvConnectorType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_ev_connector_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_ev_connector_type",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_ev_connector_type"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_ev_connector"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarFuel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_fuel"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_fuel",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_fuel"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_fuel"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarFuelType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_fuel_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_fuel_type",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_fuel_type"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_fuel_type"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCarOdometer(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_car_odometer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_car_odometer",
        state=state
    )
    entity_id = "sensor.mi9_clau_car_odometer"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_car_odometer"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauScreenBrightness(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_screen_brightness"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_screen_brightness",
        state=state
    )
    entity_id = "sensor.mi9_clau_screen_brightness"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_screen_brightness"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauScreenOffTimeout(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_screen_off_timeout"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_screen_off_timeout",
        state=state
    )
    entity_id = "sensor.mi9_clau_screen_off_timeout"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_screen_off_timeout"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauDoNotDisturbSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_do_not_disturb_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_do_not_disturb_sensor",
        state=state
    )
    entity_id = "sensor.mi9_clau_do_not_disturb_sensor"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_dnd_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauWorkProfile(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_work_profile"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_work_profile",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_work_profile"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_is_work_profile"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauGeocodedLocation(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_geocoded_location"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_geocoded_location",
        state=state
    )
    entity_id = "sensor.mi9_clau_geocoded_location"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_geocoded_location"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauDeviceLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_device_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_device_locked",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_device_locked"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_device_locked"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauDeviceSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_device_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_device_secure",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_device_secure"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_device_secure"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauKeyguardLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_keyguard_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_keyguard_locked",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_keyguard_locked"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_keyguard_locked"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauKeyguardSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_keyguard_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_keyguard_secure",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_keyguard_secure"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_keyguard_secure"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLastUsedApp(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_last_used_app"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_last_used_app",
        state=state
    )
    entity_id = "sensor.mi9_clau_last_used_app"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_last_used_app"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLastReboot(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_last_reboot"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_last_reboot",
        state=state
    )
    entity_id = "sensor.mi9_clau_last_reboot"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_last_reboot"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLastUpdateTrigger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_last_update_trigger"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_last_update_trigger",
        state=state
    )
    entity_id = "sensor.mi9_clau_last_update_trigger"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_last_update"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLightSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_light_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_light_sensor",
        state=state
    )
    entity_id = "sensor.mi9_clau_light_sensor"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_light_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauHighAccuracyMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_high_accuracy_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_high_accuracy_mode",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_high_accuracy_mode"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_high_accuracy_mode"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauHighAccuracyUpdateInterval(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_high_accuracy_update_interval"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_high_accuracy_update_interval",
        state=state
    )
    entity_id = "sensor.mi9_clau_high_accuracy_update_interval"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_high_accuracy_update_interval"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauMobileData(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_mobile_data"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_mobile_data",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_mobile_data"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_mobile_data"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauMobileDataRoaming(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_mobile_data_roaming"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_mobile_data_roaming",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_mobile_data_roaming"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_mobile_data_roaming"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_connection",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_connection"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_connection"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiBssid(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_bssid"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_bssid",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_bssid"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_bssid"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_ip_address",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_ip_address"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_ip_address"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiLinkSpeed(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_link_speed"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_link_speed",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_link_speed"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_link_speed"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauWifiState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_wifi_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_wifi_state",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_wifi_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiFrequency(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_frequency"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_frequency",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_frequency"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_frequency"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauWifiSignalStrength(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_wifi_signal_strength"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_wifi_signal_strength",
        state=state
    )
    entity_id = "sensor.mi9_clau_wifi_signal_strength"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_wifi_signal_strength"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauPublicIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_public_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_public_ip_address",
        state=state
    )
    entity_id = "sensor.mi9_clau_public_ip_address"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_public_ip_address"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauHotspotState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_hotspot_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_hotspot_state",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_hotspot_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_hotspot_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauNetworkType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_network_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_network_type",
        state=state
    )
    entity_id = "sensor.mi9_clau_network_type"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_network_type"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauNfcState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_nfc_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_nfc_state",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_nfc_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_nfc_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauNextAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_next_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_next_alarm",
        state=state
    )
    entity_id = "sensor.mi9_clau_next_alarm"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_next_alarm"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLastNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_last_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_last_notification",
        state=state
    )
    entity_id = "sensor.mi9_clau_last_notification"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_last_notification"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauLastRemovedNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_last_removed_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_last_removed_notification",
        state=state
    )
    entity_id = "sensor.mi9_clau_last_removed_notification"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_last_removed_notification"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauActiveNotificationCount(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_active_notification_count"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_active_notification_count",
        state=state
    )
    entity_id = "sensor.mi9_clau_active_notification_count"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_active_notification_count"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauMediaSession(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_media_session"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_media_session",
        state=state
    )
    entity_id = "sensor.mi9_clau_media_session"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_media_session"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauPhoneState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_phone_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_phone_state",
        state=state
    )
    entity_id = "sensor.mi9_clau_phone_state"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_phone_state"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauSim1(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_sim_1"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_sim_1",
        state=state
    )
    entity_id = "sensor.mi9_clau_sim_1"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_sim_1"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauSim2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_sim_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_sim_2",
        state=state
    )
    entity_id = "sensor.mi9_clau_sim_2"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_sim_2"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauInteractive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_interactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_interactive",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_interactive"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_is_interactive"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauDozeMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_doze_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_doze_mode",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_doze_mode"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_is_idle"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorMi9ClauPowerSave(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.mi9_clau_power_save"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.mi9_clau_power_save",
        state=state
    )
    entity_id = "binary_sensor.mi9_clau_power_save"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_power_save"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauProximitySensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_proximity_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_proximity_sensor",
        state=state
    )
    entity_id = "sensor.mi9_clau_proximity_sensor"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_proximity_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauStepsSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_steps_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_steps_sensor",
        state=state
    )
    entity_id = "sensor.mi9_clau_steps_sensor"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_steps_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauInternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_internal_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_internal_storage",
        state=state
    )
    entity_id = "sensor.mi9_clau_internal_storage"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_storage_sensor"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauExternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_external_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_external_storage",
        state=state
    )
    entity_id = "sensor.mi9_clau_external_storage"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_external_storage"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauCurrentTimeZone(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_current_time_zone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_current_time_zone",
        state=state
    )
    entity_id = "sensor.mi9_clau_current_time_zone"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_current_time_zone"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauMobileRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_mobile_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_mobile_rx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_mobile_rx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_mobile_rx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauMobileTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_mobile_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_mobile_tx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_mobile_tx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_mobile_tx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauTotalRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_total_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_total_rx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_total_rx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_total_rx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorMi9ClauTotalTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_total_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_total_tx_gb",
        state=state
    )
    entity_id = "sensor.mi9_clau_total_tx_gb"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_total_tx_gb"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class SensorOfficeJoniSwitchBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.office_joni_switch_battery"""
        state_class: str
        battery_size: str
        battery_quantity: int
        battery_voltage: float
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'battery_size': 'CR2032', 'battery_quantity': 1, 'battery_voltage': 2.5, 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'office-joni-switch Battery', 'last_changed': '2024-08-03T09:18:35.236305+00:00', 'last_updated': '2024-08-03T10:20:24.996134+00:00', 'state_value': 16})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.office_joni_switch_battery",
        state=state
    )
    entity_id = "sensor.office_joni_switch_battery"
    unique_id = "bc:02:6e:ff:fe:00:2c:8e-1-1"
    name = "office-joni-switch Battery"
    device_id = "6d1eca1676129527c2ad74b66e39e435"


class UpdateOfficeJoniSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.office_joni_switch_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x22010631', 'in_progress': False, 'latest_version': '0x22010631', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'office-joni-switch Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:30.968131+00:00', 'last_updated': '2024-07-27T14:55:30.968131+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.office_joni_switch_firmware",
        state=state
    )
    entity_id = "update.office_joni_switch_firmware"
    unique_id = "bc:02:6e:ff:fe:00:2c:8e-1-25-firmware_update"
    name = "office-joni-switch Firmware"
    device_id = "6d1eca1676129527c2ad74b66e39e435"


class ButtonOfficeJoniSwitchIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_joni_switch_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'office-joni-switch Identify', 'last_changed': '2024-07-27T14:55:29.886894+00:00', 'last_updated': '2024-07-27T14:55:29.886894+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_joni_switch_identify",
        state=state
    )
    entity_id = "button.office_joni_switch_identify"
    unique_id = "bc:02:6e:ff:fe:00:2c:8e-1-3"
    name = "office-joni-switch Identify"
    device_id = "6d1eca1676129527c2ad74b66e39e435"


class DeviceTrackerMacbookClau(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.macbook_clau"""
        source_type: str
        ip: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'router', 'ip': '192.168.1.16', 'friendly_name': 'macbook-clau', 'last_changed': '2024-07-25T11:38:55.872947+00:00', 'last_updated': '2024-07-25T11:38:55.872947+00:00', 'state_value': 'not_home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.macbook_clau",
        state=state
    )
    entity_id = "device_tracker.macbook_clau"
    unique_id = "45fecb87e3b0ef2126a8501044f7d61e"
    name = "macbook-clau"
    device_id = "None"


class BinarySensorMacbookClau(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.macbook_clau"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'connectivity', 'friendly_name': 'macbook-clau', 'last_changed': '2024-07-25T11:38:55.863710+00:00', 'last_updated': '2024-07-25T11:38:55.863710+00:00', 'state_value': 'off'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.macbook_clau",
        state=state
    )
    entity_id = "binary_sensor.macbook_clau"
    unique_id = "45fecb87e3b0ef2126a8501044f7d61e"
    name = "macbook-clau"
    device_id = "None"


class SensorTemperaturePl0Salon2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.temperature_pl_0_salon_2"""
        restored: bool
        device_class: str
        friendly_name: str
        supported_features: int
        unit_of_measurement: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'device_class': 'temperature', 'friendly_name': 'Temperature Pl_0_salon', 'supported_features': 0, 'unit_of_measurement': '°C', 'last_changed': '2024-07-25T11:39:37.436981+00:00', 'last_updated': '2024-07-25T11:39:37.436981+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.temperature_pl_0_salon_2",
        state=state
    )
    entity_id = "sensor.temperature_pl_0_salon_2"
    unique_id = "Pl_0_Salon_temperature_8"
    name = "Temperature Pl_0_salon"
    device_id = "65ded3c93e6fbb30c0a8785b42d1c805"


class SensorHumidityPl0Salon2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.humidity_pl_0_salon_2"""
        restored: bool
        device_class: str
        friendly_name: str
        supported_features: int
        unit_of_measurement: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'device_class': 'humidity', 'friendly_name': 'Humidity Pl_0_salon', 'supported_features': 0, 'unit_of_measurement': '%', 'last_changed': '2024-07-25T11:39:37.437371+00:00', 'last_updated': '2024-07-25T11:39:37.437371+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.humidity_pl_0_salon_2",
        state=state
    )
    entity_id = "sensor.humidity_pl_0_salon_2"
    unique_id = "Pl_0_Salon_humidity_8"
    name = "Humidity Pl_0_salon"
    device_id = "988fea5204e506a2a0ff0bc5e45093ff"


class SensorAirQualityPl0Salon2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.air_quality_pl_0_salon_2"""
        restored: bool
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'friendly_name': 'Air Quality Pl_0_salon', 'supported_features': 0, 'last_changed': '2024-07-25T11:39:37.437674+00:00', 'last_updated': '2024-07-25T11:39:37.437674+00:00', 'state_value': 'unavailable'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.air_quality_pl_0_salon_2",
        state=state
    )
    entity_id = "sensor.air_quality_pl_0_salon_2"
    unique_id = "Pl_0_Salonairquality_8"
    name = "Air Quality Pl_0_salon"
    device_id = "fa9442ab908ab92b520b5e5f3517d303"


class SceneDjZone(models.Entity):

    class _StateClass(models.State):
        """State class for entity scene.dj_zone"""
        entity_id: list
        id: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'entity_id': ['light.galery_flexo_light_light', 'light.galery_light_1', 'light.galery_light_2', 'light.dining_lights_group', 'light.living_ambient_sofa_light', 'light.living_down_light_04', 'light.living_down_light_09'], 'id': '1710262871537', 'icon': 'mdi:headphones', 'friendly_name': 'dj_zone', 'last_changed': '2024-07-25T11:38:40.828501+00:00', 'last_updated': '2024-07-25T11:38:40.828501+00:00', 'state_value': '2024-07-01T20:34:55.765224+00:00'})
    services = my_domains.Scene(
        instance=my_ha_instance,
        entity_id="scene.dj_zone",
        state=state
    )
    entity_id = "scene.dj_zone"
    unique_id = "1710262871537"
    name = "dj_zone"
    device_id = "None"


class SensorTexasInstrumentsCoordinator(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.texas_instruments_coordinator"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.texas_instruments_coordinator",
        state=state
    )
    entity_id = "sensor.texas_instruments_coordinator"
    unique_id = "00-12-4b-00-25-e1-da-3a_counters_Retry_NONE_0"
    name = "None"
    device_id = "a0538bfb15ee03e0ea1ef75b8faf09b9"


class BinarySensorConnectlifeApiProxyMqttAddOnRunning(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.connectlife_api_proxy_mqtt_add_on_running"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.connectlife_api_proxy_mqtt_add_on_running",
        state=state
    )
    entity_id = "binary_sensor.connectlife_api_proxy_mqtt_add_on_running"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_state"
    name = "None"
    device_id = "399279ef0578b11ba8127f34426026a1"


class SensorConnectlifeApiProxyMqttAddOnVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.connectlife_api_proxy_mqtt_add_on_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.connectlife_api_proxy_mqtt_add_on_version",
        state=state
    )
    entity_id = "sensor.connectlife_api_proxy_mqtt_add_on_version"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_version"
    name = "None"
    device_id = "399279ef0578b11ba8127f34426026a1"


class SensorConnectlifeApiProxyMqttAddOnNewestVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.connectlife_api_proxy_mqtt_add_on_newest_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.connectlife_api_proxy_mqtt_add_on_newest_version",
        state=state
    )
    entity_id = "sensor.connectlife_api_proxy_mqtt_add_on_newest_version"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_version_latest"
    name = "None"
    device_id = "399279ef0578b11ba8127f34426026a1"


class SensorConnectlifeApiProxyMqttAddOnCpuPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.connectlife_api_proxy_mqtt_add_on_cpu_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.connectlife_api_proxy_mqtt_add_on_cpu_percent",
        state=state
    )
    entity_id = "sensor.connectlife_api_proxy_mqtt_add_on_cpu_percent"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_cpu_percent"
    name = "None"
    device_id = "399279ef0578b11ba8127f34426026a1"


class SensorConnectlifeApiProxyMqttAddOnMemoryPercent(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.connectlife_api_proxy_mqtt_add_on_memory_percent"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.connectlife_api_proxy_mqtt_add_on_memory_percent",
        state=state
    )
    entity_id = "sensor.connectlife_api_proxy_mqtt_add_on_memory_percent"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_memory_percent"
    name = "None"
    device_id = "399279ef0578b11ba8127f34426026a1"


class UpdateConnectlifeApiProxyMqttAddOnUpdate(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.connectlife_api_proxy_mqtt_add_on_update"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: str
        release_url: typing.Any
        skipped_version: typing.Any
        title: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '2.1.11', 'in_progress': False, 'latest_version': '2.1.11', 'release_summary': '# Changelog\n\nAll notable changes to this project will be documented in this file.\n\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),\nand this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n##', 'release_url': None, 'skipped_version': None, 'title': 'Connectlife API proxy & MQTT Add-on', 'friendly_name': 'Connectlife API proxy & MQTT Add-on Update', 'supported_features': 25, 'last_changed': '2024-07-25T11:38:29.406036+00:00', 'last_updated': '2024-07-25T11:38:29.406036+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.connectlife_api_proxy_mqtt_add_on_update",
        state=state
    )
    entity_id = "update.connectlife_api_proxy_mqtt_add_on_update"
    unique_id = "04d8eb11_connectlife-api-proxy-mqtt_version_latest"
    name = "Connectlife API proxy & MQTT Add-on Update"
    device_id = "399279ef0578b11ba8127f34426026a1"


class InputNumberClimateLivingTemp(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_number.climate_living_temp"""
        initial: typing.Any
        editable: bool
        min: float
        max: float
        step: float
        mode: str
        unit_of_measurement: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'initial': None, 'editable': True, 'min': 18.0, 'max': 24.0, 'step': 1.0, 'mode': 'box', 'unit_of_measurement': 'ºC', 'icon': 'mdi:air-conditioner', 'friendly_name': 'climate-living-temp', 'last_changed': '2024-07-25T11:38:47.021110+00:00', 'last_updated': '2024-07-25T11:38:47.021110+00:00', 'state_value': 20.0})
    services = my_domains.InputNumber(
        instance=my_ha_instance,
        entity_id="input_number.climate_living_temp",
        state=state
    )
    entity_id = "input_number.climate_living_temp"
    unique_id = "climate_living_temp"
    name = "climate-living-temp"
    device_id = "None"


class InputNumberClimateOfficeTemp(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_number.climate_office_temp"""
        initial: typing.Any
        editable: bool
        min: float
        max: float
        step: float
        mode: str
        unit_of_measurement: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'initial': None, 'editable': True, 'min': 18.0, 'max': 24.0, 'step': 1.0, 'mode': 'box', 'unit_of_measurement': 'ºC', 'icon': 'mdi:air-conditioner', 'friendly_name': 'climate-office-temp', 'last_changed': '2024-07-25T11:38:47.023592+00:00', 'last_updated': '2024-07-25T11:38:47.023592+00:00', 'state_value': 20.0})
    services = my_domains.InputNumber(
        instance=my_ha_instance,
        entity_id="input_number.climate_office_temp",
        state=state
    )
    entity_id = "input_number.climate_office_temp"
    unique_id = "climate_office_temp"
    name = "climate-office-temp"
    device_id = "None"


class InputBooleanClimateSwitch(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_boolean.climate_switch"""
        editable: bool
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'editable': True, 'icon': 'mdi:air-conditioner', 'friendly_name': 'climate-switch', 'last_changed': '2024-07-25T11:38:47.285823+00:00', 'last_updated': '2024-07-25T11:38:47.285823+00:00', 'state_value': 'off'})
    services = my_domains.InputBoolean(
        instance=my_ha_instance,
        entity_id="input_boolean.climate_switch",
        state=state
    )
    entity_id = "input_boolean.climate_switch"
    unique_id = "climate_switch"
    name = "climate-switch"
    device_id = "None"


class SensorDateTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.date_time"""
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'icon': 'mdi:calendar-clock', 'friendly_name': 'Date & Time', 'last_changed': '2024-08-03T10:40:00.002530+00:00', 'last_updated': '2024-08-03T10:40:00.002530+00:00', 'state_value': '2024-08-03, 12:40'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.date_time",
        state=state
    )
    entity_id = "sensor.date_time"
    unique_id = "date_time"
    name = "Date & Time"
    device_id = "None"


class SensorS23JoniDetectedActivity(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_detected_activity"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_detected_activity",
        state=state
    )
    entity_id = "sensor.s23_joni_detected_activity"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_detected_activity"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniSleepConfidence(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_sleep_confidence"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_sleep_confidence",
        state=state
    )
    entity_id = "sensor.s23_joni_sleep_confidence"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_sleep_confidence"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniSleepSegment(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_sleep_segment"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_sleep_segment",
        state=state
    )
    entity_id = "sensor.s23_joni_sleep_segment"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_sleep_segment"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniAndroidAuto(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_android_auto"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_android_auto",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_android_auto"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_android_auto"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniOsVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_os_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_os_version",
        state=state
    )
    entity_id = "sensor.s23_joni_os_version"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_android_os_version"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniSecurityPatch(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_security_patch"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_security_patch",
        state=state
    )
    entity_id = "sensor.s23_joni_security_patch"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_android_os_security_patch"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCurrentVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_current_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_current_version",
        state=state
    )
    entity_id = "sensor.s23_joni_current_version"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_current_version"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAppRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_app_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_app_rx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_app_rx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_rx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAppTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_app_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_app_tx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_app_tx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_tx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAppMemory(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_app_memory"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_app_memory",
        state=state
    )
    entity_id = "sensor.s23_joni_app_memory"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_memory"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniAppInactive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_app_inactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_app_inactive",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_app_inactive"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_inactive"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAppStandbyBucket(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_app_standby_bucket"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_app_standby_bucket",
        state=state
    )
    entity_id = "sensor.s23_joni_app_standby_bucket"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_standby_bucket"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAppImportance(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_app_importance"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_app_importance",
        state=state
    )
    entity_id = "sensor.s23_joni_app_importance"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_app_importance"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniRingerMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_ringer_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_ringer_mode",
        state=state
    )
    entity_id = "sensor.s23_joni_ringer_mode"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_audio_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAudioMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_audio_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_audio_mode",
        state=state
    )
    entity_id = "sensor.s23_joni_audio_mode"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_audio_mode"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniHeadphones(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_headphones"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_headphones",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_headphones"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_headphone_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniMicMuted(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_mic_muted"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_mic_muted",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_mic_muted"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_mic_muted"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniSpeakerphone(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_speakerphone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_speakerphone",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_speakerphone"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_speakerphone_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniMusicActive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_music_active"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_music_active",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_music_active"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_music_active"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_alarm",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_alarm"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_alarm"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelCall(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_call"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_call",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_call"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_call"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelMusic(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_music"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_music",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_music"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_music"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelRinger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_ringer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_ringer",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_ringer"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_ring"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_notification",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_notification"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_notification"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelSystem(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_system"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_system",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_system"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_system"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelDtmf(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_dtmf"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_dtmf",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_dtmf"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_dtmf"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniVolumeLevelAccessibility(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_volume_level_accessibility"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_volume_level_accessibility",
        state=state
    )
    entity_id = "sensor.s23_joni_volume_level_accessibility"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_volume_accessibility"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBatteryLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_battery_level"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'icon': 'mdi:battery-80', 'friendly_name': 's23-joni Battery level', 'last_changed': '2024-08-03T09:35:49.935078+00:00', 'last_updated': '2024-08-03T09:35:49.935078+00:00', 'state_value': 89})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_battery_level",
        state=state
    )
    entity_id = "sensor.s23_joni_battery_level"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_battery_level"
    name = "s23-joni Battery level"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBatteryState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_battery_state"""
        options: list
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['charging', 'discharging', 'full', 'not_charging'], 'device_class': 'enum', 'icon': 'mdi:battery-minus', 'friendly_name': 's23-joni Battery state', 'last_changed': '2024-08-03T05:50:27.488305+00:00', 'last_updated': '2024-08-03T05:50:27.488305+00:00', 'state_value': 'discharging'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_battery_state",
        state=state
    )
    entity_id = "sensor.s23_joni_battery_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_battery_state"
    name = "s23-joni Battery state"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniIsCharging(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_is_charging"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_is_charging",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_is_charging"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_is_charging"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniChargerType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_charger_type"""
        options: list
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['ac', 'usb', 'wireless', 'dock', 'none'], 'device_class': 'enum', 'icon': 'mdi:battery', 'friendly_name': 's23-joni Charger type', 'last_changed': '2024-08-03T05:50:27.489319+00:00', 'last_updated': '2024-08-03T05:50:27.489319+00:00', 'state_value': 'none'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_charger_type",
        state=state
    )
    entity_id = "sensor.s23_joni_charger_type"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_charger_type"
    name = "s23-joni Charger type"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBatteryHealth(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_battery_health"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_battery_health",
        state=state
    )
    entity_id = "sensor.s23_joni_battery_health"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_battery_health"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBatteryTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_battery_temperature"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_battery_temperature",
        state=state
    )
    entity_id = "sensor.s23_joni_battery_temperature"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_battery_temperature"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBatteryPower(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_battery_power"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_battery_power",
        state=state
    )
    entity_id = "sensor.s23_joni_battery_power"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_battery_power"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBluetoothConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_bluetooth_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_bluetooth_connection",
        state=state
    )
    entity_id = "sensor.s23_joni_bluetooth_connection"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_bluetooth_connection"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniBluetoothState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_bluetooth_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_bluetooth_state",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_bluetooth_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_bluetooth_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBleTransmitter(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_ble_transmitter"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_ble_transmitter",
        state=state
    )
    entity_id = "sensor.s23_joni_ble_transmitter"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_ble_emitter"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniBeaconMonitor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_beacon_monitor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_beacon_monitor",
        state=state
    )
    entity_id = "sensor.s23_joni_beacon_monitor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_beacon_monitor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_battery"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_battery",
        state=state
    )
    entity_id = "sensor.s23_joni_car_battery"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_battery"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarName(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_name"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_name",
        state=state
    )
    entity_id = "sensor.s23_joni_car_name"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_name"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarChargingStatus(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_charging_status"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_charging_status",
        state=state
    )
    entity_id = "sensor.s23_joni_car_charging_status"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_charging_status"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarEvConnectorType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_ev_connector_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_ev_connector_type",
        state=state
    )
    entity_id = "sensor.s23_joni_car_ev_connector_type"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_ev_connector"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarFuel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_fuel"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_fuel",
        state=state
    )
    entity_id = "sensor.s23_joni_car_fuel"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_fuel"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarFuelType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_fuel_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_fuel_type",
        state=state
    )
    entity_id = "sensor.s23_joni_car_fuel_type"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_fuel_type"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCarOdometer(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_car_odometer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_car_odometer",
        state=state
    )
    entity_id = "sensor.s23_joni_car_odometer"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_car_odometer"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniScreenBrightness(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_screen_brightness"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_screen_brightness",
        state=state
    )
    entity_id = "sensor.s23_joni_screen_brightness"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_screen_brightness"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniScreenOffTimeout(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_screen_off_timeout"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_screen_off_timeout",
        state=state
    )
    entity_id = "sensor.s23_joni_screen_off_timeout"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_screen_off_timeout"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniDoNotDisturbSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_do_not_disturb_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_do_not_disturb_sensor",
        state=state
    )
    entity_id = "sensor.s23_joni_do_not_disturb_sensor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_dnd_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniAccentColor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_accent_color"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_accent_color",
        state=state
    )
    entity_id = "sensor.s23_joni_accent_color"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_accent_color"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniWorkProfile(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_work_profile"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_work_profile",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_work_profile"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_is_work_profile"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniGeocodedLocation(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_geocoded_location"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_geocoded_location",
        state=state
    )
    entity_id = "sensor.s23_joni_geocoded_location"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_geocoded_location"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniDeviceLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_device_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_device_locked",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_device_locked"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_device_locked"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniDeviceSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_device_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_device_secure",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_device_secure"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_device_secure"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniKeyguardLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_keyguard_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_keyguard_locked",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_keyguard_locked"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_keyguard_locked"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniKeyguardSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_keyguard_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_keyguard_secure",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_keyguard_secure"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_keyguard_secure"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLastUsedApp(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_last_used_app"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_last_used_app",
        state=state
    )
    entity_id = "sensor.s23_joni_last_used_app"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_last_used_app"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLastReboot(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_last_reboot"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_last_reboot",
        state=state
    )
    entity_id = "sensor.s23_joni_last_reboot"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_last_reboot"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLastUpdateTrigger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_last_update_trigger"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_last_update_trigger",
        state=state
    )
    entity_id = "sensor.s23_joni_last_update_trigger"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_last_update"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLightSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_light_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_light_sensor",
        state=state
    )
    entity_id = "sensor.s23_joni_light_sensor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_light_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniHighAccuracyMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_high_accuracy_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_high_accuracy_mode",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_high_accuracy_mode"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_high_accuracy_mode"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniHighAccuracyUpdateInterval(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_high_accuracy_update_interval"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_high_accuracy_update_interval",
        state=state
    )
    entity_id = "sensor.s23_joni_high_accuracy_update_interval"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_high_accuracy_update_interval"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniMobileData(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_mobile_data"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_mobile_data",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_mobile_data"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_mobile_data"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniMobileDataRoaming(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_mobile_data_roaming"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_mobile_data_roaming",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_mobile_data_roaming"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_mobile_data_roaming"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_connection",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_connection"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_connection"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiBssid(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_bssid"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_bssid",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_bssid"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_bssid"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_ip_address",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_ip_address"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_ip_address"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiLinkSpeed(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_link_speed"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_link_speed",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_link_speed"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_link_speed"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniWifiState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_wifi_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_wifi_state",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_wifi_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiFrequency(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_frequency"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_frequency",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_frequency"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_frequency"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniWifiSignalStrength(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_wifi_signal_strength"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_wifi_signal_strength",
        state=state
    )
    entity_id = "sensor.s23_joni_wifi_signal_strength"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_wifi_signal_strength"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniPublicIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_public_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_public_ip_address",
        state=state
    )
    entity_id = "sensor.s23_joni_public_ip_address"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_public_ip_address"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniHotspotState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_hotspot_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_hotspot_state",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_hotspot_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_hotspot_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniNetworkType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_network_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_network_type",
        state=state
    )
    entity_id = "sensor.s23_joni_network_type"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_network_type"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniNfcState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_nfc_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_nfc_state",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_nfc_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_nfc_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniNextAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_next_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_next_alarm",
        state=state
    )
    entity_id = "sensor.s23_joni_next_alarm"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_next_alarm"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLastNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_last_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_last_notification",
        state=state
    )
    entity_id = "sensor.s23_joni_last_notification"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_last_notification"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniLastRemovedNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_last_removed_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_last_removed_notification",
        state=state
    )
    entity_id = "sensor.s23_joni_last_removed_notification"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_last_removed_notification"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniActiveNotificationCount(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_active_notification_count"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_active_notification_count",
        state=state
    )
    entity_id = "sensor.s23_joni_active_notification_count"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_active_notification_count"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniMediaSession(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_media_session"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_media_session",
        state=state
    )
    entity_id = "sensor.s23_joni_media_session"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_media_session"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniPhoneState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_phone_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_phone_state",
        state=state
    )
    entity_id = "sensor.s23_joni_phone_state"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_phone_state"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniSim1(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_sim_1"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_sim_1",
        state=state
    )
    entity_id = "sensor.s23_joni_sim_1"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_sim_1"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniSim2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_sim_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_sim_2",
        state=state
    )
    entity_id = "sensor.s23_joni_sim_2"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_sim_2"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniInteractive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_interactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_interactive",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_interactive"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_is_interactive"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniDozeMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_doze_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_doze_mode",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_doze_mode"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_is_idle"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class BinarySensorS23JoniPowerSave(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_power_save"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_power_save",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_power_save"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_power_save"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniPressureSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_pressure_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_pressure_sensor",
        state=state
    )
    entity_id = "sensor.s23_joni_pressure_sensor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_pressure_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniProximitySensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_proximity_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_proximity_sensor",
        state=state
    )
    entity_id = "sensor.s23_joni_proximity_sensor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_proximity_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniStepsSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_steps_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_steps_sensor",
        state=state
    )
    entity_id = "sensor.s23_joni_steps_sensor"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_steps_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniInternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_internal_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_internal_storage",
        state=state
    )
    entity_id = "sensor.s23_joni_internal_storage"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_storage_sensor"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniExternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_external_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_external_storage",
        state=state
    )
    entity_id = "sensor.s23_joni_external_storage"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_external_storage"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniCurrentTimeZone(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_current_time_zone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_current_time_zone",
        state=state
    )
    entity_id = "sensor.s23_joni_current_time_zone"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_current_time_zone"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniMobileRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_mobile_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_mobile_rx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_mobile_rx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_mobile_rx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniMobileTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_mobile_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_mobile_tx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_mobile_tx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_mobile_tx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniTotalRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_total_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_total_rx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_total_rx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_total_rx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorS23JoniTotalTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_total_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_total_tx_gb",
        state=state
    )
    entity_id = "sensor.s23_joni_total_tx_gb"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_total_tx_gb"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class InputBooleanOfficeClimateAuto(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_boolean.office_climate_auto"""
        editable: bool
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'editable': True, 'icon': 'mdi:air-conditioner', 'friendly_name': 'climate-office-auto', 'last_changed': '2024-07-25T11:38:47.287576+00:00', 'last_updated': '2024-07-25T11:38:47.287576+00:00', 'state_value': 'on'})
    services = my_domains.InputBoolean(
        instance=my_ha_instance,
        entity_id="input_boolean.office_climate_auto",
        state=state
    )
    entity_id = "input_boolean.office_climate_auto"
    unique_id = "office_climate_auto"
    name = "climate-office-auto"
    device_id = "None"


class InputBooleanClimateLivingAuto(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_boolean.climate_living_auto"""
        editable: bool
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'editable': True, 'icon': 'mdi:air-conditioner', 'friendly_name': 'climate-living-auto', 'last_changed': '2024-07-25T11:38:47.289138+00:00', 'last_updated': '2024-07-25T11:38:47.289138+00:00', 'state_value': 'on'})
    services = my_domains.InputBoolean(
        instance=my_ha_instance,
        entity_id="input_boolean.climate_living_auto",
        state=state
    )
    entity_id = "input_boolean.climate_living_auto"
    unique_id = "climate_living_auto"
    name = "climate-living-auto"
    device_id = "None"


class InputNumberAcOfficeConsumption(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_number.ac_office_consumption"""
        initial: typing.Any
        editable: bool
        min: float
        max: float
        step: float
        mode: str
        unit_of_measurement: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'initial': None, 'editable': True, 'min': 0.0, 'max': 99999.0, 'step': 1.0, 'mode': 'box', 'unit_of_measurement': 'Wh', 'icon': 'mdi:lightning-bolt-circle', 'friendly_name': 'ac-office-consumption', 'last_changed': '2024-07-25T11:38:47.026798+00:00', 'last_updated': '2024-07-25T11:38:47.026798+00:00', 'state_value': 0.0})
    services = my_domains.InputNumber(
        instance=my_ha_instance,
        entity_id="input_number.ac_office_consumption",
        state=state
    )
    entity_id = "input_number.ac_office_consumption"
    unique_id = "ac_office_consumption"
    name = "ac-office-consumption"
    device_id = "None"


class InputNumberAcLivingConsumption(models.Entity):

    class _StateClass(models.State):
        """State class for entity input_number.ac_living_consumption"""
        initial: typing.Any
        editable: bool
        min: float
        max: float
        step: float
        mode: str
        unit_of_measurement: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'initial': None, 'editable': True, 'min': 0.0, 'max': 99999.0, 'step': 1.0, 'mode': 'box', 'unit_of_measurement': 'Wh', 'icon': 'mdi:lightning-bolt-circle', 'friendly_name': 'ac-living-consumption', 'last_changed': '2024-07-25T11:38:47.029893+00:00', 'last_updated': '2024-07-25T11:38:47.029893+00:00', 'state_value': 0.0})
    services = my_domains.InputNumber(
        instance=my_ha_instance,
        entity_id="input_number.ac_living_consumption",
        state=state
    )
    entity_id = "input_number.ac_living_consumption"
    unique_id = "ac_living_consumption"
    name = "ac-living-consumption"
    device_id = "None"


class SensorSonoff01minizbRssi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sonoff_01minizb_rssi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sonoff_01minizb_rssi_2",
        state=state
    )
    entity_id = "sensor.sonoff_01minizb_rssi_2"
    unique_id = "00:12:4b:00:26:b7:9e:61-1-0-rssi"
    name = "None"
    device_id = "333c1e8842daae9b3c64744acec3c123"


class SensorSonoff01minizbLqi2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.sonoff_01minizb_lqi_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.sonoff_01minizb_lqi_2",
        state=state
    )
    entity_id = "sensor.sonoff_01minizb_lqi_2"
    unique_id = "00:12:4b:00:26:b7:9e:61-1-0-lqi"
    name = "None"
    device_id = "333c1e8842daae9b3c64744acec3c123"


class UpdateOfficePrinterSwitchFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.office_printer_switch_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00002000', 'in_progress': False, 'latest_version': '0x00002000', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'office-printer-switch Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.027457+00:00', 'last_updated': '2024-07-27T14:55:31.027457+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.office_printer_switch_firmware",
        state=state
    )
    entity_id = "update.office_printer_switch_firmware"
    unique_id = "00:12:4b:00:26:b7:9e:61-1-25-firmware_update"
    name = "office-printer-switch Firmware"
    device_id = "333c1e8842daae9b3c64744acec3c123"


class ButtonOfficePrinterSwitchIdentify(models.Entity):

    class _StateClass(models.State):
        """State class for entity button.office_printer_switch_identify"""
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'device_class': 'identify', 'friendly_name': 'office-printer-switch Identify', 'last_changed': '2024-07-27T14:55:29.967214+00:00', 'last_updated': '2024-07-27T14:55:29.967214+00:00', 'state_value': 'unknown'})
    services = my_domains.Button(
        instance=my_ha_instance,
        entity_id="button.office_printer_switch_identify",
        state=state
    )
    entity_id = "button.office_printer_switch_identify"
    unique_id = "00:12:4b:00:26:b7:9e:61-1-3"
    name = "office-printer-switch Identify"
    device_id = "333c1e8842daae9b3c64744acec3c123"


class LightOfficePrinterSwitchLight(models.Entity):

    class _StateClass(models.State):
        """State class for entity light.office_printer_switch_light"""
        supported_color_modes: list
        color_mode: str
        off_with_transition: bool
        off_brightness: typing.Any
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'supported_color_modes': ['onoff'], 'color_mode': 'onoff', 'off_with_transition': False, 'off_brightness': None, 'friendly_name': 'office-printer-switch Light', 'supported_features': 8, 'last_changed': '2024-07-27T14:55:30.122971+00:00', 'last_updated': '2024-07-27T14:55:30.122971+00:00', 'state_value': 'on'})
    services = my_domains.Light(
        instance=my_ha_instance,
        entity_id="light.office_printer_switch_light",
        state=state
    )
    entity_id = "light.office_printer_switch_light"
    unique_id = "00:12:4b:00:26:b7:9e:61-1"
    name = "office-printer-switch Light"
    device_id = "333c1e8842daae9b3c64744acec3c123"


class SensorS23JoniIpv6Addresses(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_ipv6_addresses"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_ipv6_addresses",
        state=state
    )
    entity_id = "sensor.s23_joni_ipv6_addresses"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_ip6_addresses"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorMi9ClauIpv6Addresses(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.mi9_clau_ipv6_addresses"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.mi9_clau_ipv6_addresses",
        state=state
    )
    entity_id = "sensor.mi9_clau_ipv6_addresses"
    unique_id = "30eeb9f227f3ea857dfaf3c57c9f4bcc595d0e5988fc7c0e3f608a8876aa18e0_ip6_addresses"
    name = "None"
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"


class BinarySensorS23JoniWifi(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.s23_joni_wifi"""
        round_trip_time_avg: float
        round_trip_time_max: float
        round_trip_time_mdev: str
        round_trip_time_min: float
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'round_trip_time_avg': 187.362, 'round_trip_time_max': 272.868, 'round_trip_time_mdev': '', 'round_trip_time_min': 120.862, 'device_class': 'connectivity', 'friendly_name': 's23-joni-wifi', 'last_changed': '2024-08-03T07:42:29.742909+00:00', 'last_updated': '2024-08-03T10:40:11.638223+00:00', 'state_value': 'on'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.s23_joni_wifi",
        state=state
    )
    entity_id = "binary_sensor.s23_joni_wifi"
    unique_id = "f444744715edca874cb84bc1cc00233c"
    name = "s23-joni-wifi"
    device_id = "None"


class DeviceTrackerS23JoniWifi(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.s23_joni_wifi"""
        source_type: str
        ip: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'router', 'ip': '192.168.1.52', 'friendly_name': 's23-joni-wifi', 'last_changed': '2024-08-03T07:42:29.743446+00:00', 'last_updated': '2024-08-03T07:42:29.743446+00:00', 'state_value': 'home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.s23_joni_wifi",
        state=state
    )
    entity_id = "device_tracker.s23_joni_wifi"
    unique_id = "f444744715edca874cb84bc1cc00233c"
    name = "s23-joni-wifi"
    device_id = "None"


class DeviceTrackerPixelClau(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.pixel_clau"""
        source_type: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'gps', 'friendly_name': 'pixel-clau', 'last_changed': '2024-07-25T11:39:10.280066+00:00', 'last_updated': '2024-07-25T11:39:10.280066+00:00', 'state_value': 'unknown'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.pixel_clau",
        state=state
    )
    entity_id = "device_tracker.pixel_clau"
    unique_id = "2d8d920ee7872523"
    name = "pixel-clau"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauDetectedActivity(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_detected_activity"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_detected_activity",
        state=state
    )
    entity_id = "sensor.pixel_clau_detected_activity"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_detected_activity"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauSleepConfidence(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_sleep_confidence"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_sleep_confidence",
        state=state
    )
    entity_id = "sensor.pixel_clau_sleep_confidence"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_sleep_confidence"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauSleepSegment(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_sleep_segment"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_sleep_segment",
        state=state
    )
    entity_id = "sensor.pixel_clau_sleep_segment"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_sleep_segment"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauAndroidAuto(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_android_auto"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_android_auto",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_android_auto"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_android_auto"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauOsVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_os_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_os_version",
        state=state
    )
    entity_id = "sensor.pixel_clau_os_version"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_android_os_version"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauSecurityPatch(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_security_patch"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_security_patch",
        state=state
    )
    entity_id = "sensor.pixel_clau_security_patch"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_android_os_security_patch"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCurrentVersion(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_current_version"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_current_version",
        state=state
    )
    entity_id = "sensor.pixel_clau_current_version"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_current_version"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAppRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_app_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_app_rx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_app_rx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_rx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAppTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_app_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_app_tx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_app_tx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_tx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAppMemory(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_app_memory"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_app_memory",
        state=state
    )
    entity_id = "sensor.pixel_clau_app_memory"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_memory"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauAppInactive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_app_inactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_app_inactive",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_app_inactive"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_inactive"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAppStandbyBucket(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_app_standby_bucket"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_app_standby_bucket",
        state=state
    )
    entity_id = "sensor.pixel_clau_app_standby_bucket"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_standby_bucket"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAppImportance(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_app_importance"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_app_importance",
        state=state
    )
    entity_id = "sensor.pixel_clau_app_importance"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_app_importance"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauRingerMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_ringer_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_ringer_mode",
        state=state
    )
    entity_id = "sensor.pixel_clau_ringer_mode"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_audio_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAudioMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_audio_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_audio_mode",
        state=state
    )
    entity_id = "sensor.pixel_clau_audio_mode"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_audio_mode"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauHeadphones(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_headphones"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_headphones",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_headphones"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_headphone_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauMicMuted(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_mic_muted"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_mic_muted",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_mic_muted"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_mic_muted"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauSpeakerphone(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_speakerphone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_speakerphone",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_speakerphone"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_speakerphone_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauMusicActive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_music_active"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_music_active",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_music_active"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_music_active"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_alarm",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_alarm"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_alarm"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelCall(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_call"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_call",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_call"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_call"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelMusic(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_music"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_music",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_music"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_music"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelRinger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_ringer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_ringer",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_ringer"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_ring"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_notification",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_notification"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_notification"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelSystem(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_system"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_system",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_system"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_system"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelDtmf(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_dtmf"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_dtmf",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_dtmf"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_dtmf"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauVolumeLevelAccessibility(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_volume_level_accessibility"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_volume_level_accessibility",
        state=state
    )
    entity_id = "sensor.pixel_clau_volume_level_accessibility"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_volume_accessibility"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBatteryLevel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_battery_level"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'icon': 'mdi:battery-50', 'friendly_name': 'pixel-clau Battery level', 'last_changed': '2024-08-03T10:39:20.143440+00:00', 'last_updated': '2024-08-03T10:39:20.143440+00:00', 'state_value': 58})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_battery_level",
        state=state
    )
    entity_id = "sensor.pixel_clau_battery_level"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_battery_level"
    name = "pixel-clau Battery level"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBatteryState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_battery_state"""
        options: list
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['charging', 'discharging', 'full', 'not_charging'], 'device_class': 'enum', 'icon': 'mdi:battery-minus', 'friendly_name': 'pixel-clau Battery state', 'last_changed': '2024-08-03T08:29:25.353520+00:00', 'last_updated': '2024-08-03T08:29:25.353520+00:00', 'state_value': 'discharging'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_battery_state",
        state=state
    )
    entity_id = "sensor.pixel_clau_battery_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_battery_state"
    name = "pixel-clau Battery state"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauIsCharging(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_is_charging"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_is_charging",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_is_charging"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_is_charging"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauChargerType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_charger_type"""
        options: list
        device_class: str
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'options': ['ac', 'usb', 'wireless', 'dock', 'none'], 'device_class': 'enum', 'icon': 'mdi:battery', 'friendly_name': 'pixel-clau Charger type', 'last_changed': '2024-08-03T08:29:25.354686+00:00', 'last_updated': '2024-08-03T08:29:25.354686+00:00', 'state_value': 'none'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_charger_type",
        state=state
    )
    entity_id = "sensor.pixel_clau_charger_type"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_charger_type"
    name = "pixel-clau Charger type"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBatteryHealth(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_battery_health"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_battery_health",
        state=state
    )
    entity_id = "sensor.pixel_clau_battery_health"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_battery_health"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBatteryTemperature(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_battery_temperature"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_battery_temperature",
        state=state
    )
    entity_id = "sensor.pixel_clau_battery_temperature"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_battery_temperature"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBatteryPower(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_battery_power"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_battery_power",
        state=state
    )
    entity_id = "sensor.pixel_clau_battery_power"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_battery_power"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBluetoothConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_bluetooth_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_bluetooth_connection",
        state=state
    )
    entity_id = "sensor.pixel_clau_bluetooth_connection"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_bluetooth_connection"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauBluetoothState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_bluetooth_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_bluetooth_state",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_bluetooth_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_bluetooth_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBleTransmitter(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_ble_transmitter"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_ble_transmitter",
        state=state
    )
    entity_id = "sensor.pixel_clau_ble_transmitter"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_ble_emitter"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauBeaconMonitor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_beacon_monitor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_beacon_monitor",
        state=state
    )
    entity_id = "sensor.pixel_clau_beacon_monitor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_beacon_monitor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_battery"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_battery",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_battery"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_battery"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarName(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_name"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_name",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_name"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_name"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarChargingStatus(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_charging_status"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_charging_status",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_charging_status"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_charging_status"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarEvConnectorType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_ev_connector_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_ev_connector_type",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_ev_connector_type"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_ev_connector"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarFuel(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_fuel"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_fuel",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_fuel"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_fuel"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarFuelType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_fuel_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_fuel_type",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_fuel_type"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_fuel_type"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCarOdometer(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_car_odometer"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_car_odometer",
        state=state
    )
    entity_id = "sensor.pixel_clau_car_odometer"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_car_odometer"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauScreenBrightness(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_screen_brightness"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_screen_brightness",
        state=state
    )
    entity_id = "sensor.pixel_clau_screen_brightness"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_screen_brightness"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauScreenOffTimeout(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_screen_off_timeout"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_screen_off_timeout",
        state=state
    )
    entity_id = "sensor.pixel_clau_screen_off_timeout"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_screen_off_timeout"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauDoNotDisturbSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_do_not_disturb_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_do_not_disturb_sensor",
        state=state
    )
    entity_id = "sensor.pixel_clau_do_not_disturb_sensor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_dnd_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauAccentColor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_accent_color"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_accent_color",
        state=state
    )
    entity_id = "sensor.pixel_clau_accent_color"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_accent_color"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauWorkProfile(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_work_profile"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_work_profile",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_work_profile"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_is_work_profile"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauGeocodedLocation(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_geocoded_location"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_geocoded_location",
        state=state
    )
    entity_id = "sensor.pixel_clau_geocoded_location"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_geocoded_location"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauDeviceLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_device_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_device_locked",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_device_locked"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_device_locked"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauDeviceSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_device_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_device_secure",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_device_secure"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_device_secure"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauKeyguardLocked(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_keyguard_locked"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_keyguard_locked",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_keyguard_locked"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_keyguard_locked"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauKeyguardSecure(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_keyguard_secure"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_keyguard_secure",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_keyguard_secure"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_keyguard_secure"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLastUsedApp(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_last_used_app"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_last_used_app",
        state=state
    )
    entity_id = "sensor.pixel_clau_last_used_app"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_last_used_app"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLastReboot(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_last_reboot"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_last_reboot",
        state=state
    )
    entity_id = "sensor.pixel_clau_last_reboot"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_last_reboot"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLastUpdateTrigger(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_last_update_trigger"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_last_update_trigger",
        state=state
    )
    entity_id = "sensor.pixel_clau_last_update_trigger"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_last_update"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLightSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_light_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_light_sensor",
        state=state
    )
    entity_id = "sensor.pixel_clau_light_sensor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_light_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauHighAccuracyMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_high_accuracy_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_high_accuracy_mode",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_high_accuracy_mode"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_high_accuracy_mode"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauHighAccuracyUpdateInterval(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_high_accuracy_update_interval"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_high_accuracy_update_interval",
        state=state
    )
    entity_id = "sensor.pixel_clau_high_accuracy_update_interval"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_high_accuracy_update_interval"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauMobileData(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_mobile_data"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_mobile_data",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_mobile_data"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_mobile_data"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauMobileDataRoaming(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_mobile_data_roaming"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_mobile_data_roaming",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_mobile_data_roaming"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_mobile_data_roaming"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiConnection(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_connection"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_connection",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_connection"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_connection"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiBssid(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_bssid"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_bssid",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_bssid"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_bssid"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_ip_address",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_ip_address"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_ip_address"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiLinkSpeed(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_link_speed"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_link_speed",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_link_speed"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_link_speed"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauWifiState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_wifi_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_wifi_state",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_wifi_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiFrequency(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_frequency"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_frequency",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_frequency"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_frequency"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauWifiSignalStrength(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_wifi_signal_strength"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_wifi_signal_strength",
        state=state
    )
    entity_id = "sensor.pixel_clau_wifi_signal_strength"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_wifi_signal_strength"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauPublicIpAddress(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_public_ip_address"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_public_ip_address",
        state=state
    )
    entity_id = "sensor.pixel_clau_public_ip_address"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_public_ip_address"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauHotspotState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_hotspot_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_hotspot_state",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_hotspot_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_hotspot_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauNetworkType(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_network_type"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_network_type",
        state=state
    )
    entity_id = "sensor.pixel_clau_network_type"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_network_type"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauIpv6Addresses(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_ipv6_addresses"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_ipv6_addresses",
        state=state
    )
    entity_id = "sensor.pixel_clau_ipv6_addresses"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_ip6_addresses"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauNfcState(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_nfc_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_nfc_state",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_nfc_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_nfc_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauNextAlarm(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_next_alarm"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_next_alarm",
        state=state
    )
    entity_id = "sensor.pixel_clau_next_alarm"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_next_alarm"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLastNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_last_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_last_notification",
        state=state
    )
    entity_id = "sensor.pixel_clau_last_notification"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_last_notification"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauLastRemovedNotification(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_last_removed_notification"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_last_removed_notification",
        state=state
    )
    entity_id = "sensor.pixel_clau_last_removed_notification"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_last_removed_notification"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauActiveNotificationCount(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_active_notification_count"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_active_notification_count",
        state=state
    )
    entity_id = "sensor.pixel_clau_active_notification_count"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_active_notification_count"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauMediaSession(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_media_session"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_media_session",
        state=state
    )
    entity_id = "sensor.pixel_clau_media_session"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_media_session"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauPhoneState(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_phone_state"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_phone_state",
        state=state
    )
    entity_id = "sensor.pixel_clau_phone_state"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_phone_state"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauSim1(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_sim_1"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_sim_1",
        state=state
    )
    entity_id = "sensor.pixel_clau_sim_1"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_sim_1"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauSim2(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_sim_2"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_sim_2",
        state=state
    )
    entity_id = "sensor.pixel_clau_sim_2"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_sim_2"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauInteractive(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_interactive"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_interactive",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_interactive"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_is_interactive"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauDozeMode(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_doze_mode"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_doze_mode",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_doze_mode"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_is_idle"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensorPixelClauPowerSave(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.pixel_clau_power_save"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.pixel_clau_power_save",
        state=state
    )
    entity_id = "binary_sensor.pixel_clau_power_save"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_power_save"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauPressureSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_pressure_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_pressure_sensor",
        state=state
    )
    entity_id = "sensor.pixel_clau_pressure_sensor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_pressure_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauProximitySensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_proximity_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_proximity_sensor",
        state=state
    )
    entity_id = "sensor.pixel_clau_proximity_sensor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_proximity_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauStepsSensor(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_steps_sensor"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_steps_sensor",
        state=state
    )
    entity_id = "sensor.pixel_clau_steps_sensor"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_steps_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauInternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_internal_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_internal_storage",
        state=state
    )
    entity_id = "sensor.pixel_clau_internal_storage"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_storage_sensor"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauExternalStorage(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_external_storage"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_external_storage",
        state=state
    )
    entity_id = "sensor.pixel_clau_external_storage"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_external_storage"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauCurrentTimeZone(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_current_time_zone"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_current_time_zone",
        state=state
    )
    entity_id = "sensor.pixel_clau_current_time_zone"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_current_time_zone"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauMobileRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_mobile_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_mobile_rx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_mobile_rx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_mobile_rx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauMobileTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_mobile_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_mobile_tx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_mobile_tx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_mobile_tx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauTotalRxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_total_rx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_total_rx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_total_rx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_total_rx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SensorPixelClauTotalTxGb(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_total_tx_gb"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_total_tx_gb",
        state=state
    )
    entity_id = "sensor.pixel_clau_total_tx_gb"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_total_tx_gb"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class BinarySensor192168159(models.Entity):

    class _StateClass(models.State):
        """State class for entity binary_sensor.192_168_1_59"""
        round_trip_time_avg: float
        round_trip_time_max: float
        round_trip_time_mdev: str
        round_trip_time_min: float
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'round_trip_time_avg': 86.158, 'round_trip_time_max': 126.146, 'round_trip_time_mdev': '', 'round_trip_time_min': 7.471, 'device_class': 'connectivity', 'friendly_name': 'pixel-clau-wifi', 'last_changed': '2024-08-03T00:31:43.537631+00:00', 'last_updated': '2024-08-03T10:40:09.017543+00:00', 'state_value': 'on'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="binary_sensor.192_168_1_59",
        state=state
    )
    entity_id = "binary_sensor.192_168_1_59"
    unique_id = "8a65d6f7175d7e58734d9cdcdfb9ccff"
    name = "pixel-clau-wifi"
    device_id = "None"


class DeviceTracker192168159(models.Entity):

    class _StateClass(models.State):
        """State class for entity device_tracker.192_168_1_59"""
        source_type: str
        ip: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'source_type': 'router', 'ip': '192.168.1.59', 'friendly_name': 'pixel-clau-wifi', 'last_changed': '2024-08-03T00:31:43.538240+00:00', 'last_updated': '2024-08-03T00:31:43.538240+00:00', 'state_value': 'home'})
    services = my_domains.DeviceTracker(
        instance=my_ha_instance,
        entity_id="device_tracker.192_168_1_59",
        state=state
    )
    entity_id = "device_tracker.192_168_1_59"
    unique_id = "8a65d6f7175d7e58734d9cdcdfb9ccff"
    name = "pixel-clau-wifi"
    device_id = "None"


class RemoteOfficeIrControl(models.Entity):

    class _StateClass(models.State):
        """State class for entity remote.office_ir_control"""
        restored: bool
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'supported_features': 3, 'last_changed': '2024-07-25T11:39:37.438787+00:00', 'last_updated': '2024-07-25T11:39:37.438787+00:00', 'state_value': 'unavailable'})
    services = my_domains.Remote(
        instance=my_ha_instance,
        entity_id="remote.office_ir_control",
        state=state
    )
    entity_id = "remote.office_ir_control"
    unique_id = "e81656a1aa29"
    name = "None"
    device_id = "bb08ffc8c23b4b1aae35d9ec7ce83b64"


class ClimateOfficeAcIr(models.Entity):

    class _StateClass(models.State):
        """State class for entity climate.office_ac_ir"""
        hvac_modes: list
        min_temp: float
        max_temp: float
        target_temp_step: float
        fan_modes: list
        current_temperature: float
        temperature: int
        current_humidity: float
        fan_mode: str
        last_on_operation: str
        device_code: int
        manufacturer: str
        supported_models: list
        supported_controller: str
        commands_encoding: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'hvac_modes': ['off', 'heat', 'cool', 'fan_only', 'dry'], 'min_temp': 16.0, 'max_temp': 30.0, 'target_temp_step': 1.0, 'fan_modes': ['low', 'min', 'mid', 'high', 'max', 'auto'], 'current_temperature': 27.2, 'temperature': 23, 'current_humidity': 44.3, 'fan_mode': 'mid', 'last_on_operation': 'heat', 'device_code': 1522, 'manufacturer': 'Hisense', 'supported_models': ['DGR11R2'], 'supported_controller': 'Broadlink', 'commands_encoding': 'Base64', 'friendly_name': 'office-ac-ir', 'supported_features': 393, 'last_changed': '2024-07-25T11:38:43.875425+00:00', 'last_updated': '2024-08-03T10:32:53.729158+00:00', 'state_value': 'heat'})
    services = my_domains.Climate(
        instance=my_ha_instance,
        entity_id="climate.office_ac_ir",
        state=state
    )
    entity_id = "climate.office_ac_ir"
    unique_id = "office_ac_ir"
    name = "office-ac-ir"
    device_id = "None"


class ClimateOfficeAcIr4(models.Entity):

    class _StateClass(models.State):
        """State class for entity climate.office_ac_ir_4"""
        restored: bool
        hvac_modes: list
        min_temp: int
        max_temp: int
        target_temp_step: int
        fan_modes: list
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'hvac_modes': ['off', 'cool', 'heat', 'dry', 'fan_only'], 'min_temp': 16, 'max_temp': 30, 'target_temp_step': 1, 'fan_modes': ['auto', 'low', 'mid', 'max'], 'friendly_name': 'office-ac-ir-4', 'supported_features': 393, 'last_changed': '2024-07-25T11:39:37.439152+00:00', 'last_updated': '2024-07-25T11:39:37.439152+00:00', 'state_value': 'unavailable'})
    services = my_domains.Climate(
        instance=my_ha_instance,
        entity_id="climate.office_ac_ir_4",
        state=state
    )
    entity_id = "climate.office_ac_ir_4"
    unique_id = "office_ac_ir_4"
    name = "office-ac-ir-4"
    device_id = "None"


class ClimateOfficeAcIr2(models.Entity):

    class _StateClass(models.State):
        """State class for entity climate.office_ac_ir_2"""
        restored: bool
        hvac_modes: list
        min_temp: float
        max_temp: float
        target_temp_step: float
        fan_modes: list
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'hvac_modes': ['off', 'cool', 'heat'], 'min_temp': 18.0, 'max_temp': 32.0, 'target_temp_step': 1.0, 'fan_modes': ['auto', 'low', 'medium', 'high'], 'friendly_name': 'office-ac-ir-2', 'supported_features': 393, 'last_changed': '2024-07-25T11:39:37.439471+00:00', 'last_updated': '2024-07-25T11:39:37.439471+00:00', 'state_value': 'unavailable'})
    services = my_domains.Climate(
        instance=my_ha_instance,
        entity_id="climate.office_ac_ir_2",
        state=state
    )
    entity_id = "climate.office_ac_ir_2"
    unique_id = "office_ac_ir_2"
    name = "office-ac-ir-2"
    device_id = "None"


class ClimateOfficeAcIr3(models.Entity):

    class _StateClass(models.State):
        """State class for entity climate.office_ac_ir_3"""
        restored: bool
        hvac_modes: list
        min_temp: float
        max_temp: float
        target_temp_step: float
        fan_modes: list
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'restored': True, 'hvac_modes': ['off', 'heat', 'cool', 'fan_only', 'dry'], 'min_temp': 16.0, 'max_temp': 30.0, 'target_temp_step': 1.0, 'fan_modes': ['low', 'min', 'mid', 'high', 'max', 'auto'], 'friendly_name': 'office-ac-ir-3', 'supported_features': 393, 'last_changed': '2024-07-25T11:39:37.439810+00:00', 'last_updated': '2024-07-25T11:39:37.439810+00:00', 'state_value': 'unavailable'})
    services = my_domains.Climate(
        instance=my_ha_instance,
        entity_id="climate.office_ac_ir_3",
        state=state
    )
    entity_id = "climate.office_ac_ir_3"
    unique_id = "office_ac_ir_3"
    name = "office-ac-ir-3"
    device_id = "None"


class SensorTze200A7sghmmsTs0601Rssi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tze200_a7sghmms_ts0601_rssi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tze200_a7sghmms_ts0601_rssi",
        state=state
    )
    entity_id = "sensor.tze200_a7sghmms_ts0601_rssi"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-0-rssi"
    name = "None"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class SensorTze200A7sghmmsTs0601Lqi(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.tze200_a7sghmms_ts0601_lqi"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.tze200_a7sghmms_ts0601_lqi",
        state=state
    )
    entity_id = "sensor.tze200_a7sghmms_ts0601_lqi"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-0-lqi"
    name = "None"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class SensorTerraceSmartValveBattery(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terrace_smart_valve_battery"""
        state_class: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'unit_of_measurement': '%', 'device_class': 'battery', 'friendly_name': 'terrace-smart-valve Battery', 'last_changed': '2024-08-01T18:35:59.726038+00:00', 'last_updated': '2024-08-01T18:35:59.726038+00:00', 'state_value': 60})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terrace_smart_valve_battery",
        state=state
    )
    entity_id = "sensor.terrace_smart_valve_battery"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-1"
    name = "terrace-smart-valve Battery"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class UpdateTerraceSmartValveFirmware(models.Entity):

    class _StateClass(models.State):
        """State class for entity update.terrace_smart_valve_firmware"""
        auto_update: bool
        installed_version: str
        in_progress: bool
        latest_version: str
        release_summary: typing.Any
        release_url: typing.Any
        skipped_version: typing.Any
        title: typing.Any
        device_class: str
        entity_picture: str
        friendly_name: str
        supported_features: int
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'auto_update': False, 'installed_version': '0x00000048', 'in_progress': False, 'latest_version': '0x00000048', 'release_summary': None, 'release_url': None, 'skipped_version': None, 'title': None, 'device_class': 'firmware', 'entity_picture': 'https://brands.home-assistant.io/_/zha/icon.png', 'friendly_name': 'terrace-smart-valve Firmware', 'supported_features': 7, 'last_changed': '2024-07-27T14:55:31.033990+00:00', 'last_updated': '2024-07-27T14:55:31.033990+00:00', 'state_value': 'off'})
    services = my_domains.Update(
        instance=my_ha_instance,
        entity_id="update.terrace_smart_valve_firmware",
        state=state
    )
    entity_id = "update.terrace_smart_valve_firmware"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-25-firmware_update"
    name = "terrace-smart-valve Firmware"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class SwitchTerraceSmartValveSwitch(models.Entity):

    class _StateClass(models.State):
        """State class for entity switch.terrace_smart_valve_switch"""
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'friendly_name': 'terrace-smart-valve Switch', 'last_changed': '2024-08-03T06:39:00.320778+00:00', 'last_updated': '2024-08-03T06:39:00.320778+00:00', 'state_value': 'off'})
    services = my_domains.Switch(
        instance=my_ha_instance,
        entity_id="switch.terrace_smart_valve_switch",
        state=state
    )
    entity_id = "switch.terrace_smart_valve_switch"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-6"
    name = "terrace-smart-valve Switch"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class SensorTerraceSmartValveInstantaneousDemand(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terrace_smart_valve_instantaneous_demand"""
        state_class: str
        device_type: str
        unit_of_measurement: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'measurement', 'device_type': 'Water Metering', 'unit_of_measurement': 'l/h', 'friendly_name': 'terrace-smart-valve Instantaneous demand', 'last_changed': '2024-07-27T14:55:30.868893+00:00', 'last_updated': '2024-07-27T14:55:30.868893+00:00', 'state_value': 'unknown'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terrace_smart_valve_instantaneous_demand",
        state=state
    )
    entity_id = "sensor.terrace_smart_valve_instantaneous_demand"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-1794"
    name = "terrace-smart-valve Instantaneous demand"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class SensorTerraceSmartValveSummationDelivered(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.terrace_smart_valve_summation_delivered"""
        state_class: str
        device_type: str
        unit_of_measurement: str
        device_class: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: float
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'state_class': 'total_increasing', 'device_type': 'Water Metering', 'unit_of_measurement': 'L', 'device_class': 'volume', 'friendly_name': 'terrace-smart-valve Summation delivered', 'last_changed': '2024-08-01T18:35:01.823702+00:00', 'last_updated': '2024-08-01T18:35:01.823702+00:00', 'state_value': 0.0})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.terrace_smart_valve_summation_delivered",
        state=state
    )
    entity_id = "sensor.terrace_smart_valve_summation_delivered"
    unique_id = "a4:c1:38:1b:74:7a:f5:f8-1-1794-summation_delivered"
    name = "terrace-smart-valve Summation delivered"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"


class AutomationRiegoDeManana(models.Entity):

    class _StateClass(models.State):
        """State class for entity automation.riego_de_manana"""
        id: str
        last_triggered: str
        mode: str
        current: int
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'id': '1717710557975', 'last_triggered': '2024-08-03T06:35:00.279364+00:00', 'mode': 'single', 'current': 0, 'friendly_name': 'riego-de-mañana', 'last_changed': '2024-07-25T11:38:45.682960+00:00', 'last_updated': '2024-08-03T06:39:00.330490+00:00', 'state_value': 'on'})
    services = my_domains.Automation(
        instance=my_ha_instance,
        entity_id="automation.riego_de_manana",
        state=state
    )
    entity_id = "automation.riego_de_manana"
    unique_id = "1717710557975"
    name = "riego-de-mañana"
    device_id = "None"


class SensorS23JoniRemainingChargeTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.s23_joni_remaining_charge_time"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.s23_joni_remaining_charge_time",
        state=state
    )
    entity_id = "sensor.s23_joni_remaining_charge_time"
    unique_id = "329014cd2b821caa7b7be95071d9085f2d0427d43e1392ca58a13b2f10277250_remaining_charge_time"
    name = "None"
    device_id = "86116456e47329aee683359d5dde4d65"


class SensorPixelClauRemainingChargeTime(models.Entity):

    class _StateClass(models.State):
        """State class for entity sensor.pixel_clau_remaining_charge_time"""
        last_changed: typing.Any
        last_updated: typing.Any
        state_value: typing.Any
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'last_changed': None, 'last_updated': None, 'state_value': None})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sensor.pixel_clau_remaining_charge_time",
        state=state
    )
    entity_id = "sensor.pixel_clau_remaining_charge_time"
    unique_id = "a5198828d171b6d374fba7a6439cb8ec7e37a90bd9e5a3206b69cb6e56ec8bf6_remaining_charge_time"
    name = "None"
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"


class SunSun(models.Entity):

    class _StateClass(models.State):
        """State class for entity sun.sun"""
        next_dawn: str
        next_dusk: str
        next_midnight: str
        next_noon: str
        next_rising: str
        next_setting: str
        elevation: float
        azimuth: float
        rising: bool
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: str
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'next_dawn': '2024-08-04T04:15:46.947633+00:00', 'next_dusk': '2024-08-03T19:39:38.227707+00:00', 'next_midnight': '2024-08-03T23:57:27+00:00', 'next_noon': '2024-08-03T11:57:34+00:00', 'next_rising': '2024-08-04T04:47:37.285863+00:00', 'next_setting': '2024-08-03T19:07:48.891788+00:00', 'elevation': 60.6, 'azimuth': 139.22, 'rising': True, 'friendly_name': 'Sun', 'last_changed': '2024-08-03T04:48:37.358212+00:00', 'last_updated': '2024-08-03T10:39:02.127239+00:00', 'state_value': 'above_horizon'})
    services = models.Domain(
        instance=my_ha_instance,
        entity_id="sun.sun",
        state=state
    )
    entity_id = "sun.sun"
    unique_id = "None"
    name = "Sun"
    device_id = "None"


class ZoneHome(models.Entity):

    class _StateClass(models.State):
        """State class for entity zone.home"""
        latitude: float
        longitude: float
        radius: int
        passive: bool
        persons: list
        editable: bool
        icon: str
        friendly_name: str
        last_changed: str
        last_updated: str
        state_value: int
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    state = _StateClass(**{'latitude': 41.42194116407516, 'longitude': 2.1571397781372075, 'radius': 300, 'passive': False, 'persons': ['person.claudia', 'person.joni'], 'editable': True, 'icon': 'mdi:home', 'friendly_name': 'Casa', 'last_changed': '2024-08-03T07:42:29.744974+00:00', 'last_updated': '2024-08-03T07:42:29.744974+00:00', 'state_value': 2})
    services = my_domains.Zone(
        instance=my_ha_instance,
        entity_id="zone.home",
        state=state
    )
    entity_id = "zone.home"
    unique_id = "None"
    name = "Casa"
    device_id = "None"
