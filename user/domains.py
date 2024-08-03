import hapy.models as models


class PersistentNotification(models.Domain):

    def create(self, message: str = None, title: str = None, notification_id: str = None):
        """ Shows a notification on the **Notifications** panel.

        :message: Message body of the notification.
            {'text': None}
            Example: Please check your configuration.yaml.

        :title: Optional title of the notification.
            {'text': None}
            Example: Test notification

        :notification_id: ID of the notification. This new notification will overwrite an existing notification with the same ID.
            {'text': None}
            Example: 1234
        """

    def dismiss(self, notification_id: str = None):
        """ Removes a notification from the **Notifications** panel.

        :notification_id: ID of the notification to be removed.
            {'text': None}
            Example: 1234
        """

    def dismiss_all(self):
        """ Removes all notifications from the **Notifications** panel.
        """


class Homeassistant(models.Domain):

    def save_persistent_states(self):
        """ Saves the persistent states immediately. Maintains the normal periodic saving interval.
        """

    def turn_off(self):
        """ Generic service to turn devices off under any domain.
        """

    def turn_on(self):
        """ Generic service to turn devices on under any domain.
        """

    def toggle(self):
        """ Generic service to toggle devices on/off under any domain.
        """

    def stop(self):
        """ Stops Home Assistant.
        """

    def restart(self):
        """ Restarts Home Assistant.
        """

    def check_config(self):
        """ Checks the Home Assistant YAML-configuration files for errors. Errors will be shown in the Home Assistant logs.
        """

    def update_entity(self):
        """ Forces one or more entities to update its data.
        """

    def reload_core_config(self):
        """ Reloads the core configuration from the YAML-configuration.
        """

    def set_location(self, latitude: str = None, longitude: str = None, elevation: str = None):
        """ Updates the Home Assistant location.

        :latitude: Latitude of your location.
            {'number': {'mode': 'box', 'min': -90, 'max': 90, 'step': 'any'}}
            Example: 32.87336

        :longitude: Longitude of your location.
            {'number': {'mode': 'box', 'min': -180, 'max': 180, 'step': 'any'}}
            Example: 117.22743

        :elevation: Elevation of your location.
            {'number': {'mode': 'box', 'step': 'any'}}
            Example: 120
        """

    def reload_custom_templates(self):
        """ Reloads Jinja2 templates found in the `custom_templates` folder in your config. New values will be applied on the next render of the template.
        """

    def reload_config_entry(self, entry_id: str = None):
        """ Reloads the specified config entry.

        :entry_id: The configuration entry ID of the entry to be reloaded.
            {'text': None}
            Example: 8955375327824e14ba89e4b29cc3ec9a
        """

    def reload_all(self):
        """ Reload all YAML configuration that can be reloaded without restarting Home Assistant.
        """


class SystemLog(models.Domain):

    def clear(self):
        """ Clears all log entries.
        """

    def write(self, message: str = None, level: str = None, logger: str = None):
        """ Write log entry.

        :message: Message to log.
            {'text': None}
            Example: Something went wrong

        :level: Log level.
            {'select': {'options': ['debug', 'info', 'warning', 'error', 'critical'], 'translation_key': 'level'}}
            Example: 

        :logger: Logger name under which to log the message. Defaults to `system_log.external`.
            {'text': None}
            Example: mycomponent.myplatform
        """


class Logger(models.Domain):

    def set_default_level(self, level: str = None):
        """ Sets the default log level for integrations.

        :level: Default severity level for all integrations.
            {'select': {'options': ['debug', 'info', 'warning', 'error', 'fatal', 'critical'], 'translation_key': 'level'}}
            Example: 
        """

    def set_level(self):
        """ Sets the log level for one or more integrations.
        """


class Person(models.Domain):

    def reload(self):
        """ Reloads persons from the YAML-configuration.
        """


class Frontend(models.Domain):

    def set_theme(self, name: str = None, mode: str = None):
        """ Sets the default theme Home Assistant uses. Can be overridden by a user.

        :name: Name of a theme.
            {'theme': {'include_default': True}}
            Example: default

        :mode: Theme mode.
            {'select': {'options': ['dark', 'light'], 'translation_key': 'mode'}}
            Example: 
        """

    def reload_themes(self):
        """ Reloads themes from the YAML-configuration.
        """


class Recorder(models.Domain):

    def purge(self, keep_days: str = None, repack: str = None, apply_filter: str = None):
        """ Starts purge task - to clean up old data from your database.

        :keep_days: Number of days to keep the data in the database. Starting today, counting backward. A value of `7` means that everything older than a week will be purged.
            {'number': {'min': 0, 'max': 365, 'unit_of_measurement': 'days'}}
            Example: 

        :repack: Attempt to save disk space by rewriting the entire database file.
            {'boolean': None}
            Example: 

        :apply_filter: Apply `entity_id` and `event_type` filters in addition to time-based purge.
            {'boolean': None}
            Example: 
        """

    def purge_entities(self, domains: str = None, entity_globs: str = None, keep_days: str = None):
        """ Starts a purge task to remove the data related to specific entities from your database.

        :domains: List of domains for which the data needs to be removed from the recorder database.
            {'object': None}
            Example: sun

        :entity_globs: List of glob patterns used to select the entities for which the data is to be removed from the recorder database.
            {'object': None}
            Example: domain*.object_id*

        :keep_days: Number of days to keep the data for rows matching the filter. Starting today, counting backward. A value of `7` means that everything older than a week will be purged. The default of 0 days will remove all matching rows immediately.
            {'number': {'min': 0, 'max': 365, 'unit_of_measurement': 'days'}}
            Example: 
        """

    def enable(self):
        """ Starts the recording of events and state changes.
        """

    def disable(self):
        """ Stops the recording of events and state changes.
        """


