"""Generates the `entities.py` module imported by user automation code
(`import entities`) — ported from hapy/generators/entities.py. Source data
is the in-memory `register` dict built by runtime/registry.py (see
async_build_register), not a REST/WS payload.
"""
from .. import helpers

RUNTIME_MODELS_IMPORT = "from custom_components.hapy_automation.runtime import models"

entity_tmpl = """
{runtime_import}
import {domains_route} as my_domains
import typing
from datetime import datetime

my_ha_instance = models.HassBridge(models.get_hass())
"""


entity_ref_tmpl = """
class {class_name}(models.Entity):

    class _StateClass(models.State):
        \"\"\"State class for entity {entity_id}\"\"\"
{dataclass_fields}
        old: models.State = models.State()
        last_changed: datetime = None
        last_updated: datetime = None
        state_value: typing.Any = None

    entity_id = "{entity_id}"
    unique_id = "{unique_id}"
    name = "{name}"
    device_id = "{device_id}"
    state = _StateClass(actual_entity_id=entity_id, ha_instance=my_ha_instance, **{attributes})
    services = {domain_ref}(
        instance=my_ha_instance,
        entity_id="{entity_id}",
        state=state
    )

"""


INDENT = 4


def get_dataclass_field(key, value, indent_level=2):
    indent = indent_level * INDENT
    field_type = 'typing.Any' if value is None else type(value).__name__
    parameter = helpers.Pythonize.parameter_name(key)
    return f'{" " * indent}{parameter}: {field_type}'


def get_dataclass_fields(attributes: dict):
    return '\n'.join(get_dataclass_field(k, v) for k, v in attributes.items())


def get_state_attributes(attributes: dict):
    return {helpers.Pythonize.parameter_name(k): v for k, v in attributes.items()}


def get_instantiate_definition(entity_id, entity_data, register):
    class_name = helpers.Pythonize.class_name(entity_id)
    unique_id = entity_data.get('unique_id', None)
    name = entity_data.get('name', entity_id)
    attributes = entity_data.get('attributes') or {}
    domain_name = entity_id.split('.')[0]
    state_attributes = get_state_attributes(attributes)
    dataclass_fields = get_dataclass_fields(attributes)
    if domain_name in register['domains']:
        domain_class = helpers.Pythonize.class_name(domain_name)
        domain_ref = f'my_domains.{domain_class}'
    else:
        domain_ref = 'models.Domain'
    return entity_ref_tmpl.format(
        class_name=class_name,
        entity_id=entity_id,
        unique_id=unique_id,
        name=name,
        attributes=state_attributes,
        domain_ref=domain_ref,
        dataclass_fields=dataclass_fields,
        device_id=entity_data.get('device_id', None)
    )


def generate_entity_module(register, domains_route='domains'):
    if 'entities' not in register:
        raise ValueError('No entities to generate')
    header = entity_tmpl.format(runtime_import=RUNTIME_MODELS_IMPORT, domains_route=domains_route)
    entity_instances = [header] + [
        get_instantiate_definition(entity_id, entity_data, register)
        for entity_id, entity_data in register['entities'].items()
    ]
    return '\n'.join(entity_instances)


def write_entities_module(register, module_path, domains_route='domains'):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_entity_module(register, domains_route))
    return module_path
