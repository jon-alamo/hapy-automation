import ha_control.helpers as helpers


entity_tmpl = "import {domains_route} as my_domains"


def get_domain(entity_id):
    return entity_id.split('.')[0]


def get_class_definition(entity_id, entity_data, register):
    if 'name' in entity_data and entity_data['name'] not in [None, '', 'None']:
        class_name = helpers.Pythonize.class_name(entity_data['name'])
    else:
        class_name = helpers.Pythonize.class_name(entity_id)

    domain_name = entity_id.split('.')[0]
    if domain_name in register['domains']:
        domain_class = helpers.Pythonize.class_name(domain_name)
        return f'\n\nclass {class_name}(my_domains.{domain_class}):'
    else:
        return f'\n\nclass {class_name}:'


def generate_entity_class(entity_id: str, entity_data: dict, register: dict):
    class_lines = [
        get_class_definition(entity_id, entity_data, register),
        f'    entity_id = "{entity_id}"'
    ]
    return '\n'.join(class_lines)


def generate_entity_module(register, domains_route):
    if 'entities' not in register:
        raise ValueError('No entities to generate')

    entity_classes = [entity_tmpl.format(domains_route=domains_route)] + [
        generate_entity_class(entity_id, entity_data, register)
        for entity_id, entity_data in register['entities'].items()
    ]
    return '\n'.join(entity_classes)


def write_entities_module(register, module_path, domains_route):
    with open(module_path, 'w') as f:
        f.write(generate_entity_module(register, domains_route))
    return module_path