class Hassio(models.Domain):

    def addon_start(self, addon: str = None):
        """ Starts an add-on.

        :addon: The add-on slug.
            {'addon': None}
            Example: core_ssh
        """

    def addon_stop(self, addon: str = None):
        """ Stops an add-on.

        :addon: The add-on slug.
            {'addon': None}
            Example: core_ssh
        """

    def addon_restart(self, addon: str = None):
        """ Restarts an add-on.

        :addon: The add-on slug.
            {'addon': None}
            Example: core_ssh
        """

    def addon_update(self, addon: str = None):
        """ Updates an add-on. This service should be used with caution since add-on updates can contain breaking changes. It is highly recommended that you review release notes/change logs before updating an add-on.

        :addon: The add-on slug.
            {'addon': None}
            Example: core_ssh
        """

    def addon_stdin(self, addon: str = None):
        """ Writes data to add-on stdin.

        :addon: The add-on slug.
            {'addon': None}
            Example: core_ssh
        """

    def host_shutdown(self):
        """ Powers off the host system.
        """

    def host_reboot(self):
        """ Reboots the host system.
        """

    def backup_full(self, name: str = None, password: str = None, compressed: str = None, location: str = None, homeassistant_exclude_database: str = None):
        """ Creates a full backup.

        :name: Optional (default = current date and time).
            {'text': None}
            Example: Backup 1

        :password: Password to protect the backup with.
            {'text': None}
            Example: password

        :compressed: Compresses the backup files.
            {'boolean': None}
            Example: 

        :location: Name of a backup network storage to host backups.
            {'backup_location': None}
            Example: my_backup_mount

        :homeassistant_exclude_database: Exclude the Home Assistant database file from backup
            {'boolean': None}
            Example: 
        """

    def backup_partial(self, homeassistant: str = None, homeassistant_exclude_database: str = None, addons: str = None, folders: str = None, name: str = None, password: str = None, compressed: str = None, location: str = None):
        """ Creates a partial backup.

        :homeassistant: Includes Home Assistant settings in the backup.
            {'boolean': None}
            Example: 

        :homeassistant_exclude_database: Exclude the Home Assistant database file from backup
            {'boolean': None}
            Example: 

        :addons: List of add-ons to include in the backup. Use the name slug of the add-on.
            {'object': None}
            Example: ['core_ssh', 'core_samba', 'core_mosquitto']

        :folders: List of directories to include in the backup.
            {'object': None}
            Example: ['homeassistant', 'share']

        :name: Optional (default = current date and time).
            {'text': None}
            Example: Partial backup 1

        :password: Password to protect the backup with.
            {'text': None}
            Example: password

        :compressed: Compresses the backup files.
            {'boolean': None}
            Example: 

        :location: Name of a backup network storage to host backups.
            {'backup_location': None}
            Example: my_backup_mount
        """

    def restore_full(self, slug: str = None, password: str = None):
        """ Restores from full backup.

        :slug: Slug of backup to restore from.
            {'text': None}
            Example: 

        :password: Optional password.
            {'text': None}
            Example: password
        """

    def restore_partial(self, slug: str = None, homeassistant: str = None, folders: str = None, addons: str = None, password: str = None):
        """ Restores from a partial backup.

        :slug: Slug of backup to restore from.
            {'text': None}
            Example: 

        :homeassistant: Restores Home Assistant.
            {'boolean': None}
            Example: 

        :folders: List of directories to include in the backup.
            {'object': None}
            Example: ['homeassistant', 'share']

        :addons: List of add-ons to include in the backup. Use the name slug of the add-on.
            {'object': None}
            Example: ['core_ssh', 'core_samba', 'core_mosquitto']

        :password: Optional password.
            {'text': None}
            Example: password
        """


class Update(models.Domain):

    def install(self, version: str = None, backup: str = None):
        """ Installs an update for this device or service.

        :version: The version to install. If omitted, the latest version will be installed.
            {'text': None}
            Example: 1.0.0

        :backup: If supported by the integration, this creates a backup before starting the update .
            {'boolean': None}
            Example: 
        """

    def skip(self):
        """ Marks currently available update as skipped.
        """

    def clear_skipped(self):
        """ Removes the skipped version marker from an update.
        """


class Cloud(models.Domain):

    def remote_connect(self):
        """ Makes the instance UI accessible from outside of the local network by using Home Assistant Cloud.
        """

    def remote_disconnect(self):
        """ Disconnects the Home Assistant UI from the Home Assistant Cloud. You will no longer be able to access your Home Assistant instance from outside your local network.
        """


class WakeOnLan(models.Domain):

    def send_magic_packet(self, mac: str = None, broadcast_address: str = None, broadcast_port: str = None):
        """ Sends a 'magic packet' to wake up a device with 'Wake-On-LAN' capabilities.

        :mac: MAC address of the device to wake up.
            {'text': None}
            Example: aa:bb:cc:dd:ee:ff

        :broadcast_address: Broadcast IP where to send the magic packet.
            {'text': None}
            Example: 192.168.255.255

        :broadcast_port: Port where to send the magic packet.
            {'number': {'min': 1, 'max': 65535}}
            Example: 
        """


class Smartir(models.Domain):

    def check_updates(self):
        """ Check for SmartIR updates.
        """

    def update_component(self):
        """ Update SmartIR component.
        """


class Climate(models.Domain):

    def turn_on(self):
        """ Turns climate device on.
        """

    def turn_off(self):
        """ Turns climate device off.
        """

    def toggle(self):
        """ Toggles climate device, from on to off, or off to on.
        """

    def set_hvac_mode(self, hvac_mode: str = None):
        """ Sets HVAC operation mode.

        :hvac_mode: HVAC operation mode.
            {'select': {'options': ['off', 'auto', 'cool', 'dry', 'fan_only', 'heat_cool', 'heat'], 'translation_key': 'hvac_mode'}}
            Example: 
        """

    def set_preset_mode(self, preset_mode: str = None):
        """ Sets preset mode.

        :preset_mode: Preset mode.
            {'text': None}
            Example: away
        """

    def set_aux_heat(self, aux_heat: str = None):
        """ Turns auxiliary heater on/off.

        :aux_heat: New value of auxiliary heater.
            {'boolean': None}
            Example: 
        """

    def set_temperature(self, temperature: str = None, target_temp_high: str = None, target_temp_low: str = None, hvac_mode: str = None):
        """ Sets target temperature.

        :temperature: Target temperature.
            {'number': {'min': 0, 'max': 250, 'step': 0.1, 'mode': 'box'}}
            Example: 

        :target_temp_high: High target temperature.
            {'number': {'min': 0, 'max': 250, 'step': 0.1, 'mode': 'box'}}
            Example: 

        :target_temp_low: Low target temperature.
            {'number': {'min': 0, 'max': 250, 'step': 0.1, 'mode': 'box'}}
            Example: 

        :hvac_mode: HVAC operation mode.
            {'select': {'options': ['off', 'auto', 'cool', 'dry', 'fan_only', 'heat_cool', 'heat'], 'translation_key': 'hvac_mode'}}
            Example: 
        """

    def set_humidity(self, humidity: str = None):
        """ Sets target humidity.

        :humidity: Target humidity.
            {'number': {'min': 30, 'max': 99, 'unit_of_measurement': '%'}}
            Example: 
        """

    def set_fan_mode(self, fan_mode: str = None):
        """ Sets fan operation mode.

        :fan_mode: Fan operation mode.
            {'text': None}
            Example: low
        """

    def set_swing_mode(self, swing_mode: str = None):
        """ Sets swing operation mode.

        :swing_mode: Swing operation mode.
            {'text': None}
            Example: horizontal
        """


