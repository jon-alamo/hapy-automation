# hapyautomation

Basic lib to communicate with Home Assistant.

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
