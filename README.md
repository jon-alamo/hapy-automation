# ha_control

Basic lib to communicate with Home Assistant.

## Installation with pip

```bash
pip install git+https://github.com/jon-alamo/ha_control.git
```

## Usage

```bash
export HA_URL="http(s)://<home-assistant-address>:<port>"
export HA_TOKEN=<home-assistant-token>
```

```python
import ha_control
ha_control.entities.MyHomeAssistantLight.turn_on()
ha_control.entities.MyHomeAssistantLight.get_state()
```
