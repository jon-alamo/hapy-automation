import ha_control


if __name__ == '__main__':
    import automations
    ha_url, ha_token = ha_control.get_secrets()
    registry = ha_control.get_registry()
    app = ha_control.Application(automations, ha_url, ha_token, registry)
    app.run_forever()
