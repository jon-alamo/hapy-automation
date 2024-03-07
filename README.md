# hapy-automation

#### !! project under development. It may contain bugs or unexpected behaviours

### Homeassistant Python Automation Tool.

This tool implements a simple automation flow for Home Assistant using Python. 
It comes with a self-discovery feature that generates Python modules where 
entities, devices and services are type-hinted and bound statically, so the 
IDE can provide auto-completion and type checking when creating automations 
based on state changes in entities or action triggers in devices (if using ZHA 
Plugin).


## Installation with pip

```bash
pip install git+https://github.com/jon-alamo/hapy-automation.git
```

## First steps

### Starting new project
To start a new automation project, first create a .env file with the following:
```bash
HA_API_URL=http://<your-ha-instance>:<port>/api
HA_WS_URL=ws://<your-ha-instance>:<port>/api/websocket
HA_TOKEN=<your-ha-token>
LOG_LEVEL=INFO
TIMEZONE=Europe/Madrid
```

Then, create the project structure and self-discovering feature by running the 
following command from the directory where the .env file is located:
```bash
hapy-start
```

To create a project in different directory, use:
```bash
hapy-start --directory path/to/new/project
```

### Automations
By default, the `hapy-start` command creates an `automations.py` file in the 
project root. For readability and maintainability, automations can be created 
in separate files as long as they are referenced under the `automations` 
namespace imported when the project is started. So for instance, 
`automations.py` file can be replaced by a python package named `automations` 
containing several modules with automations and a `__init__.py` which imports 
all the modules.

#### Defining some automations

Whichever module containing automations to be used, should look like follows:

```python
import hapy
import entities
import devices


class OnMySwitchOn(hapy.Automation):

    def init_condition(self):
        return devices.MySwitch.remote_button_short_press_turn_on

    def action(self):
        entities.MyLight.turn_on()


class OnMySwitchDimUp(hapy.Automation):

    def init_condition(self):
        return devices.MySwitch.remote_button_long_press_dim_up

    def exit_condition(self):
        return devices.MySwitch.remote_button_long_release_dim_up
    
    def action(self):
        entities.MyLight.services.turn_on(brightness_step_pct=10)


class OnMyLightTurnedOn(hapy.Automation):

    def init_condition(self):
        return entities.MyLight.state.changed(old_value='off', new_value='on')

    def action(self):
        entities.MySecondLight.services.turn_off()
```

### Running app

Tu run the app, just execute the following command from the project root:

```bash
python application.py
```

At this stage of the application, automation files are watched for changes and
reloaded automatically when detected. 


### Updating entities and devices

Tu update entities and devices in an existing project, just execute the 
`hapy-start` command from the project root. This will execute the self-discovery
feature and update the entities and devices modules with the new entities and
devices found in the Home Assistant instance. At this point, entities that 
changed their entity_id in Home Assistant will disappear from the entities.py 
module and therefore, any automation using them will raise an error.
