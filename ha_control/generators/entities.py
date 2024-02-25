import ha_control.helpers as helpers


entity_tmpl = '\n'.join([
    "import ha_control.models as models",
    "from . import {domains_route} as my_domains",
    "import dataclasses",
    "import typing",
    "\nmy_ha_instance = models.HAInstance(secret_file='{secret_file}')\n"
])

entity_ref_tmpl = """
class {class_name}(models.Entity):

    @dataclasses.dataclass
    class _StateClass(models.State):
        "State class for entity {entity_id}"
{dataclass_fields}

    state = _StateClass(**{attributes})
    services = {domain_ref}(
        instance=my_ha_instance,
        entity_id="{entity_id}",
        state=state
    )
    unique_id = "{unique_id}"
    name = "{name}"
    device_id = "{entity_id}"
"""

INDENT = 4


def get_domain(entity_id):
    return entity_id.split('.')[0]


def get_dataclass_field(key, value, indent_level=2):
    indent = indent_level * INDENT
    if value is None:
        field_type = 'typing.Any'
    else:
        field_type = type(value).__name__
    return f'{" " * indent}{key}: {field_type}'


def get_dataclass_fields(attributes: dict):
    fields = []
    for k, v in attributes.items():
        fields.append(get_dataclass_field(k, v))
    return '\n'.join(fields)


def get_instantiate_definition(entity_id, entity_data, register):
    class_name = helpers.Pythonize.class_name(entity_id)
    unique_id = entity_data.get('unique_id', None)
    name = entity_data.get('name', entity_id)
    attributes = entity_data.get('attributes') or {}
    domain_name = entity_id.split('.')[0]
    dataclass_fields = get_dataclass_fields(attributes)
    if domain_name in register['domains']:
        domain_class = helpers.Pythonize.class_name(domain_name)
        domain_ref = f'my_domains.{domain_class}'
    else:
        domain_ref = f'models.Domain'
    return entity_ref_tmpl.format(
        class_name=class_name,
        entity_id=entity_id,
        unique_id=unique_id,
        name=name,
        attributes=attributes,
        domain_ref=domain_ref,
        dataclass_fields=dataclass_fields
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
