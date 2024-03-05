# hapyautomation
### Homeassistant (Pure)Python Automation Tool.

This tool implements a simple automation flow for Home Assistant using Python. 
It comes with a self-discovery feature that generates Python modules where 
entities, devices and services are type-hinted and bound statically, so the 
IDE can provide auto-completion and type checking when creating automations 
based on state changes in entities or action triggers in devices (if using ZHA 
Plugin).


## Installation with pip

```bash
pip install git+https://github.com/jon-alamo/hapy.git
```

## Usage

```python
import hapy

ha_url = "http(s)://<home-assistant-address>:<port>"
ha_token = "home-assistant-token"
directory = 'my_ha_instance'
hapy.generate_modules(directory, ha_url, ha_token)
```

```python
import entities
entities.MyHomeAssistantLight.services.turn_on()
```
