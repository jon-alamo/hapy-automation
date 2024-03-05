import hapy
from hapy.config import settings


if __name__ == '__main__':
    import automations, devices, entities
    ha_url, ha_token = settings.ha_url, settings.ha_token
    registry = hapy.get_registry()
    app = hapy.Application(automations, ha_url, ha_token, registry)
    app.run_forever()
