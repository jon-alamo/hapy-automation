import ha_control
from ha_control.config import settings


if __name__ == '__main__':
    import automations
    ha_url, ha_token = settings.ha_url, settings.ha_token
    registry = ha_control.get_registry()
    app = ha_control.Application(automations, ha_url, ha_token, registry)
    app.run_forever()
