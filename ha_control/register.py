import os


entity_keys = {
    'id': ['entity_id'],
    'unique_id': ['unique_id'],
    'name': ['name', 'friendly_name'],
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


def populate_dict(source_dict, mapping):
    target_dict = {}
    for target_key, source_keys in mapping:
        for source_key in source_keys:
            if source_key in source_dict:
                target_dict[target_key] = source_dict[source_key]
                break
        else:
            target_dict[target_key] = None
    return target_dict


def register_entity(entity_data, register):
    if 'entity_id' not in entity_data:
        raise ValueError('Entity data must contain an entity_id')

    entity_id = entity_data['entity_id']
    data_piece = {}

    if 'entities' not in register:
        register['entities'] = {}

    for target_key, source_keys in entity_keys:
        for source_key in source_keys:
            if source_key in entity_data:
                data_piece[target_key] = entity_data[source_key]
                break
        else:
            data_piece[target_key] = None

    # Register unique id
    if not data_piece['unique_key'] and entity_id in register['ent2unique']:
        data_piece['unique_key'] = register['ent2unique'][entity_id]
    elif entity_id not in register['ent2unique'] and data_piece['unique_key']:
        register['ent2unique'][entity_id] = data_piece['unique_key']

    # Register unique key
    if data_piece['unique_key']:
        register['unique_keys'][data_piece['unique_key']] = entity_id

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
    data_piece = {}
    for target_key, source_keys in device_keys:
        for source_key in source_keys:
            if source_key in device_data:
                data_piece[target_key] = device_data[source_key]
                break
        else:
            data_piece[target_key] = None

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