class Conversation(models.Domain):

    def process(self, text: str = None, language: str = None, agent_id: str = None, conversation_id: str = None):
        """ Launches a conversation from a transcribed text.

        :text: Transcribed text input.
            {'text': None}
            Example: Turn all lights on

        :language: Language of text. Defaults to server language.
            {'text': None}
            Example: NL

        :agent_id: Conversation agent to process your request. The conversation agent is the brains of your assistant. It processes the incoming text commands.
            {'conversation_agent': None}
            Example: homeassistant

        :conversation_id: ID of the conversation, to be able to continue a previous conversation
            {'text': None}
            Example: my_conversation_1
        """

    def reload(self, language: str = None, agent_id: str = None):
        """ Reloads the intent configuration.

        :language: Language to clear cached intents for. Defaults to server language.
            {'text': None}
            Example: NL

        :agent_id: Conversation agent to reload.
            {'conversation_agent': None}
            Example: homeassistant
        """


class Scene(models.Domain):

    def reload(self):
        """ Reloads the scenes from the YAML-configuration.
        """

    def apply(self, entities: str = None, transition: str = None):
        """ Activates a scene with configuration.

        :entities: List of entities and their target state.
            {'object': None}
            Example: light.kitchen: "on"
light.ceiling:
  state: "on"
  brightness: 80


        :transition: Time it takes the devices to transition into the states defined in the scene.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example: 
        """

    def create(self, scene_id: str = None, entities: str = None, snapshot_entities: str = None):
        """ Creates a new scene.

        :scene_id: The entity ID of the new scene.
            {'text': None}
            Example: all_lights

        :entities: List of entities and their target state. If your entities are already in the target state right now, use `snapshot_entities` instead.
            {'object': None}
            Example: light.tv_back_light: "on"
light.ceiling:
  state: "on"
  brightness: 200


        :snapshot_entities: List of entities to be included in the snapshot. By taking a snapshot, you record the current state of those entities. If you do not want to use the current state of all your entities for this scene, you can combine the `snapshot_entities` with `entities`.
            {'entity': {'multiple': True}}
            Example: - light.ceiling
- light.kitchen

        """

    def delete(self):
        """ Deletes a dynamically created scene.
        """

    def turn_on(self, transition: str = None):
        """ Activates a scene.

        :transition: Time it takes the devices to transition into the states defined in the scene.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example: 
        """


class Switch(models.Domain):

    def turn_off(self):
        """ Turns a switch off.
        """

    def turn_on(self):
        """ Turns a switch on.
        """

    def toggle(self):
        """ Toggles a switch on/off.
        """


class Logbook(models.Domain):

    def log(self, name: str = None, message: str = None, entity_id: str = None, domain: str = None):
        """ Creates a custom entry in the logbook.

        :name: Custom name for an entity, can be referenced using an `entity_id`.
            {'text': None}
            Example: Kitchen

        :message: Message of the logbook entry.
            {'text': None}
            Example: is being used

        :entity_id: Entity to reference in the logbook entry.
            {'entity': None}
            Example: 

        :domain: Determines which icon is used in the logbook entry. The icon illustrates the integration domain related to this logbook entry.
            {'text': None}
            Example: light
        """


class Group(models.Domain):

    def reload(self):
        """ Reloads group configuration, entities, and notify services from YAML-configuration.
        """

    def set(self, object_id: str = None, name: str = None, icon: str = None, entities: str = None, add_entities: str = None, remove_entities: str = None, all: str = None):
        """ Creates/Updates a user group.

        :object_id: Object ID of this group. This object ID is used as part of the entity ID. Entity ID format: [domain].[object_id].
            {'text': None}
            Example: test_group

        :name: Name of the group.
            {'text': None}
            Example: My test group

        :icon: Name of the icon for the group.
            {'icon': None}
            Example: mdi:camera

        :entities: List of all members in the group. Cannot be used in combination with `Add entities` or `Remove entities`.
            {'entity': {'multiple': True}}
            Example: domain.entity_id1, domain.entity_id2

        :add_entities: List of members to be added to the group. Cannot be used in combination with `Entities` or `Remove entities`.
            {'entity': {'multiple': True}}
            Example: domain.entity_id1, domain.entity_id2

        :remove_entities: List of members to be removed from a group. Cannot be used in combination with `Entities` or `Add entities`.
            {'entity': {'multiple': True}}
            Example: domain.entity_id1, domain.entity_id2

        :all: Enable this option if the group should only be used when all entities are in state `on`.
            {'boolean': None}
            Example: 
        """

    def remove(self, object_id: str = None):
        """ Removes a group.

        :object_id: Object ID of this group. This object ID is used as part of the entity ID. Entity ID format: [domain].[object_id].
            {'object': None}
            Example: test_group
        """


class Ffmpeg(models.Domain):

    def start(self, entity_id: str = None):
        """ Sends a start command to a ffmpeg based sensor.

        :entity_id: Name of entity that will start. Platform dependent.
            {'entity': {'integration': 'ffmpeg', 'domain': 'binary_sensor'}}
            Example: 
        """

    def stop(self, entity_id: str = None):
        """ Sends a stop command to a ffmpeg based sensor.

        :entity_id: Name of entity that will stop. Platform dependent.
            {'entity': {'integration': 'ffmpeg', 'domain': 'binary_sensor'}}
            Example: 
        """

    def restart(self, entity_id: str = None):
        """ Sends a restart command to a ffmpeg based sensor.

        :entity_id: Name of entity that will restart. Platform dependent.
            {'entity': {'integration': 'ffmpeg', 'domain': 'binary_sensor'}}
            Example: 
        """


