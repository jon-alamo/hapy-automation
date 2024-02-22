import ha_control.register as register
import ha_control.generators as generators
import ha_control.ha_websocket as ha_websocket
import ha_control.ha_restapi as ha_restapi


def generate_modules(directory):
    domains = ha_restapi.get_services()
    devices = ha_websocket.get_devices()
    entities = ha_websocket.get_entities()
    states = ha_restapi.get_states()
    reg_data = {}
    reg_data = register.register_domains(domains, reg_data)
    reg_data = register.register_entities(entities, reg_data)
    reg_data = register.register_states(states, reg_data)
    reg_data = register.register_devices(devices, reg_data)

    domains_module_path = f'{directory}/domains.py'
    entities_module_path = f'{directory}/entities.py'
    generators.domains.write_domain_module(reg_data, domains_module_path)
    generators.entities.write_entities_module(
        reg_data, entities_module_path, domains_route='domains'
    )
