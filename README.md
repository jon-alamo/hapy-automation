# ha_control

Basic lib to communicate with Home Assistant.

## Installation with pip

```bash
pip install git+https://github.com/jon-alamo/ha_control.git
```

## Usage

```python
import ha_control
ha_url="http(s)://<home-assistant-address>:<port>"
ha_token="home-assistant-token"
directory = 'my_ha_instance'
ha_control.generate_modules(directory, ha_url, ha_token)
```

```python
import my_ha_instance.entities as entities
entities.MyHomeAssistantLight.services.turn_on()
```