class InputText(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def set_value(self, value: str = None):
        """ Sets the value.

        :value: The target value.
            {'text': None}
            Example: This is an example text
        """


class Counter(models.Domain):

    def increment(self):
        """ Increments a counter.
        """

    def decrement(self):
        """ Decrements a counter.
        """

    def reset(self):
        """ Resets a counter.
        """

    def set_value(self, value: str = None):
        """ Sets the counter value.

        :value: The new counter value the entity should be set to.
            {'number': {'min': 0, 'max': 9223372036854775807, 'mode': 'box'}}
            Example: 
        """


class InputSelect(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def select_first(self):
        """ Selects the first option.
        """

    def select_last(self):
        """ Selects the last option.
        """

    def select_next(self, cycle: str = None):
        """ Select the next option.

        :cycle: If the option should cycle from the last to the first option on the list.
            {'boolean': None}
            Example: 
        """

    def select_option(self, option: str = None):
        """ Selects an option.

        :option: Option to be selected.
            {'text': None}
            Example: "Item A"
        """

    def select_previous(self, cycle: str = None):
        """ Selects the previous option.

        :cycle: If the option should cycle from the last to the first option on the list.
            {'boolean': None}
            Example: 
        """

    def set_options(self, options: str = None):
        """ Sets the options.

        :options: List of options.
            {'object': None}
            Example: ["Item A", "Item B", "Item C"]
        """


class Light(models.Domain):

    def turn_on(self, transition: str = None, rgb_color: str = None, rgbw_color: str = None, rgbww_color: str = None, color_name: str = None, hs_color: str = None, xy_color: str = None, color_temp: str = None, kelvin: str = None, brightness: str = None, brightness_pct: str = None, brightness_step: str = None, brightness_step_pct: str = None, white: str = None, profile: str = None, flash: str = None, effect: str = None):
        """ Turn on one or more lights and adjust properties of the light, even when they are turned on already.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example: 

        :rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
            {'color_rgb': None}
            Example: 

        :rgbw_color: The color in RGBW format. A list of four integers between 0 and 255 representing the values of red, green, blue, and white.
            {'object': None}
            Example: [255, 100, 100, 50]

        :rgbww_color: The color in RGBWW format. A list of five integers between 0 and 255 representing the values of red, green, blue, cold white, and warm white.
            {'object': None}
            Example: [255, 100, 100, 50, 70]

        :color_name: A human-readable color name.
            {'select': {'translation_key': 'color_name', 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}
            Example: 

        :hs_color: Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.
            {'object': None}
            Example: [300, 70]

        :xy_color: Color in XY-format. A list of two decimal numbers between 0 and 1.
            {'object': None}
            Example: [0.52, 0.43]

        :color_temp: Color temperature in mireds.
            {'color_temp': {'unit': 'mired', 'min': 153, 'max': 500}}
            Example: 

        :kelvin: Color temperature in Kelvin.
            {'color_temp': {'unit': 'kelvin', 'min': 2000, 'max': 6500}}
            Example: 

        :brightness: Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.
            {'number': {'min': 0, 'max': 255}}
            Example: 

        :brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 

        :brightness_step: Change brightness by an amount.
            {'number': {'min': -225, 'max': 255}}
            Example: 

        :brightness_step_pct: Change brightness by a percentage.
            {'number': {'min': -100, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 

        :white: Set the light to white mode.
            {'constant': {'value': True, 'label': 'Enabled'}}
            Example: 

        :profile: Name of a light profile to use.
            {'text': None}
            Example: relax

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example: 

        :effect: Light effect.
            {'text': None}
            Example: 
        """

    def turn_off(self, transition: str = None, flash: str = None):
        """ Turn off one or more lights.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example: 

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example: 
        """

    def toggle(self, transition: str = None, rgb_color: str = None, color_name: str = None, hs_color: str = None, xy_color: str = None, color_temp: str = None, kelvin: str = None, brightness: str = None, brightness_pct: str = None, white: str = None, profile: str = None, flash: str = None, effect: str = None):
        """ Toggles one or more lights, from on to off, or, off to on, based on their current state.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example: 

        :rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
            {'color_rgb': None}
            Example: [255, 100, 100]

        :color_name: A human-readable color name.
            {'select': {'translation_key': 'color_name', 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}
            Example: 

        :hs_color: Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.
            {'object': None}
            Example: [300, 70]

        :xy_color: Color in XY-format. A list of two decimal numbers between 0 and 1.
            {'object': None}
            Example: [0.52, 0.43]

        :color_temp: Color temperature in mireds.
            {'color_temp': None}
            Example: 

        :kelvin: Color temperature in Kelvin.
            {'color_temp': {'unit': 'kelvin', 'min': 2000, 'max': 6500}}
            Example: 

        :brightness: Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.
            {'number': {'min': 0, 'max': 255}}
            Example: 

        :brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 

        :white: Set the light to white mode.
            {'constant': {'value': True, 'label': 'Enabled'}}
            Example: 

        :profile: Name of a light profile to use.
            {'text': None}
            Example: relax

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example: 

        :effect: Light effect.
            {'text': None}
            Example: 
        """


class MediaPlayer(models.Domain):

    def turn_on(self):
        """ Turns on the power of the media player.
        """

    def turn_off(self):
        """ Turns off the power of the media player.
        """

    def toggle(self):
        """ Toggles a media player on/off.
        """

    def volume_up(self):
        """ Turns up the volume.
        """

    def volume_down(self):
        """ Turns down the volume.
        """

    def media_play_pause(self):
        """ Toggles play/pause.
        """

    def media_play(self):
        """ Starts playing.
        """

    def media_pause(self):
        """ Pauses.
        """

    def media_stop(self):
        """ Stops playing.
        """

    def media_next_track(self):
        """ Selects the next track.
        """

    def media_previous_track(self):
        """ Selects the previous track.
        """

    def clear_playlist(self):
        """ Clears the playlist.
        """

    def volume_set(self, volume_level: str = None):
        """ Sets the volume level.

        :volume_level: The volume. 0 is inaudible, 1 is the maximum volume.
            {'number': {'min': 0, 'max': 1, 'step': 0.01}}
            Example: 
        """

    def volume_mute(self, is_volume_muted: str = None):
        """ Mutes or unmutes the media player.

        :is_volume_muted: Defines whether or not it is muted.
            {'boolean': None}
            Example: 
        """

    def media_seek(self, seek_position: str = None):
        """ Allows you to go to a different part of the media that is currently playing.

        :seek_position: Target position in the currently playing media. The format is platform dependent.
            {'number': {'min': 0, 'max': 9223372036854775807, 'step': 0.01, 'mode': 'box'}}
            Example: 
        """

    def join(self, group_members: str = None):
        """ Groups media players together for synchronous playback. Only works on supported multiroom audio systems.

        :group_members: The players which will be synced with the playback specified in `target`.
            {'entity': {'multiple': True, 'domain': 'media_player'}}
            Example: - media_player.multiroom_player2
- media_player.multiroom_player3

        """

    def select_source(self, source: str = None):
        """ Sends the media player the command to change input source.

        :source: Name of the source to switch to. Platform dependent.
            {'text': None}
            Example: video1
        """

    def select_sound_mode(self, sound_mode: str = None):
        """ Selects a specific sound mode.

        :sound_mode: Name of the sound mode to switch to.
            {'text': None}
            Example: Music
        """

    def play_media(self, media_content_id: str = None, media_content_type: str = None, enqueue: str = None, announce: str = None):
        """ Starts playing specified media.

        :media_content_id: The ID of the content to play. Platform dependent.
            {'text': None}
            Example: https://home-assistant.io/images/cast/splash.png

        :media_content_type: The type of the content to play. Such as image, music, tv show, video, episode, channel, or playlist.
            {'text': None}
            Example: music

        :enqueue: If the content should be played now or be added to the queue.
            {'select': {'options': ['play', 'next', 'add', 'replace'], 'translation_key': 'enqueue'}}
            Example: 

        :announce: If the media should be played as an announcement.
            {'boolean': None}
            Example: true
        """

    def shuffle_set(self, shuffle: str = None):
        """ Playback mode that selects the media in randomized order.

        :shuffle: Whether or not shuffle mode is enabled.
            {'boolean': None}
            Example: 
        """

    def unjoin(self):
        """ Removes the player from a group. Only works on platforms which support player groups.
        """

    def repeat_set(self, repeat: str = None):
        """ Playback mode that plays the media in a loop.

        :repeat: Repeat mode to set.
            {'select': {'options': ['off', 'all', 'one'], 'translation_key': 'repeat'}}
            Example: 
        """


class Automation(models.Domain):

    def trigger(self, skip_condition: str = None):
        """ Triggers the actions of an automation.

        :skip_condition: Defines whether or not the conditions will be skipped.
            {'boolean': None}
            Example: 
        """

    def toggle(self):
        """ Toggles (enable / disable) an automation.
        """

    def turn_on(self):
        """ Enables an automation.
        """

    def turn_off(self, stop_actions: str = None):
        """ Disables an automation.

        :stop_actions: Stops currently running actions.
            {'boolean': None}
            Example: 
        """

    def reload(self):
        """ Reloads the automation configuration.
        """


class Script(models.Domain):

    def reload(self):
        """ Reloads all the available scripts.
        """

    def turn_on(self):
        """ Runs the sequence of actions defined in a script.
        """

    def turn_off(self):
        """ Stops a running script.
        """

    def toggle(self):
        """ Toggle a script. Starts it, if isn't running, stops it otherwise.
        """


class Zone(models.Domain):

    def reload(self):
        """ Reloads zones from the YAML-configuration.
        """


class InputNumber(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def set_value(self, value: str = None):
        """ Sets the value.

        :value: The target value.
            {'number': {'min': 0, 'max': 9223372036854775807, 'step': 0.001, 'mode': 'box'}}
            Example: 
        """

    def increment(self):
        """ Increments the value by 1 step.
        """

    def decrement(self):
        """ Decrements the current value by 1 step.
        """


class InputDatetime(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def set_datetime(self, date: str = None, time: str = None, datetime: str = None, timestamp: str = None):
        """ Sets the date and/or time.

        :date: The target date.
            {'text': None}
            Example: "2019-04-20"

        :time: The target time.
            {'time': None}
            Example: "05:04:20"

        :datetime: The target date & time.
            {'text': None}
            Example: "2019-04-20 05:04:20"

        :timestamp: The target date & time, expressed by a UNIX timestamp.
            {'number': {'min': 0, 'max': 9223372036854775807, 'mode': 'box'}}
            Example: 
        """


class InputButton(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def press(self):
        """ Mimics the physical button press on the device.
        """


class Schedule(models.Domain):

    def reload(self):
        """ Reloads schedules from the YAML-configuration.
        """


class Tts(models.Domain):

    def speak(self, media_player_entity_id: str = None, message: str = None, cache: str = None, language: str = None, options: str = None):
        """ Speaks something using text-to-speech on a media player.

        :media_player_entity_id: Media players to play the message.
            {'entity': {'domain': 'media_player'}}
            Example: 

        :message: The text you want to convert into speech so that you can listen to it on your device.
            {'text': None}
            Example: My name is hanna

        :cache: Stores this message locally so that when the text is requested again, the output can be produced more quickly.
            {'boolean': None}
            Example: 

        :language: Language to use for speech generation.
            {'text': None}
            Example: ru

        :options: A dictionary containing integration-specific options.
            {'object': None}
            Example: platform specific
        """

    def clear_cache(self):
        """ Removes all cached text-to-speech files and purges the memory.
        """

    def cloud_say(self, entity_id: str = None, message: str = None, cache: str = None, language: str = None, options: str = None):
        """ Say something using text-to-speech on a media player with cloud.

        :entity_id: 
            {'entity': {'domain': 'media_player'}}
            Example: 

        :message: 
            {'text': None}
            Example: My name is hanna

        :cache: 
            {'boolean': None}
            Example: 

        :language: 
            {'text': None}
            Example: ru

        :options: 
            {'object': None}
            Example: platform specific
        """


class Timer(models.Domain):

    def reload(self):
        """ Reloads timers from the YAML-configuration.
        """

    def start(self, duration: str = None):
        """ Starts a timer.

        :duration: Duration the timer requires to finish. [optional].
            {'text': None}
            Example: 00:01:00 or 60
        """

    def pause(self):
        """ Pauses a timer.
        """

    def cancel(self):
        """ Cancels a timer.
        """

    def finish(self):
        """ Finishes a timer.
        """

    def change(self, duration: str = None):
        """ Changes a timer.

        :duration: Duration to add or subtract to the running timer.
            {'text': None}
            Example: 00:01:00, 60 or -60
        """


class InputBoolean(models.Domain):

    def reload(self):
        """ Reloads helpers from the YAML-configuration.
        """

    def turn_on(self):
        """ Turns on the helper.
        """

    def turn_off(self):
        """ Turns off the helper.
        """

    def toggle(self):
        """ Toggles the helper on/off.
        """


class Weather(models.Domain):

    def get_forecast(self, type: str = None):
        """ Get weather forecast.

        :type: Forecast type: daily, hourly or twice daily.
            {'select': {'options': ['daily', 'hourly', 'twice_daily'], 'translation_key': 'forecast_type'}}
            Example: 
        """

    def get_forecasts(self, type: str = None):
        """ Get weather forecasts.

        :type: Forecast type: daily, hourly or twice daily.
            {'select': {'options': ['daily', 'hourly', 'twice_daily'], 'translation_key': 'forecast_type'}}
            Example: 
        """


class Securitas(models.Domain):

    def refresh_alarm_status(self):
        """ 
        """


class AlarmControlPanel(models.Domain):

    def alarm_disarm(self, code: str = None):
        """ Disarms the alarm.

        :code: Code to disarm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_arm_home(self, code: str = None):
        """ Sets the alarm to: _armed, but someone is home_.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_arm_away(self, code: str = None):
        """ Sets the alarm to: _armed, no one home_.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_arm_night(self, code: str = None):
        """ Sets the alarm to: _armed for the night_.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_arm_vacation(self, code: str = None):
        """ Sets the alarm to: _armed for vacation_.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_arm_custom_bypass(self, code: str = None):
        """ Arms the alarm while allowing to bypass a custom area.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """

    def alarm_trigger(self, code: str = None):
        """ Enables an external alarm trigger.

        :code: Code to arm the alarm.
            {'text': None}
            Example: 1234
        """


class DeviceTracker(models.Domain):

    def see(self, mac: str = None, dev_id: str = None, host_name: str = None, location_name: str = None, gps: str = None, gps_accuracy: str = None, battery: str = None):
        """ Records a seen tracked device.

        :mac: MAC address of the device.
            {'text': None}
            Example: FF:FF:FF:FF:FF:FF

        :dev_id: ID of the device (find the ID in `known_devices.yaml`).
            {'text': None}
            Example: phonedave

        :host_name: Hostname of the device.
            {'text': None}
            Example: Dave

        :location_name: Name of the location where the device is located. The options are: `home`, `not_home`, or the name of the zone.
            {'text': None}
            Example: home

        :gps: GPS coordinates where the device is located, specified by latitude and longitude (for example: [51.513845, -0.100539]).
            {'object': None}
            Example: [51.509802, -0.086692]

        :gps_accuracy: Accuracy of the GPS coordinates.
            {'number': {'min': 0, 'mode': 'box', 'unit_of_measurement': 'm'}}
            Example: 

        :battery: Battery level of the device.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """


class Remote(models.Domain):

    def turn_off(self):
        """ Turns the device off.
        """

    def turn_on(self, activity: str = None):
        """ Sends the power on command.

        :activity: Activity ID or activity name to be started.
            {'text': None}
            Example: BedroomTV
        """

    def toggle(self):
        """ Toggles a device on/off.
        """

    def send_command(self, device: str = None, command: str = None, num_repeats: str = None, delay_secs: str = None, hold_secs: str = None):
        """ Sends a command or a list of commands to a device.

        :device: Device ID to send command to.
            {'text': None}
            Example: 32756745

        :command: A single command or a list of commands to send.
            {'object': None}
            Example: Play

        :num_repeats: The number of times you want to repeat the commands.
            {'number': {'min': 0, 'max': 255}}
            Example: 

        :delay_secs: The time you want to wait in between repeated commands.
            {'number': {'min': 0, 'max': 60, 'step': 0.1, 'unit_of_measurement': 'seconds'}}
            Example: 

        :hold_secs: The time you want to have it held before the release is send.
            {'number': {'min': 0, 'max': 60, 'step': 0.1, 'unit_of_measurement': 'seconds'}}
            Example: 
        """

    def learn_command(self, device: str = None, command: str = None, command_type: str = None, alternative: str = None, timeout: str = None):
        """ Learns a command or a list of commands from a device.

        :device: Device ID to learn command from.
            {'text': None}
            Example: television

        :command: A single command or a list of commands to learn.
            {'object': None}
            Example: Turn on

        :command_type: The type of command to be learned.
            {'select': {'options': ['ir', 'rf']}}
            Example: 

        :alternative: If code must be stored as an alternative. This is useful for discrete codes. Discrete codes are used for toggles that only perform one function. For example, a code to only turn a device on. If it is on already, sending the code won't change the state.
            {'boolean': None}
            Example: 

        :timeout: Timeout for the command to be learned.
            {'number': {'min': 0, 'max': 60, 'step': 5, 'unit_of_measurement': 'seconds'}}
            Example: 
        """

    def delete_command(self, device: str = None, command: str = None):
        """ Deletes a command or a list of commands from the database.

        :device: Device from which commands will be deleted.
            {'text': None}
            Example: television

        :command: The single command or the list of commands to be deleted.
            {'object': None}
            Example: Mute
        """


class Notify(models.Domain):

    def persistent_notification(self, message: str = None, title: str = None, data: str = None):
        """ Sends a notification that is visible in the **Notifications** panel.

        :message: Message body of the notification.
            {'text': None}
            Example: The garage door has been open for 10 minutes.

        :title: Title of the notification.
            {'text': None}
            Example: Your Garage Door Friend

        :data: Some integrations provide extended functionality. For information on how to use _data_, refer to the integration documentation..
            {'object': None}
            Example: platform specific
        """

    def mobile_app_mi9_clau(self, message: str = None, title: str = None, target: str = None, data: str = None):
        """ Sends a notification message using the mobile_app_mi9_clau integration.

        :message: 
            {'text': None}
            Example: The garage door has been open for 10 minutes.

        :title: 
            {'text': None}
            Example: Your Garage Door Friend

        :target: 
            {'object': None}
            Example: platform specific

        :data: 
            {'object': None}
            Example: platform specific
        """

    def mobile_app_s23_joni(self, message: str = None, title: str = None, target: str = None, data: str = None):
        """ Sends a notification message using the mobile_app_s23_joni integration.

        :message: 
            {'text': None}
            Example: The garage door has been open for 10 minutes.

        :title: 
            {'text': None}
            Example: Your Garage Door Friend

        :target: 
            {'object': None}
            Example: platform specific

        :data: 
            {'object': None}
            Example: platform specific
        """

    def mobile_app_pixel_clau(self, message: str = None, title: str = None, target: str = None, data: str = None):
        """ Sends a notification message using the mobile_app_pixel_clau integration.

        :message: 
            {'text': None}
            Example: The garage door has been open for 10 minutes.

        :title: 
            {'text': None}
            Example: Your Garage Door Friend

        :target: 
            {'object': None}
            Example: platform specific

        :data: 
            {'object': None}
            Example: platform specific
        """

    def notify(self, message: str = None, title: str = None, target: str = None, data: str = None):
        """ Sends a notification message using the notify service.

        :message: 
            {'text': None}
            Example: The garage door has been open for 10 minutes.

        :title: 
            {'text': None}
            Example: Your Garage Door Friend

        :target: 
            {'object': None}
            Example: platform specific

        :data: 
            {'object': None}
            Example: platform specific
        """


class Zha(models.Domain):

    def set_lock_user_code(self, code_slot: str = None, user_code: str = None):
        """ Sets a user code on a lock.

        :code_slot: Code slot to set the code in.
            {'text': None}
            Example: 1

        :user_code: Code to set.
            {'text': None}
            Example: 1234
        """

    def enable_lock_user_code(self, code_slot: str = None):
        """ Enables a user code on a lock.

        :code_slot: Code slot to enable.
            {'text': None}
            Example: 1
        """

    def disable_lock_user_code(self, code_slot: str = None):
        """ Disables a user code on a lock.

        :code_slot: Code slot to disable.
            {'text': None}
            Example: 1
        """

    def clear_lock_user_code(self, code_slot: str = None):
        """ Clears a user code from a lock.

        :code_slot: Code slot to clear code from.
            {'text': None}
            Example: 1
        """

    def permit(self, duration: str = None, ieee: str = None, source_ieee: str = None, install_code: str = None, qr_code: str = None):
        """ Allows nodes to join the Zigbee network.

        :duration: Time to permit joins.
            {'number': {'min': 0, 'max': 254, 'unit_of_measurement': 'seconds'}}
            Example: 

        :ieee: IEEE address of the node permitting new joins.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34

        :source_ieee: IEEE address of the joining device (must be used with the install code).
            {'text': None}
            Example: 00:0a:bf:00:01:10:23:35

        :install_code: Install code of the joining device (must be used with the source_ieee).
            {'text': None}
            Example: 1234-5678-1234-5678-AABB-CCDD-AABB-CCDD-EEFF

        :qr_code: Value of the QR install code (different between vendors).
            {'text': None}
            Example: Z:000D6FFFFED4163B$I:52797BF4A5084DAA8E1712B61741CA024051
        """

    def remove(self, ieee: str = None):
        """ Removes a node from the Zigbee network.

        :ieee: IEEE address of the node to remove.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34
        """

    def set_zigbee_cluster_attribute(self, ieee: str = None, endpoint_id: str = None, cluster_id: str = None, cluster_type: str = None, attribute: str = None, value: str = None, manufacturer: str = None):
        """ Sets an attribute value for the specified cluster on the specified entity.

        :ieee: IEEE address for the device.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34

        :endpoint_id: Endpoint ID for the cluster.
            {'number': {'min': 1, 'max': 65535, 'mode': 'box'}}
            Example: 

        :cluster_id: ZCL cluster to retrieve attributes for.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :cluster_type: Type of the cluster.
            {'select': {'options': ['in', 'out']}}
            Example: 

        :attribute: ID of the attribute to set.
            {'number': {'min': 1, 'max': 65535}}
            Example: 0

        :value: Value to write to the attribute.
            {'text': None}
            Example: 1

        :manufacturer: Manufacturer code. Use a value of "-1" to force no code to be set.
            {'text': None}
            Example: 252
        """

    def issue_zigbee_cluster_command(self, ieee: str = None, endpoint_id: str = None, cluster_id: str = None, cluster_type: str = None, command: str = None, command_type: str = None, args: str = None, params: str = None, manufacturer: str = None):
        """ Issues a command on the specified cluster on the specified entity.

        :ieee: IEEE address for the device.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34

        :endpoint_id: Endpoint ID for the cluster.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :cluster_id: ZCL cluster to retrieve attributes for.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :cluster_type: Type of the cluster.
            {'select': {'options': ['in', 'out']}}
            Example: 

        :command: ID of the command to execute.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :command_type: Type of the command to execute.
            {'select': {'options': ['client', 'server']}}
            Example: 

        :args: Arguments to pass to the command.
            {'object': None}
            Example: [arg1, arg2, argN]

        :params: Parameters to pass to the command.
            {'object': None}
            Example: 

        :manufacturer: Manufacturer code. Use a value of "-1" to force no code to be set.
            {'text': None}
            Example: 252
        """

    def issue_zigbee_group_command(self, group: str = None, cluster_id: str = None, cluster_type: str = None, command: str = None, args: str = None, manufacturer: str = None):
        """ Issue command on the specified cluster on the specified group.

        :group: Hexadecimal address of the group.
            {'text': None}
            Example: 546

        :cluster_id: ZCL cluster to send command to.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :cluster_type: Type of the cluster.
            {'select': {'options': ['in', 'out']}}
            Example: 

        :command: ID of the command to execute.
            {'number': {'min': 1, 'max': 65535}}
            Example: 

        :args: Arguments to pass to the command.
            {'object': None}
            Example: [arg1, arg2, argN]

        :manufacturer: Manufacturer code. Use a value of "-1" to force no code to be set.
            {'text': None}
            Example: 252
        """

    def warning_device_squawk(self, ieee: str = None, mode: str = None, strobe: str = None, level: str = None):
        """ This service uses the WD capabilities to emit a quick audible/visible pulse called a "squawk". The squawk command has no effect if the WD is currently active (warning in progress).

        :ieee: IEEE address for the device.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34

        :mode: The Squawk Mode field is used as a 4-bit enumeration, and can have one of the values shown in Table 8-24 of the ZCL spec - Squawk Mode Field. The exact operation of each mode (how the WD “squawks”) is implementation specific.
            {'number': {'min': 0, 'max': 1, 'mode': 'box'}}
            Example: 

        :strobe: The strobe field is used as a Boolean, and determines if the visual indication is also required in addition to the audible squawk, as shown in Table 8-25 of the ZCL spec - Strobe Bit.
            {'number': {'min': 0, 'max': 1, 'mode': 'box'}}
            Example: 

        :level: The squawk level field is used as a 2-bit enumeration, and determines the intensity of audible squawk sound as shown in Table 8-26 of the ZCL spec - Squawk Level Field Values.
            {'number': {'min': 0, 'max': 3, 'mode': 'box'}}
            Example: 
        """

    def warning_device_warn(self, ieee: str = None, mode: str = None, strobe: str = None, level: str = None, duration: str = None, duty_cycle: str = None, intensity: str = None):
        """ This service starts the operation of the warning device. The warning device alerts the surrounding area by audible (siren) and visual (strobe) signals.

        :ieee: IEEE address for the device.
            {'text': None}
            Example: 00:0d:6f:00:05:7d:2d:34

        :mode: The Warning Mode field is used as a 4-bit enumeration, can have one of the values 0-6 defined below in table 8-20 of the ZCL spec. The exact behavior of the warning device in each mode is according to the relevant security standards.
            {'number': {'min': 0, 'max': 6, 'mode': 'box'}}
            Example: 

        :strobe: The Strobe field is used as a 2-bit enumeration, and determines if the visual indication is required in addition to the audible siren, as indicated in Table 8-21 of the ZCL spec. "0" means no strobe, "1" means strobe. If the strobe field is “1” and the Warning Mode is “0” (“Stop”), then only the strobe is activated.
            {'number': {'min': 0, 'max': 1, 'mode': 'box'}}
            Example: 

        :level: The Siren Level field is used as a 2-bit enumeration, and indicates the intensity of audible squawk sound as shown in Table 8-22 of the ZCL spec.
            {'number': {'min': 0, 'max': 3, 'mode': 'box'}}
            Example: 

        :duration: Requested duration of warning, in seconds (16 bit). If both Strobe and Warning Mode are "0" this field is ignored.
            {'number': {'min': 0, 'max': 65535, 'unit_of_measurement': 'seconds'}}
            Example: 

        :duty_cycle: Indicates the length of the flash cycle. This allows you to vary the flash duration for different alarm types (e.g., fire, police, burglar). The valid range is 0-100 in increments of 10. All other values must be rounded to the nearest valid value. Strobe calculates a duty cycle over a duration of one second. The ON state must precede the OFF state. For example, if the Strobe Duty Cycle field specifies “40,”, then the strobe flashes ON for 4/10ths of a second and then turns OFF for 6/10ths of a second.
            {'number': {'min': 0, 'max': 100, 'step': 10}}
            Example: 

        :intensity: Indicates the intensity of the strobe as shown in Table 8-23 of the ZCL spec. This attribute is designed to vary the output of the strobe (i.e., brightness) and not its frequency, which is detailed in section 8.4.2.3.1.6 of the ZCL spec.
            {'number': {'min': 0, 'max': 3, 'mode': 'box'}}
            Example: 
        """


class Button(models.Domain):

    def press(self):
        """ Press the button entity.
        """


class Cover(models.Domain):

    def open_cover(self):
        """ Opens a cover.
        """

    def close_cover(self):
        """ Closes a cover.
        """

    def set_cover_position(self, position: str = None):
        """ Moves a cover to a specific position.

        :position: Target position.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """

    def stop_cover(self):
        """ Stops the cover movement.
        """

    def toggle(self):
        """ Toggles a cover open/closed.
        """

    def open_cover_tilt(self):
        """ Tilts a cover open.
        """

    def close_cover_tilt(self):
        """ Tilts a cover to close.
        """

    def stop_cover_tilt(self):
        """ Stops a tilting cover movement.
        """

    def set_cover_tilt_position(self, tilt_position: str = None):
        """ Moves a cover tilt to a specific position.

        :tilt_position: Target tilt positition.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """

    def toggle_cover_tilt(self):
        """ Toggles a cover tilt open/closed.
        """


class Fan(models.Domain):

    def turn_on(self, percentage: str = None, preset_mode: str = None):
        """ Turns fan on.

        :percentage: Speed of the fan.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 

        :preset_mode: Preset mode.
            {'text': None}
            Example: auto
        """

    def turn_off(self):
        """ Turns fan off.
        """

    def toggle(self):
        """ Toggles the fan on/off.
        """

    def increase_speed(self, percentage_step: str = None):
        """ Increases the speed of the fan.

        :percentage_step: Increases the speed by a percentage step.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """

    def decrease_speed(self, percentage_step: str = None):
        """ Decreases the speed of the fan.

        :percentage_step: Decreases the speed by a percentage step.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """

    def oscillate(self, oscillating: str = None):
        """ Controls oscillatation of the fan.

        :oscillating: Turn on/off oscillation.
            {'boolean': None}
            Example: 
        """

    def set_direction(self, direction: str = None):
        """ Sets the fan rotation direction.

        :direction: Direction to rotate.
            {'select': {'options': ['forward', 'reverse'], 'translation_key': 'direction'}}
            Example: 
        """

    def set_percentage(self, percentage: str = None):
        """ Sets the fan speed.

        :percentage: Speed of the fan.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example: 
        """

    def set_preset_mode(self, preset_mode: str = None):
        """ Sets preset mode.

        :preset_mode: Preset mode.
            {'text': None}
            Example: auto
        """


class Lock(models.Domain):

    def unlock(self, code: str = None):
        """ Unlocks a lock.

        :code: Code used to unlock the lock.
            {'text': None}
            Example: 1234
        """

    def lock(self, code: str = None):
        """ Locks a lock.

        :code: Code used to lock the lock.
            {'text': None}
            Example: 1234
        """

    def open(self, code: str = None):
        """ Opens a lock.

        :code: Code used to open the lock.
            {'text': None}
            Example: 1234
        """


class Number(models.Domain):

    def set_value(self, value: str = None):
        """ Sets the value of a number.

        :value: The target value to set.
            {'text': None}
            Example: 42
        """


class Select(models.Domain):

    def select_first(self):
        """ Selects the first option.
        """

    def select_last(self):
        """ Selects the last option.
        """

    def select_next(self, cycle: str = None):
        """ Selects the next option.

        :cycle: If the option should cycle from the last to the first.
            {'boolean': None}
            Example: 
        """

    def select_option(self, option: str = None):
        """ Selects an option.

        :option: Option to be selected.
            {'text': None}
            Example: "Item A"
        """

    def select_previous(self, cycle: str = None):
        """ Selects the previous option.

        :cycle: If the option should cycle from the first to the last.
            {'boolean': None}
            Example: 
        """


class Siren(models.Domain):

    def turn_on(self, tone: str = None, volume_level: str = None, duration: str = None):
        """ Turns the siren on.

        :tone: The tone to emit. When `available_tones` property is a map, either the key or the value can be used. Must be supported by the integration.
            {'text': None}
            Example: fire

        :volume_level: The volume. 0 is inaudible, 1 is the maximum volume. Must be supported by the integration.
            {'number': {'min': 0, 'max': 1, 'step': 0.05}}
            Example: 0.5

        :duration: Number of seconds the sound is played. Must be supported by the integration.
            {'text': None}
            Example: 15
        """

    def turn_off(self):
        """ Turns the siren off.
        """

    def toggle(self):
        """ Toggles the siren on/off.
        """