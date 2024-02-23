import ha_control.helpers as helpers
import ha_control.models as models


entity_tmpl = '\n'.join([
    "import ha_control.models as models",
    "from . import {domains_route} as my_domains",
    "my_ha_instance = models.HAInstance(secret_file='{secret_file}')\n"
])

entity_ref_tmpl = """
{instance_name} = models.Entity(
    instance=my_ha_instance,
    entity_id="{entity_id}", 
    unique_id="{unique_id}", 
    name="{name}", 
    device_id="{entity_id}", 
    attributes={attributes}, 
    domain_class={domain_ref}
)
"""


def get_domain(entity_id):
    return entity_id.split('.')[0]


def get_instantiate_definition(entity_id, entity_data, register):
    instance_name = helpers.Pythonize.method_name(entity_id.split('.')[1])
    unique_id = entity_data.get('unique_id', None)
    name = entity_data.get('name', entity_id)
    attributes = entity_data.get('attributes', {})
    domain_name = entity_id.split('.')[0]
    if domain_name in register['domains']:
        domain_class = helpers.Pythonize.class_name(domain_name)
        domain_ref = f'my_domains.{domain_class}'
    else:
        domain_ref = None
    return entity_ref_tmpl.format(
        instance_name=instance_name,
        entity_id=entity_id,
        unique_id=unique_id,
        name=name,
        attributes=attributes,
        domain_ref=domain_ref
    )


def generate_entity_module(register, domains_route, secret_file):
    if 'entities' not in register:
        raise ValueError('No entities to generate')
    entity_header = entity_tmpl.format(
        domains_route=domains_route,
        secret_file=secret_file
    )
    entity_instances = [entity_header] + [
        get_instantiate_definition(entity_id, entity_data, register)
        for entity_id, entity_data in register['entities'].items()
    ]
    return '\n'.join(entity_instances)


def write_entities_module(register, module_path, domains_route, secret_file):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_entity_module(register, domains_route, secret_file))
    return module_path
