import hapy
from hapy.config import settings


if __name__ == '__main__':
    import automations, devices, entities
    ha_api_url = settings.ha_api_url
    ha_ws_url = settings.ha_ws_url
    ha_token = settings.ha_token
    registry = hapy.get_registry()
    app = hapy.Application(automations, ha_api_url, ha_ws_url, ha_token, registry)
    app.run_forever()
