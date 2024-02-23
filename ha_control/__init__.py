import os
import json
import ha_control.register as register
import ha_control.generators as generators
import ha_control.ha_instance as ha_instance


def generate_modules(directory, ha_url, ha_token):
    os.makedirs(directory, exist_ok=True)
    secret_file = os.path.join(directory, '.secret')
    with open(secret_file, 'w', encoding="utf-8") as f:
        json.dump({'ha_url': ha_url, 'ha_token': ha_token}, f)
    ha = ha_instance.HAInstance(ha_url=ha_url, ha_token=ha_token)
    reg_data = register.get_registry(ha, directory=directory)
    domains_module_path = f'{directory}/domains.py'
    entities_module_path = f'{directory}/entities.py'
    generators.domains.write_domain_module(reg_data, domains_module_path)
    generators.entities.write_entities_module(
        reg_data, entities_module_path, domains_route='domains',
        secret_file=secret_file
    )
