
import hapy.models as models
import hapy.generators.devices as gen_devices
import entities as my_entities


class HomeAssistantCore_0b(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "bac32c0a9033740e54fe621b88d7220b"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        update_home_assistant_core_update = my_entities.UpdateHomeAssistantCoreUpdate
        sensor_home_assistant_core_cpu_percent = my_entities.SensorHomeAssistantCoreCpuPercent
        sensor_home_assistant_core_memory_percent = my_entities.SensorHomeAssistantCoreMemoryPercent




class HomeAssistantSupervisor_d6(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "d01ab98c93f7e94e7a0f1c31100cc8d6"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        update_home_assistant_supervisor_update = my_entities.UpdateHomeAssistantSupervisorUpdate
        sensor_home_assistant_supervisor_cpu_percent = my_entities.SensorHomeAssistantSupervisorCpuPercent
        sensor_home_assistant_supervisor_memory_percent = my_entities.SensorHomeAssistantSupervisorMemoryPercent




class HomeAssistantOperatingSystem_6d(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "1d62450fe5a2c4adc07ab8a4207f276d"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        update_home_assistant_operating_system_update = my_entities.UpdateHomeAssistantOperatingSystemUpdate
        sensor_home_assistant_operating_system_version = my_entities.SensorHomeAssistantOperatingSystemVersion
        sensor_home_assistant_operating_system_newest_version = my_entities.SensorHomeAssistantOperatingSystemNewestVersion




class Hci0xb8x27xebx13x28x92x_b7(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "c4f1271b31a51d28ed7fd1016eb859b7"
    unique_id = "None"
    
    class entities:
        """Device entities"""





class TexasInstrumentsCoordinator_b9(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "a0538bfb15ee03e0ea1ef75b8faf09b9"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_texas_instruments_coordinator = my_entities.SensorTexasInstrumentsCoordinator




class LivingDownLight01_80(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "5faab9fdb078d8eb9823828e963d4880"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_9 = my_entities.SensorInnrRs230CRssi9
        sensor_innr_rs_230_c_lqi_9 = my_entities.SensorInnrRs230CLqi9
        button_living_down_light_01_identifybutton_9 = my_entities.ButtonLivingDownLight01Identifybutton9
        light_living_down_light_01 = my_entities.LightLivingDownLight01
        number_living_down_light_01_onlevelconfiguration_9 = my_entities.NumberLivingDownLight01Onlevelconfiguration9
        number_living_down_light_01_onofftransitiontimeconfiguration_9 = my_entities.NumberLivingDownLight01Onofftransitiontimeconfiguration9
        number_living_down_light_01_start_up_color_temperature = my_entities.NumberLivingDownLight01StartUpColorTemperature
        number_living_down_light_01_startupcurrentlevelconfiguration_9 = my_entities.NumberLivingDownLight01Startupcurrentlevelconfiguration9
        select_living_down_light_01_startuponoffselect_9 = my_entities.SelectLivingDownLight01Startuponoffselect9
        update_living_down_light_01_firmware = my_entities.UpdateLivingDownLight01Firmware




class KitchenMainLight_2f(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "c7457b86d6c698e9eb880dcd5b91ef2f"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_sonoff_01minizb_rssi = my_entities.SensorSonoff01minizbRssi
        sensor_sonoff_01minizb_lqi = my_entities.SensorSonoff01minizbLqi
        button_kitchen_main_light_identifybutton = my_entities.ButtonKitchenMainLightIdentifybutton
        light_kitchen_main_light = my_entities.LightKitchenMainLight
        update_kitchen_main_light_firmware = my_entities.UpdateKitchenMainLightFirmware




class DiningMainLight01_ff(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "9d81f0e2fef987777e18692b538612ff"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_awox_tlsr82xx_rssi = my_entities.SensorAwoxTlsr82xxRssi
        sensor_awox_tlsr82xx_lqi = my_entities.SensorAwoxTlsr82xxLqi
        button_dining_main_light_01_identifybutton = my_entities.ButtonDiningMainLight01Identifybutton
        light_dining_main_light_01 = my_entities.LightDiningMainLight01
        binary_sensor_dining_main_light_01_opening = my_entities.BinarySensorDiningMainLight01Opening
        number_dining_main_light_01_start_up_color_temperature = my_entities.NumberDiningMainLight01StartUpColorTemperature
        number_dining_main_light_01_startupcurrentlevelconfiguration = my_entities.NumberDiningMainLight01Startupcurrentlevelconfiguration
        select_dining_main_light_01_startuponoffselect = my_entities.SelectDiningMainLight01Startuponoffselect




class DiningMainLight02_95(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "8d875e28eff5aec83b6791c1ccf12195"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_awox_tlsr82xx_rssi_2 = my_entities.SensorAwoxTlsr82xxRssi2
        sensor_awox_tlsr82xx_lqi_2 = my_entities.SensorAwoxTlsr82xxLqi2
        button_dining_main_light_02_identifybutton_2 = my_entities.ButtonDiningMainLight02Identifybutton2
        light_dining_main_light_02 = my_entities.LightDiningMainLight02
        binary_sensor_dining_main_light_02_opening_2 = my_entities.BinarySensorDiningMainLight02Opening2
        number_dining_main_light_02_start_up_color_temperature = my_entities.NumberDiningMainLight02StartUpColorTemperature
        number_dining_main_light_02_startupcurrentlevelconfiguration_2 = my_entities.NumberDiningMainLight02Startupcurrentlevelconfiguration2
        select_dining_main_light_02_startuponoffselect_2 = my_entities.SelectDiningMainLight02Startuponoffselect2




class LivingDownLight02_a9(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "28a55a6e1112de03c235ed13f265e5a9"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi = my_entities.SensorInnrRs230CRssi
        sensor_innr_rs_230_c_lqi = my_entities.SensorInnrRs230CLqi
        light_living_down_light_02 = my_entities.LightLivingDownLight02
        number_living_down_light_02_start_up_color_temperature = my_entities.NumberLivingDownLight02StartUpColorTemperature
        button_living_down_light_02_identify = my_entities.ButtonLivingDownLight02Identify
        number_living_down_light_02_on_level = my_entities.NumberLivingDownLight02OnLevel
        number_living_down_light_02_on_off_transition_time = my_entities.NumberLivingDownLight02OnOffTransitionTime
        select_living_down_light_02_start_up_behavior = my_entities.SelectLivingDownLight02StartUpBehavior
        number_living_down_light_02_start_up_current_level = my_entities.NumberLivingDownLight02StartUpCurrentLevel
        update_living_down_light_02_firmware = my_entities.UpdateLivingDownLight02Firmware




class LivingDownLight03_6c(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "724db7afb158e737b318f8f6a25be76c"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_2 = my_entities.SensorInnrRs230CRssi2
        sensor_innr_rs_230_c_lqi_2 = my_entities.SensorInnrRs230CLqi2
        button_living_down_light_03_identifybutton_2 = my_entities.ButtonLivingDownLight03Identifybutton2
        light_living_down_light_03 = my_entities.LightLivingDownLight03
        number_living_down_light_03_onlevelconfiguration_2 = my_entities.NumberLivingDownLight03Onlevelconfiguration2
        number_living_down_light_03_onofftransitiontimeconfiguration_2 = my_entities.NumberLivingDownLight03Onofftransitiontimeconfiguration2
        number_living_down_light_03_start_up_color_temperature = my_entities.NumberLivingDownLight03StartUpColorTemperature
        number_living_down_light_03_startupcurrentlevelconfiguration_2 = my_entities.NumberLivingDownLight03Startupcurrentlevelconfiguration2
        select_living_down_light_03_startuponoffselect_2 = my_entities.SelectLivingDownLight03Startuponoffselect2
        update_living_down_light_03_firmware = my_entities.UpdateLivingDownLight03Firmware




class LivingDownLight04_bc(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "f25d96f98c4b0a65a837f2a60b7fb5bc"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_3 = my_entities.SensorInnrRs230CRssi3
        sensor_innr_rs_230_c_lqi_3 = my_entities.SensorInnrRs230CLqi3
        light_living_down_light_04 = my_entities.LightLivingDownLight04
        number_living_down_light_04_start_up_color_temperature = my_entities.NumberLivingDownLight04StartUpColorTemperature
        button_living_down_light_04_identify = my_entities.ButtonLivingDownLight04Identify
        number_living_down_light_04_on_level = my_entities.NumberLivingDownLight04OnLevel
        number_living_down_light_04_on_off_transition_time = my_entities.NumberLivingDownLight04OnOffTransitionTime
        select_living_down_light_04_start_up_behavior = my_entities.SelectLivingDownLight04StartUpBehavior
        number_living_down_light_04_start_up_current_level = my_entities.NumberLivingDownLight04StartUpCurrentLevel
        update_living_down_light_04_firmware = my_entities.UpdateLivingDownLight04Firmware




class LivingDownLight05_b6(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "382a4339e445922e7979bf4fbc7c47b6"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_4 = my_entities.SensorInnrRs230CRssi4
        sensor_innr_rs_230_c_lqi_4 = my_entities.SensorInnrRs230CLqi4
        light_living_down_light_05 = my_entities.LightLivingDownLight05
        number_living_down_light_05_start_up_color_temperature = my_entities.NumberLivingDownLight05StartUpColorTemperature
        button_living_down_light_05_identify = my_entities.ButtonLivingDownLight05Identify
        number_living_down_light_05_on_level = my_entities.NumberLivingDownLight05OnLevel
        number_living_down_light_05_on_off_transition_time = my_entities.NumberLivingDownLight05OnOffTransitionTime
        number_living_down_light_05_start_up_current_level = my_entities.NumberLivingDownLight05StartUpCurrentLevel
        select_living_down_light_05_start_up_behavior = my_entities.SelectLivingDownLight05StartUpBehavior
        update_living_down_light_05_firmware = my_entities.UpdateLivingDownLight05Firmware




class LivingDownLight06_c4(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "6a3409358f8587a1027bb10ebdaa52c4"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_5 = my_entities.SensorInnrRs230CRssi5
        sensor_innr_rs_230_c_lqi_5 = my_entities.SensorInnrRs230CLqi5
        button_living_down_light_06_identifybutton_4 = my_entities.ButtonLivingDownLight06Identifybutton4
        light_living_down_light_06 = my_entities.LightLivingDownLight06
        number_living_down_light_06_onlevelconfiguration_4 = my_entities.NumberLivingDownLight06Onlevelconfiguration4
        number_living_down_light_06_onofftransitiontimeconfiguration_4 = my_entities.NumberLivingDownLight06Onofftransitiontimeconfiguration4
        number_living_down_light_06_start_up_color_temperature = my_entities.NumberLivingDownLight06StartUpColorTemperature
        number_living_down_light_06_startupcurrentlevelconfiguration_4 = my_entities.NumberLivingDownLight06Startupcurrentlevelconfiguration4
        select_living_down_light_06_startuponoffselect_4 = my_entities.SelectLivingDownLight06Startuponoffselect4
        update_living_down_light_06_firmware = my_entities.UpdateLivingDownLight06Firmware




class LivingDownLight07_bd(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "ec5ebd77800a011201aad0123c4d91bd"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_6 = my_entities.SensorInnrRs230CRssi6
        sensor_innr_rs_230_c_lqi_6 = my_entities.SensorInnrRs230CLqi6
        light_living_down_light_07 = my_entities.LightLivingDownLight07
        number_living_down_light_07_start_up_color_temperature = my_entities.NumberLivingDownLight07StartUpColorTemperature
        button_living_down_light_07_identify = my_entities.ButtonLivingDownLight07Identify
        number_living_down_light_07_on_level = my_entities.NumberLivingDownLight07OnLevel
        number_living_down_light_07_on_off_transition_time = my_entities.NumberLivingDownLight07OnOffTransitionTime
        select_living_down_light_07_start_up_behavior = my_entities.SelectLivingDownLight07StartUpBehavior
        number_living_down_light_07_start_up_current_level = my_entities.NumberLivingDownLight07StartUpCurrentLevel
        update_living_down_light_07_firmware = my_entities.UpdateLivingDownLight07Firmware




class LivingDownLight08_95(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "8b1994f323e86cd5eee43419ff7c2495"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_7 = my_entities.SensorInnrRs230CRssi7
        sensor_innr_rs_230_c_lqi_7 = my_entities.SensorInnrRs230CLqi7
        light_living_down_light_08 = my_entities.LightLivingDownLight08
        number_living_down_light_08_start_up_color_temperature = my_entities.NumberLivingDownLight08StartUpColorTemperature
        button_living_down_light_08_identify = my_entities.ButtonLivingDownLight08Identify
        number_living_down_light_08_on_level = my_entities.NumberLivingDownLight08OnLevel
        number_living_down_light_08_on_off_transition_time = my_entities.NumberLivingDownLight08OnOffTransitionTime
        select_living_down_light_08_start_up_behavior = my_entities.SelectLivingDownLight08StartUpBehavior
        number_living_down_light_08_start_up_current_level = my_entities.NumberLivingDownLight08StartUpCurrentLevel
        update_living_down_light_08_firmware = my_entities.UpdateLivingDownLight08Firmware




class LivingDownLight09_32(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "884dfdc10561d0534b50d884aad3b132"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_innr_rs_230_c_rssi_8 = my_entities.SensorInnrRs230CRssi8
        sensor_innr_rs_230_c_lqi_8 = my_entities.SensorInnrRs230CLqi8
        button_living_down_light_09_identifybutton_6 = my_entities.ButtonLivingDownLight09Identifybutton6
        light_living_down_light_09 = my_entities.LightLivingDownLight09
        number_living_down_light_09_onlevelconfiguration_6 = my_entities.NumberLivingDownLight09Onlevelconfiguration6
        number_living_down_light_09_onofftransitiontimeconfiguration_6 = my_entities.NumberLivingDownLight09Onofftransitiontimeconfiguration6
        number_living_down_light_09_start_up_color_temperature = my_entities.NumberLivingDownLight09StartUpColorTemperature
        number_living_down_light_09_startupcurrentlevelconfiguration_6 = my_entities.NumberLivingDownLight09Startupcurrentlevelconfiguration6
        select_living_down_light_09_startuponoffselect_6 = my_entities.SelectLivingDownLight09Startuponoffselect6
        update_living_down_light_09_firmware = my_entities.UpdateLivingDownLight09Firmware




class FileEditor_56(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "9ef171592ea1010f3661c65633b6cd56"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        binary_sensor_file_editor_running = my_entities.BinarySensorFileEditorRunning
        sensor_file_editor_version = my_entities.SensorFileEditorVersion
        sensor_file_editor_newest_version = my_entities.SensorFileEditorNewestVersion
        sensor_file_editor_cpu_percent = my_entities.SensorFileEditorCpuPercent
        sensor_file_editor_memory_percent = my_entities.SensorFileEditorMemoryPercent
        update_file_editor_update = my_entities.UpdateFileEditorUpdate




class SamsungQ64ba55Tv_cd(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "f3604fa009d16354ba1e2abbb963f8cd"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        media_player_samsung_q64ba_55_tv = my_entities.MediaPlayerSamsungQ64ba55Tv
        remote_samsung_q64ba_55_tv = my_entities.RemoteSamsungQ64ba55Tv




class TerminalxSsh_44(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "e04484f3a56a3f5a79a50f15e3014644"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        binary_sensor_terminal_ssh_running = my_entities.BinarySensorTerminalSshRunning
        sensor_terminal_ssh_version = my_entities.SensorTerminalSshVersion
        sensor_terminal_ssh_newest_version = my_entities.SensorTerminalSshNewestVersion
        sensor_terminal_ssh_cpu_percent = my_entities.SensorTerminalSshCpuPercent
        sensor_terminal_ssh_memory_percent = my_entities.SensorTerminalSshMemoryPercent
        update_terminal_ssh_update = my_entities.UpdateTerminalSshUpdate




class GaleryFlexoLight_12(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "22dba118ea8c1a7086ad4479d1e95712"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi = my_entities.SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmRssi
        sensor_ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi = my_entities.SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmLqi
        number_galery_flexo_light_start_up_color_temperature = my_entities.NumberGaleryFlexoLightStartUpColorTemperature
        button_galery_flexo_light_identify = my_entities.ButtonGaleryFlexoLightIdentify
        number_galery_flexo_light_on_level = my_entities.NumberGaleryFlexoLightOnLevel
        number_galery_flexo_light_on_off_transition_time = my_entities.NumberGaleryFlexoLightOnOffTransitionTime
        select_galery_flexo_light_start_up_behavior = my_entities.SelectGaleryFlexoLightStartUpBehavior
        number_galery_flexo_light_start_up_current_level = my_entities.NumberGaleryFlexoLightStartUpCurrentLevel
        light_galery_flexo_light_light = my_entities.LightGaleryFlexoLightLight
        update_galery_flexo_light_firmware = my_entities.UpdateGaleryFlexoLightFirmware




class BedMainLight_88(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "176891a7db6daf1e864a9e578cea3388"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi = my_entities.SensorIkeaOfSwedenTradfriBulbE27Ww806lmRssi
        sensor_ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi = my_entities.SensorIkeaOfSwedenTradfriBulbE27Ww806lmLqi
        button_bed_main_light_identify = my_entities.ButtonBedMainLightIdentify
        light_bed_main_light_light = my_entities.LightBedMainLightLight
        number_bed_main_light_on_level = my_entities.NumberBedMainLightOnLevel
        number_bed_main_light_on_off_transition_time = my_entities.NumberBedMainLightOnOffTransitionTime
        select_bed_main_light_start_up_behavior = my_entities.SelectBedMainLightStartUpBehavior
        number_bed_main_light_start_up_current_level = my_entities.NumberBedMainLightStartUpCurrentLevel
        update_bed_main_light_firmware = my_entities.UpdateBedMainLightFirmware




class OfficeMainLight_ea(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "6a38306ec46728170175ef7cac3ea4ea"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_bulb_e27_ww_806lm_rssi_2 = my_entities.SensorIkeaOfSwedenTradfriBulbE27Ww806lmRssi2
        sensor_ikea_of_sweden_tradfri_bulb_e27_ww_806lm_lqi_2 = my_entities.SensorIkeaOfSwedenTradfriBulbE27Ww806lmLqi2
        button_office_main_light_identifybutton_2 = my_entities.ButtonOfficeMainLightIdentifybutton2
        light_office_main_light_light_2 = my_entities.LightOfficeMainLightLight2
        number_office_main_light_onlevelconfiguration_2 = my_entities.NumberOfficeMainLightOnlevelconfiguration2
        number_office_main_light_onofftransitiontimeconfiguration_2 = my_entities.NumberOfficeMainLightOnofftransitiontimeconfiguration2
        number_office_main_light_startupcurrentlevelconfiguration_2 = my_entities.NumberOfficeMainLightStartupcurrentlevelconfiguration2
        select_office_main_light_startuponoffselect_2 = my_entities.SelectOfficeMainLightStartuponoffselect2
        update_office_main_light_firmware = my_entities.UpdateOfficeMainLightFirmware




class Tailscale_64(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "314dd30fce529dbaf8e55aaed367b664"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        binary_sensor_tailscale_running = my_entities.BinarySensorTailscaleRunning
        sensor_tailscale_version = my_entities.SensorTailscaleVersion
        sensor_tailscale_newest_version = my_entities.SensorTailscaleNewestVersion
        sensor_tailscale_cpu_percent = my_entities.SensorTailscaleCpuPercent
        sensor_tailscale_memory_percent = my_entities.SensorTailscaleMemoryPercent
        update_tailscale_update = my_entities.UpdateTailscaleUpdate




class BedMainSwitch01_5e(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "f61b9317af000c4b650b5d686343895e"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi
        sensor_bed_main_switch_01_battery = my_entities.SensorBedMainSwitch01Battery
        button_bed_main_switch_01_identify = my_entities.ButtonBedMainSwitch01Identify
        update_bed_main_switch_01_firmware = my_entities.UpdateBedMainSwitch01Firmware

    no_action = False


class OfficeMainSwitch01_47(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "11071fea99ed8823fe1bd6f4849a1747"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_2 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi2
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_2 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi2
        sensor_office_main_switch_01_battery = my_entities.SensorOfficeMainSwitch01Battery
        button_office_main_switch_01_identify = my_entities.ButtonOfficeMainSwitch01Identify
        update_office_main_switch_01_firmware = my_entities.UpdateOfficeMainSwitch01Firmware

    no_action = False


class OfficeJoniSwitch_35(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "6d1eca1676129527c2ad74b66e39e435"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_3 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi3
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_3 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi3
        sensor_office_joni_switch_battery = my_entities.SensorOfficeJoniSwitchBattery
        update_office_joni_switch_firmware = my_entities.UpdateOfficeJoniSwitchFirmware
        button_office_joni_switch_identify = my_entities.ButtonOfficeJoniSwitchIdentify

    no_action = False


class BedLeftSwitch_9f(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "d563507ad7b015ef221e0a70b6afc49f"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_5 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi5
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_5 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi5
        sensor_bed_left_switch_battery = my_entities.SensorBedLeftSwitchBattery
        button_bed_left_switch_identify = my_entities.ButtonBedLeftSwitchIdentify
        update_bed_left_switch_firmware = my_entities.UpdateBedLeftSwitchFirmware

    no_action = False


class LivingMainControl_83(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "Remote Control N2")
    quirk_attribute = "device_automation_triggers_metadata"
    device_id = "a701fbed4393032c83f56e66d56c2a83"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_remote_control_n2_rssi = my_entities.SensorIkeaOfSwedenRemoteControlN2Rssi
        sensor_ikea_of_sweden_remote_control_n2_lqi = my_entities.SensorIkeaOfSwedenRemoteControlN2Lqi
        sensor_living_main_control_battery = my_entities.SensorLivingMainControlBattery
        button_living_main_control_identify = my_entities.ButtonLivingMainControlIdentify
        update_living_main_control_firmware = my_entities.UpdateLivingMainControlFirmware

    no_action = False


class DiningMainSwitch_bb(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "2851603edfb42a65d6925eb41f784bbb"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_6 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi6
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_6 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi6
        sensor_dining_main_switch_battery_6 = my_entities.SensorDiningMainSwitchBattery6
        button_dining_main_switch_identify_4 = my_entities.ButtonDiningMainSwitchIdentify4
        update_dining_main_switch_firmware = my_entities.UpdateDiningMainSwitchFirmware

    no_action = False


class BedRightLight_ea(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "0e0b1c6beeb9d20b78672af8115982ea"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfribulbgu10ws345lm_rssi_2 = my_entities.SensorIkeaOfSwedenTradfribulbgu10ws345lmRssi2
        sensor_ikea_of_sweden_tradfribulbgu10ws345lm_lqi_2 = my_entities.SensorIkeaOfSwedenTradfribulbgu10ws345lmLqi2
        button_bed_right_light_identify = my_entities.ButtonBedRightLightIdentify
        light_bed_right_light_light = my_entities.LightBedRightLightLight
        number_bed_right_light_on_level = my_entities.NumberBedRightLightOnLevel
        number_bed_right_light_on_off_transition_time = my_entities.NumberBedRightLightOnOffTransitionTime
        select_bed_right_light_start_up_behavior = my_entities.SelectBedRightLightStartUpBehavior
        number_bed_right_light_start_up_color_temperature = my_entities.NumberBedRightLightStartUpColorTemperature
        number_bed_right_light_start_up_current_level = my_entities.NumberBedRightLightStartUpCurrentLevel
        update_bed_right_light_firmware = my_entities.UpdateBedRightLightFirmware




class BedRightSwitch_77(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "df2045cfeac2943e4f94fa9a24723277"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_7 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi7
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_7 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi7
        sensor_bed_right_switch_battery = my_entities.SensorBedRightSwitchBattery
        button_bed_right_switch_identify = my_entities.ButtonBedRightSwitchIdentify
        update_bed_right_switch_firmware = my_entities.UpdateBedRightSwitchFirmware

    no_action = False


class TvGamingButton_9a(models.Device):
    quirk = gen_devices.get_device_quirk("eWeLink", "WB01")
    quirk_attribute = "device_automation_triggers_metadata"
    device_id = "1fc43fcc44e909a2a6d39ee73f257b9a"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_tv_gaming_button_battery = my_entities.SensorTvGamingButtonBattery
        button_tv_gaming_button_identify = my_entities.ButtonTvGamingButtonIdentify
        sensor_tv_gaming_button_lqi = my_entities.SensorTvGamingButtonLqi
        sensor_tv_gaming_button_rssi = my_entities.SensorTvGamingButtonRssi

    no_action = False


class SamsungQ64ba55Tv_fe(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "d9210728a89d2af02be858974aed07fe"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        media_player_samsung_q64ba_55_tv_2 = my_entities.MediaPlayerSamsungQ64ba55Tv2




class JoniDeskButton_6f(models.Device):
    quirk = gen_devices.get_device_quirk("eWeLink", "WB01")
    quirk_attribute = "device_automation_triggers_metadata"
    device_id = "ee80cf293d694022cf00e664a062c06f"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ewelink_wb01_rssi = my_entities.SensorEwelinkWb01Rssi
        sensor_ewelink_wb01_lqi = my_entities.SensorEwelinkWb01Lqi
        sensor_joni_desk_button_battery = my_entities.SensorJoniDeskButtonBattery
        button_joni_desk_button_identify = my_entities.ButtonJoniDeskButtonIdentify

    no_action = False


class OfficeDownlightJoni_19(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "d41fe84161aac5e954aa7d78d91b1819"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_bulb_e14_cws_470lm_rssi = my_entities.SensorIkeaOfSwedenTradfriBulbE14Cws470lmRssi
        sensor_ikea_of_sweden_tradfri_bulb_e14_cws_470lm_lqi = my_entities.SensorIkeaOfSwedenTradfriBulbE14Cws470lmLqi
        button_office_downlight_joni_identify = my_entities.ButtonOfficeDownlightJoniIdentify
        light_office_downlight_joni = my_entities.LightOfficeDownlightJoni
        number_office_downlight_joni_on_level = my_entities.NumberOfficeDownlightJoniOnLevel
        select_office_downlight_joni_start_up_behavior = my_entities.SelectOfficeDownlightJoniStartUpBehavior
        number_office_downlight_joni_start_up_color_temperature = my_entities.NumberOfficeDownlightJoniStartUpColorTemperature
        number_office_downlight_joni_start_up_current_level = my_entities.NumberOfficeDownlightJoniStartUpCurrentLevel
        update_office_downlight_joni_firmware = my_entities.UpdateOfficeDownlightJoniFirmware




class LivingAmbientSofa_f7(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "20524a8c01e94ae3e70f83771ade00f7"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_rssi_2 = my_entities.SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmRssi2
        sensor_ikea_of_sweden_tradfribulbe27wsglobeopal1055lm_lqi_2 = my_entities.SensorIkeaOfSwedenTradfribulbe27wsglobeopal1055lmLqi2
        button_living_ambient_sofa_identify = my_entities.ButtonLivingAmbientSofaIdentify
        light_living_ambient_sofa_light = my_entities.LightLivingAmbientSofaLight
        number_living_ambient_sofa_on_level = my_entities.NumberLivingAmbientSofaOnLevel
        number_living_ambient_sofa_on_off_transition_time = my_entities.NumberLivingAmbientSofaOnOffTransitionTime
        select_living_ambient_sofa_start_up_behavior = my_entities.SelectLivingAmbientSofaStartUpBehavior
        number_living_ambient_sofa_start_up_color_temperature = my_entities.NumberLivingAmbientSofaStartUpColorTemperature
        number_living_ambient_sofa_start_up_current_level = my_entities.NumberLivingAmbientSofaStartUpCurrentLevel
        update_living_ambient_sofa_firmware = my_entities.UpdateLivingAmbientSofaFirmware




class BedLeftLight_95(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "4235267e075fb2a70160bdc771810295"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfribulbgu10ws345lm_rssi = my_entities.SensorIkeaOfSwedenTradfribulbgu10ws345lmRssi
        sensor_ikea_of_sweden_tradfribulbgu10ws345lm_lqi = my_entities.SensorIkeaOfSwedenTradfribulbgu10ws345lmLqi
        button_bed_left_light_identify = my_entities.ButtonBedLeftLightIdentify
        light_bed_left_light_light = my_entities.LightBedLeftLightLight
        number_bed_left_light_on_level = my_entities.NumberBedLeftLightOnLevel
        number_bed_left_light_on_off_transition_time = my_entities.NumberBedLeftLightOnOffTransitionTime
        select_bed_left_light_start_up_behavior = my_entities.SelectBedLeftLightStartUpBehavior
        number_bed_left_light_start_up_color_temperature = my_entities.NumberBedLeftLightStartUpColorTemperature
        number_bed_left_light_start_up_current_level = my_entities.NumberBedLeftLightStartUpCurrentLevel
        update_bed_left_light_firmware = my_entities.UpdateBedLeftLightFirmware




class KitchenMainSwitch_91(models.Device):
    quirk = gen_devices.get_device_quirk("IKEA of Sweden", "TRADFRI on/off switch")
    quirk_attribute = "device_automation_triggers"
    device_id = "83f3a2ec56c0e312b046b46446691791"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ikea_of_sweden_tradfri_on_off_switch_rssi_4 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchRssi4
        sensor_ikea_of_sweden_tradfri_on_off_switch_lqi_4 = my_entities.SensorIkeaOfSwedenTradfriOnOffSwitchLqi4
        sensor_kitchen_main_switch_battery = my_entities.SensorKitchenMainSwitchBattery
        button_kitchen_main_switch_identify = my_entities.ButtonKitchenMainSwitchIdentify
        update_kitchen_main_switch_firmware = my_entities.UpdateKitchenMainSwitchFirmware

    no_action = False


class Hacs_b1(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "80cd8633ed3f38ed19b86bf2fa1df6b1"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_hacs = my_entities.SensorHacs




class GaleryLight1_16(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "59db7ac655d4cc512c470f4f68b6ac16"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_tz3210_dksca8p8_ts0505b_rssi = my_entities.SensorTz3210Dksca8p8Ts0505bRssi
        sensor_tz3210_dksca8p8_ts0505b_lqi = my_entities.SensorTz3210Dksca8p8Ts0505bLqi
        light_galery_light_1 = my_entities.LightGaleryLight1
        button_galery_light_1_identify = my_entities.ButtonGaleryLight1Identify
        number_galery_light_1_start_up_color_temperature = my_entities.NumberGaleryLight1StartUpColorTemperature
        update_galery_light_1_firmware = my_entities.UpdateGaleryLight1Firmware




class GaleryLight2_9b(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "773311fd39675f914631c4de4261699b"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_tz3210_dksca8p8_ts0505b_rssi_2 = my_entities.SensorTz3210Dksca8p8Ts0505bRssi2
        sensor_tz3210_dksca8p8_ts0505b_lqi_2 = my_entities.SensorTz3210Dksca8p8Ts0505bLqi2
        light_galery_light_2 = my_entities.LightGaleryLight2
        button_galery_light_2_identify = my_entities.ButtonGaleryLight2Identify
        number_galery_light_2_start_up_color_temperature = my_entities.NumberGaleryLight2StartUpColorTemperature
        update_galery_light_2_firmware = my_entities.UpdateGaleryLight2Firmware




class HomeAssistantHost_02(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "ab3e5233df6ae2e3386598f445678b02"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_home_assistant_host_os_agent_version = my_entities.SensorHomeAssistantHostOsAgentVersion
        sensor_home_assistant_host_apparmor_version = my_entities.SensorHomeAssistantHostApparmorVersion
        sensor_home_assistant_host_disk_total = my_entities.SensorHomeAssistantHostDiskTotal
        sensor_home_assistant_host_disk_used = my_entities.SensorHomeAssistantHostDiskUsed
        sensor_home_assistant_host_disk_free = my_entities.SensorHomeAssistantHostDiskFree




class Sun_73(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "2f05da6ec3274d5b4aa5f9093a1b0673"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_sun_next_dawn = my_entities.SensorSunNextDawn
        sensor_sun_next_dusk = my_entities.SensorSunNextDusk
        sensor_sun_next_midnight = my_entities.SensorSunNextMidnight
        sensor_sun_next_noon = my_entities.SensorSunNextNoon
        sensor_sun_next_rising = my_entities.SensorSunNextRising
        sensor_sun_next_setting = my_entities.SensorSunNextSetting
        sensor_sun_solar_elevation = my_entities.SensorSunSolarElevation
        sensor_sun_solar_azimuth = my_entities.SensorSunSolarAzimuth
        sensor_sun_solar_rising = my_entities.SensorSunSolarRising




class Forecast_60(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "9437d9cf851f6d29ea772ca9a8ccb060"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        weather_forecast_casa = my_entities.WeatherForecastCasa




class OfficeTemperature01_f5(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "a50e9e7dcaf1c074ccef880443dd15f5"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ewelink_th01_rssi = my_entities.SensorEwelinkTh01Rssi
        sensor_ewelink_th01_lqi = my_entities.SensorEwelinkTh01Lqi
        sensor_office_temperature_01_battery = my_entities.SensorOfficeTemperature01Battery
        sensor_office_temperature_01_humidity = my_entities.SensorOfficeTemperature01Humidity
        button_office_temperature_01_identify = my_entities.ButtonOfficeTemperature01Identify
        sensor_office_temperature_01_temperature = my_entities.SensorOfficeTemperature01Temperature




class LivingTemperature01_98(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "6284013aec649bd4b35a3e5405239898"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_ewelink_th01_rssi_2 = my_entities.SensorEwelinkTh01Rssi2
        sensor_ewelink_th01_lqi_2 = my_entities.SensorEwelinkTh01Lqi2
        sensor_living_temperature_01_battery = my_entities.SensorLivingTemperature01Battery
        sensor_living_temperature_01_humidity = my_entities.SensorLivingTemperature01Humidity
        button_living_temperature_01_identify = my_entities.ButtonLivingTemperature01Identify
        sensor_living_temperature_01_temperature = my_entities.SensorLivingTemperature01Temperature




class Alarm_f2(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "b09d2f2d32403ec4d251307f236106f2"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        alarm_control_panel_alarm = my_entities.AlarmControlPanelAlarm




class SentinelTemperature_80(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "ec3e3827a6a81d3071786de7cb8ca680"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_temperature_pl_0_salon = my_entities.SensorTemperaturePl0Salon




class SentinelHumidity_b9(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "4f013eba2fcfd4795f85f9b0130abeb9"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_humidity_pl_0_salon = my_entities.SensorHumidityPl0Salon




class SentinelAirQuality_bf(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "2100636d63fed89f2b2b054d952461bf"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_air_quality_pl_0_salon = my_entities.SensorAirQualityPl0Salon




class S23Joni_65(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "86116456e47329aee683359d5dde4d65"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        device_tracker_joni_s23 = my_entities.DeviceTrackerJoniS23
        sensor_s23_joni_detected_activity = my_entities.SensorS23JoniDetectedActivity
        sensor_s23_joni_sleep_confidence = my_entities.SensorS23JoniSleepConfidence
        sensor_s23_joni_sleep_segment = my_entities.SensorS23JoniSleepSegment
        binary_sensor_s23_joni_android_auto = my_entities.BinarySensorS23JoniAndroidAuto
        sensor_s23_joni_os_version = my_entities.SensorS23JoniOsVersion
        sensor_s23_joni_security_patch = my_entities.SensorS23JoniSecurityPatch
        sensor_s23_joni_current_version = my_entities.SensorS23JoniCurrentVersion
        sensor_s23_joni_app_rx_gb = my_entities.SensorS23JoniAppRxGb
        sensor_s23_joni_app_tx_gb = my_entities.SensorS23JoniAppTxGb
        sensor_s23_joni_app_memory = my_entities.SensorS23JoniAppMemory
        binary_sensor_s23_joni_app_inactive = my_entities.BinarySensorS23JoniAppInactive
        sensor_s23_joni_app_standby_bucket = my_entities.SensorS23JoniAppStandbyBucket
        sensor_s23_joni_app_importance = my_entities.SensorS23JoniAppImportance
        sensor_s23_joni_ringer_mode = my_entities.SensorS23JoniRingerMode
        sensor_s23_joni_audio_mode = my_entities.SensorS23JoniAudioMode
        binary_sensor_s23_joni_headphones = my_entities.BinarySensorS23JoniHeadphones
        binary_sensor_s23_joni_mic_muted = my_entities.BinarySensorS23JoniMicMuted
        binary_sensor_s23_joni_speakerphone = my_entities.BinarySensorS23JoniSpeakerphone
        binary_sensor_s23_joni_music_active = my_entities.BinarySensorS23JoniMusicActive
        sensor_s23_joni_volume_level_alarm = my_entities.SensorS23JoniVolumeLevelAlarm
        sensor_s23_joni_volume_level_call = my_entities.SensorS23JoniVolumeLevelCall
        sensor_s23_joni_volume_level_music = my_entities.SensorS23JoniVolumeLevelMusic
        sensor_s23_joni_volume_level_ringer = my_entities.SensorS23JoniVolumeLevelRinger
        sensor_s23_joni_volume_level_notification = my_entities.SensorS23JoniVolumeLevelNotification
        sensor_s23_joni_volume_level_system = my_entities.SensorS23JoniVolumeLevelSystem
        sensor_s23_joni_volume_level_dtmf = my_entities.SensorS23JoniVolumeLevelDtmf
        sensor_s23_joni_volume_level_accessibility = my_entities.SensorS23JoniVolumeLevelAccessibility
        sensor_s23_joni_battery_level = my_entities.SensorS23JoniBatteryLevel
        sensor_s23_joni_battery_state = my_entities.SensorS23JoniBatteryState
        binary_sensor_s23_joni_is_charging = my_entities.BinarySensorS23JoniIsCharging
        sensor_s23_joni_charger_type = my_entities.SensorS23JoniChargerType
        sensor_s23_joni_battery_health = my_entities.SensorS23JoniBatteryHealth
        sensor_s23_joni_battery_temperature = my_entities.SensorS23JoniBatteryTemperature
        sensor_s23_joni_battery_power = my_entities.SensorS23JoniBatteryPower
        sensor_s23_joni_bluetooth_connection = my_entities.SensorS23JoniBluetoothConnection
        binary_sensor_s23_joni_bluetooth_state = my_entities.BinarySensorS23JoniBluetoothState
        sensor_s23_joni_ble_transmitter = my_entities.SensorS23JoniBleTransmitter
        sensor_s23_joni_beacon_monitor = my_entities.SensorS23JoniBeaconMonitor
        sensor_s23_joni_car_battery = my_entities.SensorS23JoniCarBattery
        sensor_s23_joni_car_name = my_entities.SensorS23JoniCarName
        sensor_s23_joni_car_charging_status = my_entities.SensorS23JoniCarChargingStatus
        sensor_s23_joni_car_ev_connector_type = my_entities.SensorS23JoniCarEvConnectorType
        sensor_s23_joni_car_fuel = my_entities.SensorS23JoniCarFuel
        sensor_s23_joni_car_fuel_type = my_entities.SensorS23JoniCarFuelType
        sensor_s23_joni_car_odometer = my_entities.SensorS23JoniCarOdometer
        sensor_s23_joni_screen_brightness = my_entities.SensorS23JoniScreenBrightness
        sensor_s23_joni_screen_off_timeout = my_entities.SensorS23JoniScreenOffTimeout
        sensor_s23_joni_do_not_disturb_sensor = my_entities.SensorS23JoniDoNotDisturbSensor
        sensor_s23_joni_accent_color = my_entities.SensorS23JoniAccentColor
        binary_sensor_s23_joni_work_profile = my_entities.BinarySensorS23JoniWorkProfile
        sensor_s23_joni_geocoded_location = my_entities.SensorS23JoniGeocodedLocation
        binary_sensor_s23_joni_device_locked = my_entities.BinarySensorS23JoniDeviceLocked
        binary_sensor_s23_joni_device_secure = my_entities.BinarySensorS23JoniDeviceSecure
        binary_sensor_s23_joni_keyguard_locked = my_entities.BinarySensorS23JoniKeyguardLocked
        binary_sensor_s23_joni_keyguard_secure = my_entities.BinarySensorS23JoniKeyguardSecure
        sensor_s23_joni_last_used_app = my_entities.SensorS23JoniLastUsedApp
        sensor_s23_joni_last_reboot = my_entities.SensorS23JoniLastReboot
        sensor_s23_joni_last_update_trigger = my_entities.SensorS23JoniLastUpdateTrigger
        sensor_s23_joni_light_sensor = my_entities.SensorS23JoniLightSensor
        binary_sensor_s23_joni_high_accuracy_mode = my_entities.BinarySensorS23JoniHighAccuracyMode
        sensor_s23_joni_high_accuracy_update_interval = my_entities.SensorS23JoniHighAccuracyUpdateInterval
        binary_sensor_s23_joni_mobile_data = my_entities.BinarySensorS23JoniMobileData
        binary_sensor_s23_joni_mobile_data_roaming = my_entities.BinarySensorS23JoniMobileDataRoaming
        sensor_s23_joni_wifi_connection = my_entities.SensorS23JoniWifiConnection
        sensor_s23_joni_wifi_bssid = my_entities.SensorS23JoniWifiBssid
        sensor_s23_joni_wifi_ip_address = my_entities.SensorS23JoniWifiIpAddress
        sensor_s23_joni_wifi_link_speed = my_entities.SensorS23JoniWifiLinkSpeed
        binary_sensor_s23_joni_wifi_state = my_entities.BinarySensorS23JoniWifiState
        sensor_s23_joni_wifi_frequency = my_entities.SensorS23JoniWifiFrequency
        sensor_s23_joni_wifi_signal_strength = my_entities.SensorS23JoniWifiSignalStrength
        sensor_s23_joni_public_ip_address = my_entities.SensorS23JoniPublicIpAddress
        binary_sensor_s23_joni_hotspot_state = my_entities.BinarySensorS23JoniHotspotState
        sensor_s23_joni_network_type = my_entities.SensorS23JoniNetworkType
        binary_sensor_s23_joni_nfc_state = my_entities.BinarySensorS23JoniNfcState
        sensor_s23_joni_next_alarm = my_entities.SensorS23JoniNextAlarm
        sensor_s23_joni_last_notification = my_entities.SensorS23JoniLastNotification
        sensor_s23_joni_last_removed_notification = my_entities.SensorS23JoniLastRemovedNotification
        sensor_s23_joni_active_notification_count = my_entities.SensorS23JoniActiveNotificationCount
        sensor_s23_joni_media_session = my_entities.SensorS23JoniMediaSession
        sensor_s23_joni_phone_state = my_entities.SensorS23JoniPhoneState
        sensor_s23_joni_sim_1 = my_entities.SensorS23JoniSim1
        sensor_s23_joni_sim_2 = my_entities.SensorS23JoniSim2
        binary_sensor_s23_joni_interactive = my_entities.BinarySensorS23JoniInteractive
        binary_sensor_s23_joni_doze_mode = my_entities.BinarySensorS23JoniDozeMode
        binary_sensor_s23_joni_power_save = my_entities.BinarySensorS23JoniPowerSave
        sensor_s23_joni_pressure_sensor = my_entities.SensorS23JoniPressureSensor
        sensor_s23_joni_proximity_sensor = my_entities.SensorS23JoniProximitySensor
        sensor_s23_joni_steps_sensor = my_entities.SensorS23JoniStepsSensor
        sensor_s23_joni_internal_storage = my_entities.SensorS23JoniInternalStorage
        sensor_s23_joni_external_storage = my_entities.SensorS23JoniExternalStorage
        sensor_s23_joni_current_time_zone = my_entities.SensorS23JoniCurrentTimeZone
        sensor_s23_joni_mobile_rx_gb = my_entities.SensorS23JoniMobileRxGb
        sensor_s23_joni_mobile_tx_gb = my_entities.SensorS23JoniMobileTxGb
        sensor_s23_joni_total_rx_gb = my_entities.SensorS23JoniTotalRxGb
        sensor_s23_joni_total_tx_gb = my_entities.SensorS23JoniTotalTxGb
        sensor_s23_joni_ipv6_addresses = my_entities.SensorS23JoniIpv6Addresses
        sensor_s23_joni_remaining_charge_time = my_entities.SensorS23JoniRemainingChargeTime




class Mi9Clau_36(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "a11262bebbc2bd1aa95fd9c3d95d7136"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        device_tracker_mi9_clau = my_entities.DeviceTrackerMi9Clau
        sensor_mi9_clau_detected_activity = my_entities.SensorMi9ClauDetectedActivity
        sensor_mi9_clau_sleep_confidence = my_entities.SensorMi9ClauSleepConfidence
        sensor_mi9_clau_sleep_segment = my_entities.SensorMi9ClauSleepSegment
        binary_sensor_mi9_clau_android_auto = my_entities.BinarySensorMi9ClauAndroidAuto
        sensor_mi9_clau_os_version = my_entities.SensorMi9ClauOsVersion
        sensor_mi9_clau_security_patch = my_entities.SensorMi9ClauSecurityPatch
        sensor_mi9_clau_current_version = my_entities.SensorMi9ClauCurrentVersion
        sensor_mi9_clau_app_rx_gb = my_entities.SensorMi9ClauAppRxGb
        sensor_mi9_clau_app_tx_gb = my_entities.SensorMi9ClauAppTxGb
        sensor_mi9_clau_app_memory = my_entities.SensorMi9ClauAppMemory
        binary_sensor_mi9_clau_app_inactive = my_entities.BinarySensorMi9ClauAppInactive
        sensor_mi9_clau_app_standby_bucket = my_entities.SensorMi9ClauAppStandbyBucket
        sensor_mi9_clau_app_importance = my_entities.SensorMi9ClauAppImportance
        sensor_mi9_clau_ringer_mode = my_entities.SensorMi9ClauRingerMode
        sensor_mi9_clau_audio_mode = my_entities.SensorMi9ClauAudioMode
        binary_sensor_mi9_clau_headphones = my_entities.BinarySensorMi9ClauHeadphones
        binary_sensor_mi9_clau_mic_muted = my_entities.BinarySensorMi9ClauMicMuted
        binary_sensor_mi9_clau_speakerphone = my_entities.BinarySensorMi9ClauSpeakerphone
        binary_sensor_mi9_clau_music_active = my_entities.BinarySensorMi9ClauMusicActive
        sensor_mi9_clau_volume_level_alarm = my_entities.SensorMi9ClauVolumeLevelAlarm
        sensor_mi9_clau_volume_level_call = my_entities.SensorMi9ClauVolumeLevelCall
        sensor_mi9_clau_volume_level_music = my_entities.SensorMi9ClauVolumeLevelMusic
        sensor_mi9_clau_volume_level_ringer = my_entities.SensorMi9ClauVolumeLevelRinger
        sensor_mi9_clau_volume_level_notification = my_entities.SensorMi9ClauVolumeLevelNotification
        sensor_mi9_clau_volume_level_system = my_entities.SensorMi9ClauVolumeLevelSystem
        sensor_mi9_clau_volume_level_dtmf = my_entities.SensorMi9ClauVolumeLevelDtmf
        sensor_mi9_clau_volume_level_accessibility = my_entities.SensorMi9ClauVolumeLevelAccessibility
        sensor_mi9_clau_battery_level = my_entities.SensorMi9ClauBatteryLevel
        sensor_mi9_clau_battery_state = my_entities.SensorMi9ClauBatteryState
        binary_sensor_mi9_clau_is_charging = my_entities.BinarySensorMi9ClauIsCharging
        sensor_mi9_clau_charger_type = my_entities.SensorMi9ClauChargerType
        sensor_mi9_clau_battery_health = my_entities.SensorMi9ClauBatteryHealth
        sensor_mi9_clau_battery_temperature = my_entities.SensorMi9ClauBatteryTemperature
        sensor_mi9_clau_battery_power = my_entities.SensorMi9ClauBatteryPower
        sensor_mi9_clau_bluetooth_connection = my_entities.SensorMi9ClauBluetoothConnection
        binary_sensor_mi9_clau_bluetooth_state = my_entities.BinarySensorMi9ClauBluetoothState
        sensor_mi9_clau_ble_transmitter = my_entities.SensorMi9ClauBleTransmitter
        sensor_mi9_clau_beacon_monitor = my_entities.SensorMi9ClauBeaconMonitor
        sensor_mi9_clau_car_battery = my_entities.SensorMi9ClauCarBattery
        sensor_mi9_clau_car_name = my_entities.SensorMi9ClauCarName
        sensor_mi9_clau_car_charging_status = my_entities.SensorMi9ClauCarChargingStatus
        sensor_mi9_clau_car_ev_connector_type = my_entities.SensorMi9ClauCarEvConnectorType
        sensor_mi9_clau_car_fuel = my_entities.SensorMi9ClauCarFuel
        sensor_mi9_clau_car_fuel_type = my_entities.SensorMi9ClauCarFuelType
        sensor_mi9_clau_car_odometer = my_entities.SensorMi9ClauCarOdometer
        sensor_mi9_clau_screen_brightness = my_entities.SensorMi9ClauScreenBrightness
        sensor_mi9_clau_screen_off_timeout = my_entities.SensorMi9ClauScreenOffTimeout
        sensor_mi9_clau_do_not_disturb_sensor = my_entities.SensorMi9ClauDoNotDisturbSensor
        binary_sensor_mi9_clau_work_profile = my_entities.BinarySensorMi9ClauWorkProfile
        sensor_mi9_clau_geocoded_location = my_entities.SensorMi9ClauGeocodedLocation
        binary_sensor_mi9_clau_device_locked = my_entities.BinarySensorMi9ClauDeviceLocked
        binary_sensor_mi9_clau_device_secure = my_entities.BinarySensorMi9ClauDeviceSecure
        binary_sensor_mi9_clau_keyguard_locked = my_entities.BinarySensorMi9ClauKeyguardLocked
        binary_sensor_mi9_clau_keyguard_secure = my_entities.BinarySensorMi9ClauKeyguardSecure
        sensor_mi9_clau_last_used_app = my_entities.SensorMi9ClauLastUsedApp
        sensor_mi9_clau_last_reboot = my_entities.SensorMi9ClauLastReboot
        sensor_mi9_clau_last_update_trigger = my_entities.SensorMi9ClauLastUpdateTrigger
        sensor_mi9_clau_light_sensor = my_entities.SensorMi9ClauLightSensor
        binary_sensor_mi9_clau_high_accuracy_mode = my_entities.BinarySensorMi9ClauHighAccuracyMode
        sensor_mi9_clau_high_accuracy_update_interval = my_entities.SensorMi9ClauHighAccuracyUpdateInterval
        binary_sensor_mi9_clau_mobile_data = my_entities.BinarySensorMi9ClauMobileData
        binary_sensor_mi9_clau_mobile_data_roaming = my_entities.BinarySensorMi9ClauMobileDataRoaming
        sensor_mi9_clau_wifi_connection = my_entities.SensorMi9ClauWifiConnection
        sensor_mi9_clau_wifi_bssid = my_entities.SensorMi9ClauWifiBssid
        sensor_mi9_clau_wifi_ip_address = my_entities.SensorMi9ClauWifiIpAddress
        sensor_mi9_clau_wifi_link_speed = my_entities.SensorMi9ClauWifiLinkSpeed
        binary_sensor_mi9_clau_wifi_state = my_entities.BinarySensorMi9ClauWifiState
        sensor_mi9_clau_wifi_frequency = my_entities.SensorMi9ClauWifiFrequency
        sensor_mi9_clau_wifi_signal_strength = my_entities.SensorMi9ClauWifiSignalStrength
        sensor_mi9_clau_public_ip_address = my_entities.SensorMi9ClauPublicIpAddress
        binary_sensor_mi9_clau_hotspot_state = my_entities.BinarySensorMi9ClauHotspotState
        sensor_mi9_clau_network_type = my_entities.SensorMi9ClauNetworkType
        binary_sensor_mi9_clau_nfc_state = my_entities.BinarySensorMi9ClauNfcState
        sensor_mi9_clau_next_alarm = my_entities.SensorMi9ClauNextAlarm
        sensor_mi9_clau_last_notification = my_entities.SensorMi9ClauLastNotification
        sensor_mi9_clau_last_removed_notification = my_entities.SensorMi9ClauLastRemovedNotification
        sensor_mi9_clau_active_notification_count = my_entities.SensorMi9ClauActiveNotificationCount
        sensor_mi9_clau_media_session = my_entities.SensorMi9ClauMediaSession
        sensor_mi9_clau_phone_state = my_entities.SensorMi9ClauPhoneState
        sensor_mi9_clau_sim_1 = my_entities.SensorMi9ClauSim1
        sensor_mi9_clau_sim_2 = my_entities.SensorMi9ClauSim2
        binary_sensor_mi9_clau_interactive = my_entities.BinarySensorMi9ClauInteractive
        binary_sensor_mi9_clau_doze_mode = my_entities.BinarySensorMi9ClauDozeMode
        binary_sensor_mi9_clau_power_save = my_entities.BinarySensorMi9ClauPowerSave
        sensor_mi9_clau_proximity_sensor = my_entities.SensorMi9ClauProximitySensor
        sensor_mi9_clau_steps_sensor = my_entities.SensorMi9ClauStepsSensor
        sensor_mi9_clau_internal_storage = my_entities.SensorMi9ClauInternalStorage
        sensor_mi9_clau_external_storage = my_entities.SensorMi9ClauExternalStorage
        sensor_mi9_clau_current_time_zone = my_entities.SensorMi9ClauCurrentTimeZone
        sensor_mi9_clau_mobile_rx_gb = my_entities.SensorMi9ClauMobileRxGb
        sensor_mi9_clau_mobile_tx_gb = my_entities.SensorMi9ClauMobileTxGb
        sensor_mi9_clau_total_rx_gb = my_entities.SensorMi9ClauTotalRxGb
        sensor_mi9_clau_total_tx_gb = my_entities.SensorMi9ClauTotalTxGb
        sensor_mi9_clau_ipv6_addresses = my_entities.SensorMi9ClauIpv6Addresses




class xded3c93e6fbb30c0a8785b42d1c805(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "65ded3c93e6fbb30c0a8785b42d1c805"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_temperature_pl_0_salon_2 = my_entities.SensorTemperaturePl0Salon2




class xfea5204e506a2a0ff0bc5e45093ff(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "988fea5204e506a2a0ff0bc5e45093ff"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_humidity_pl_0_salon_2 = my_entities.SensorHumidityPl0Salon2




class Fa9442ab908ab92b520b5e5f3517d303(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "fa9442ab908ab92b520b5e5f3517d303"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_air_quality_pl_0_salon_2 = my_entities.SensorAirQualityPl0Salon2




class ConnectlifeApiProxyxMqttAddOn_a1(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "399279ef0578b11ba8127f34426026a1"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        binary_sensor_connectlife_api_proxy_mqtt_add_on_running = my_entities.BinarySensorConnectlifeApiProxyMqttAddOnRunning
        sensor_connectlife_api_proxy_mqtt_add_on_version = my_entities.SensorConnectlifeApiProxyMqttAddOnVersion
        sensor_connectlife_api_proxy_mqtt_add_on_newest_version = my_entities.SensorConnectlifeApiProxyMqttAddOnNewestVersion
        sensor_connectlife_api_proxy_mqtt_add_on_cpu_percent = my_entities.SensorConnectlifeApiProxyMqttAddOnCpuPercent
        sensor_connectlife_api_proxy_mqtt_add_on_memory_percent = my_entities.SensorConnectlifeApiProxyMqttAddOnMemoryPercent
        update_connectlife_api_proxy_mqtt_add_on_update = my_entities.UpdateConnectlifeApiProxyMqttAddOnUpdate




class OfficePrinterSwitch_23(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "333c1e8842daae9b3c64744acec3c123"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_sonoff_01minizb_rssi_2 = my_entities.SensorSonoff01minizbRssi2
        sensor_sonoff_01minizb_lqi_2 = my_entities.SensorSonoff01minizbLqi2
        update_office_printer_switch_firmware = my_entities.UpdateOfficePrinterSwitchFirmware
        button_office_printer_switch_identify = my_entities.ButtonOfficePrinterSwitchIdentify
        light_office_printer_switch_light = my_entities.LightOfficePrinterSwitchLight




class PixelClau_6e(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "df1c098ba7e44ad72a4c1c42b203c96e"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        device_tracker_pixel_clau = my_entities.DeviceTrackerPixelClau
        sensor_pixel_clau_detected_activity = my_entities.SensorPixelClauDetectedActivity
        sensor_pixel_clau_sleep_confidence = my_entities.SensorPixelClauSleepConfidence
        sensor_pixel_clau_sleep_segment = my_entities.SensorPixelClauSleepSegment
        binary_sensor_pixel_clau_android_auto = my_entities.BinarySensorPixelClauAndroidAuto
        sensor_pixel_clau_os_version = my_entities.SensorPixelClauOsVersion
        sensor_pixel_clau_security_patch = my_entities.SensorPixelClauSecurityPatch
        sensor_pixel_clau_current_version = my_entities.SensorPixelClauCurrentVersion
        sensor_pixel_clau_app_rx_gb = my_entities.SensorPixelClauAppRxGb
        sensor_pixel_clau_app_tx_gb = my_entities.SensorPixelClauAppTxGb
        sensor_pixel_clau_app_memory = my_entities.SensorPixelClauAppMemory
        binary_sensor_pixel_clau_app_inactive = my_entities.BinarySensorPixelClauAppInactive
        sensor_pixel_clau_app_standby_bucket = my_entities.SensorPixelClauAppStandbyBucket
        sensor_pixel_clau_app_importance = my_entities.SensorPixelClauAppImportance
        sensor_pixel_clau_ringer_mode = my_entities.SensorPixelClauRingerMode
        sensor_pixel_clau_audio_mode = my_entities.SensorPixelClauAudioMode
        binary_sensor_pixel_clau_headphones = my_entities.BinarySensorPixelClauHeadphones
        binary_sensor_pixel_clau_mic_muted = my_entities.BinarySensorPixelClauMicMuted
        binary_sensor_pixel_clau_speakerphone = my_entities.BinarySensorPixelClauSpeakerphone
        binary_sensor_pixel_clau_music_active = my_entities.BinarySensorPixelClauMusicActive
        sensor_pixel_clau_volume_level_alarm = my_entities.SensorPixelClauVolumeLevelAlarm
        sensor_pixel_clau_volume_level_call = my_entities.SensorPixelClauVolumeLevelCall
        sensor_pixel_clau_volume_level_music = my_entities.SensorPixelClauVolumeLevelMusic
        sensor_pixel_clau_volume_level_ringer = my_entities.SensorPixelClauVolumeLevelRinger
        sensor_pixel_clau_volume_level_notification = my_entities.SensorPixelClauVolumeLevelNotification
        sensor_pixel_clau_volume_level_system = my_entities.SensorPixelClauVolumeLevelSystem
        sensor_pixel_clau_volume_level_dtmf = my_entities.SensorPixelClauVolumeLevelDtmf
        sensor_pixel_clau_volume_level_accessibility = my_entities.SensorPixelClauVolumeLevelAccessibility
        sensor_pixel_clau_battery_level = my_entities.SensorPixelClauBatteryLevel
        sensor_pixel_clau_battery_state = my_entities.SensorPixelClauBatteryState
        binary_sensor_pixel_clau_is_charging = my_entities.BinarySensorPixelClauIsCharging
        sensor_pixel_clau_charger_type = my_entities.SensorPixelClauChargerType
        sensor_pixel_clau_battery_health = my_entities.SensorPixelClauBatteryHealth
        sensor_pixel_clau_battery_temperature = my_entities.SensorPixelClauBatteryTemperature
        sensor_pixel_clau_battery_power = my_entities.SensorPixelClauBatteryPower
        sensor_pixel_clau_bluetooth_connection = my_entities.SensorPixelClauBluetoothConnection
        binary_sensor_pixel_clau_bluetooth_state = my_entities.BinarySensorPixelClauBluetoothState
        sensor_pixel_clau_ble_transmitter = my_entities.SensorPixelClauBleTransmitter
        sensor_pixel_clau_beacon_monitor = my_entities.SensorPixelClauBeaconMonitor
        sensor_pixel_clau_car_battery = my_entities.SensorPixelClauCarBattery
        sensor_pixel_clau_car_name = my_entities.SensorPixelClauCarName
        sensor_pixel_clau_car_charging_status = my_entities.SensorPixelClauCarChargingStatus
        sensor_pixel_clau_car_ev_connector_type = my_entities.SensorPixelClauCarEvConnectorType
        sensor_pixel_clau_car_fuel = my_entities.SensorPixelClauCarFuel
        sensor_pixel_clau_car_fuel_type = my_entities.SensorPixelClauCarFuelType
        sensor_pixel_clau_car_odometer = my_entities.SensorPixelClauCarOdometer
        sensor_pixel_clau_screen_brightness = my_entities.SensorPixelClauScreenBrightness
        sensor_pixel_clau_screen_off_timeout = my_entities.SensorPixelClauScreenOffTimeout
        sensor_pixel_clau_do_not_disturb_sensor = my_entities.SensorPixelClauDoNotDisturbSensor
        sensor_pixel_clau_accent_color = my_entities.SensorPixelClauAccentColor
        binary_sensor_pixel_clau_work_profile = my_entities.BinarySensorPixelClauWorkProfile
        sensor_pixel_clau_geocoded_location = my_entities.SensorPixelClauGeocodedLocation
        binary_sensor_pixel_clau_device_locked = my_entities.BinarySensorPixelClauDeviceLocked
        binary_sensor_pixel_clau_device_secure = my_entities.BinarySensorPixelClauDeviceSecure
        binary_sensor_pixel_clau_keyguard_locked = my_entities.BinarySensorPixelClauKeyguardLocked
        binary_sensor_pixel_clau_keyguard_secure = my_entities.BinarySensorPixelClauKeyguardSecure
        sensor_pixel_clau_last_used_app = my_entities.SensorPixelClauLastUsedApp
        sensor_pixel_clau_last_reboot = my_entities.SensorPixelClauLastReboot
        sensor_pixel_clau_last_update_trigger = my_entities.SensorPixelClauLastUpdateTrigger
        sensor_pixel_clau_light_sensor = my_entities.SensorPixelClauLightSensor
        binary_sensor_pixel_clau_high_accuracy_mode = my_entities.BinarySensorPixelClauHighAccuracyMode
        sensor_pixel_clau_high_accuracy_update_interval = my_entities.SensorPixelClauHighAccuracyUpdateInterval
        binary_sensor_pixel_clau_mobile_data = my_entities.BinarySensorPixelClauMobileData
        binary_sensor_pixel_clau_mobile_data_roaming = my_entities.BinarySensorPixelClauMobileDataRoaming
        sensor_pixel_clau_wifi_connection = my_entities.SensorPixelClauWifiConnection
        sensor_pixel_clau_wifi_bssid = my_entities.SensorPixelClauWifiBssid
        sensor_pixel_clau_wifi_ip_address = my_entities.SensorPixelClauWifiIpAddress
        sensor_pixel_clau_wifi_link_speed = my_entities.SensorPixelClauWifiLinkSpeed
        binary_sensor_pixel_clau_wifi_state = my_entities.BinarySensorPixelClauWifiState
        sensor_pixel_clau_wifi_frequency = my_entities.SensorPixelClauWifiFrequency
        sensor_pixel_clau_wifi_signal_strength = my_entities.SensorPixelClauWifiSignalStrength
        sensor_pixel_clau_public_ip_address = my_entities.SensorPixelClauPublicIpAddress
        binary_sensor_pixel_clau_hotspot_state = my_entities.BinarySensorPixelClauHotspotState
        sensor_pixel_clau_network_type = my_entities.SensorPixelClauNetworkType
        sensor_pixel_clau_ipv6_addresses = my_entities.SensorPixelClauIpv6Addresses
        binary_sensor_pixel_clau_nfc_state = my_entities.BinarySensorPixelClauNfcState
        sensor_pixel_clau_next_alarm = my_entities.SensorPixelClauNextAlarm
        sensor_pixel_clau_last_notification = my_entities.SensorPixelClauLastNotification
        sensor_pixel_clau_last_removed_notification = my_entities.SensorPixelClauLastRemovedNotification
        sensor_pixel_clau_active_notification_count = my_entities.SensorPixelClauActiveNotificationCount
        sensor_pixel_clau_media_session = my_entities.SensorPixelClauMediaSession
        sensor_pixel_clau_phone_state = my_entities.SensorPixelClauPhoneState
        sensor_pixel_clau_sim_1 = my_entities.SensorPixelClauSim1
        sensor_pixel_clau_sim_2 = my_entities.SensorPixelClauSim2
        binary_sensor_pixel_clau_interactive = my_entities.BinarySensorPixelClauInteractive
        binary_sensor_pixel_clau_doze_mode = my_entities.BinarySensorPixelClauDozeMode
        binary_sensor_pixel_clau_power_save = my_entities.BinarySensorPixelClauPowerSave
        sensor_pixel_clau_pressure_sensor = my_entities.SensorPixelClauPressureSensor
        sensor_pixel_clau_proximity_sensor = my_entities.SensorPixelClauProximitySensor
        sensor_pixel_clau_steps_sensor = my_entities.SensorPixelClauStepsSensor
        sensor_pixel_clau_internal_storage = my_entities.SensorPixelClauInternalStorage
        sensor_pixel_clau_external_storage = my_entities.SensorPixelClauExternalStorage
        sensor_pixel_clau_current_time_zone = my_entities.SensorPixelClauCurrentTimeZone
        sensor_pixel_clau_mobile_rx_gb = my_entities.SensorPixelClauMobileRxGb
        sensor_pixel_clau_mobile_tx_gb = my_entities.SensorPixelClauMobileTxGb
        sensor_pixel_clau_total_rx_gb = my_entities.SensorPixelClauTotalRxGb
        sensor_pixel_clau_total_tx_gb = my_entities.SensorPixelClauTotalTxGb
        sensor_pixel_clau_remaining_charge_time = my_entities.SensorPixelClauRemainingChargeTime




class OfficeIrControl_64(models.Device):
    quirk = None
    quirk_attribute = None
    device_id = "bb08ffc8c23b4b1aae35d9ec7ce83b64"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        remote_office_ir_control = my_entities.RemoteOfficeIrControl




class TerraceSmartValve_40(models.Device):
    quirk = gen_devices.get_device_quirk("_TZE200_a7sghmms", "TS0601")
    quirk_attribute = "device_automation_triggers"
    device_id = "07b5758601724d0bcf4a9ce66bcbfe40"
    unique_id = "None"
    
    class entities:
        """Device entities"""
        sensor_tze200_a7sghmms_ts0601_rssi = my_entities.SensorTze200A7sghmmsTs0601Rssi
        sensor_tze200_a7sghmms_ts0601_lqi = my_entities.SensorTze200A7sghmmsTs0601Lqi
        sensor_terrace_smart_valve_battery = my_entities.SensorTerraceSmartValveBattery
        update_terrace_smart_valve_firmware = my_entities.UpdateTerraceSmartValveFirmware
        switch_terrace_smart_valve_switch = my_entities.SwitchTerraceSmartValveSwitch
        sensor_terrace_smart_valve_instantaneous_demand = my_entities.SensorTerraceSmartValveInstantaneousDemand
        sensor_terrace_smart_valve_summation_delivered = my_entities.SensorTerraceSmartValveSummationDelivered

    no_action = False
