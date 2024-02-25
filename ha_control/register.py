import json
import zhaquirks
import pkgutil
import importlib
import inspect


entity_keys = {
    'id': ['entity_id'],
    'unique_id': ['unique_id'],
    'name': ['name', 'attributes.friendly_name'],
    'attributes': ['attributes'],
    'device_id': ['device_id'],
    'area_id': ['area_id']
}

device_keys = {
    'id': ['id'],
    'name': ['name_by_user', 'name'],
    'model': ['model'],
    'manufacturer': ['manufacturer'],
    'area_id': ['area_id']
}

domain_mapping = {
    'services': ['services'],
}


def find_value(data, key):
    if key in data:
        return data[key]
    keys = key.split('.')
    for k in keys:
        if k in data:
            return find_value(data[k], '.'.join(keys[1:]))
        else:
            return None


def populate_dict(source_dict, mapping):
    target_dict = {}
    for target_key, source_keys in mapping.items():
        for source_key in source_keys:
            if value := find_value(source_dict, source_key):
                target_dict[target_key] = value
                break
        else:
            target_dict[target_key] = None
    return target_dict


def register_entity(entity_data, register):
    if 'entity_id' not in entity_data:
        raise ValueError('Entity data must contain an entity_id')

    entity_id = entity_data['entity_id']

    if 'entities' not in register:
        register['entities'] = {}

    data_piece = populate_dict(entity_data, entity_keys)

    # Register entity
    if entity_id not in register['entities']:
        register['entities'][entity_id] = data_piece
    else:
        update_data = {k: v for k, v in data_piece.items() if v is not None}
        register['entities'][entity_id].update(update_data)

    return register


def register_device(device_data, register):
    if 'id' not in device_data:
        return
    device_id = device_data['id']
    data_piece = populate_dict(device_data, device_keys)

    if 'devices' not in register:
        register['devices'] = {}

    if data_piece['id'] is not None:
        register['devices'][device_id] = data_piece
    return register


def register_domain(domain_data: dict, register: dict):
    if 'domain' not in domain_data:
        return
    domain = domain_data['domain']

    if 'domains' not in register:
        register['domains'] = {}

    if domain not in register['domains']:
        register['domains'][domain] = domain_data['services']
    else:
        update_data = {k: v for k, v in domain_data['services'].items() if v is not None}
        register['domains'][domain].update(update_data)


def register_domains(domains: list, register: dict):
    for domain in domains:
        register_domain(domain, register)
    return register


def register_entities(entities: dict, register: dict):
    for entity in entities['result']:
        register_entity(entity, register)
    return register


def register_states(states: dict, register: dict):
    for state in states:
        register_entity(state, register)
    return register


def register_devices(devices: dict, register: dict):
    for device in devices['result']:
        register_device(device, register)
    return register


def register_signatures(register: dict):
    if 'device_signatures' not in register:
        register['device_signatures'] = {}

    for importer, package_name, ispkg in pkgutil.walk_packages(
            path=zhaquirks.__path__, onerror=lambda x: None
    ):
        package_route = f"zhaquirks.{package_name}"
        package = importlib.import_module(package_route)
        if not ispkg:
            continue
        for _, module, is_pkg in pkgutil.walk_packages(package.__path__):
            if is_pkg:
                continue
            module_route = f"{package_route}.{module}"
            module = importlib.import_module(module_route)
            for class_name, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, 'signature') and obj.signature is not None:
                    device_key = zhaquirks.const.MODELS_INFO
                    if device_key not in obj.signature:
                        continue
                    for device_id in obj.signature[device_key]:
                        if not device_id:
                            continue
                        key = ' '.join(filter(lambda x: x is not None, device_id))
                        location = [module_route, class_name]
                        register['device_signatures'][key] = location

    return register


def get_registry(instance, directory: None):
    domains = instance.get_services()
    devices = instance.get_devices()
    entities = instance.get_entities()
    states = instance.get_states()
    reg_data = {}
    reg_data = register_domains(domains, reg_data)
    reg_data = register_entities(entities, reg_data)
    reg_data = register_states(states, reg_data)
    reg_data = register_devices(devices, reg_data)
    reg_data = register_signatures(reg_data)

    if directory:
        with open(f'{directory}/.registry', 'w', encoding="utf-8") as f:
            json.dump(reg_data, f)

    return reg_data
