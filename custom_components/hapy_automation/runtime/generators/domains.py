"""Generates the `domains.py` module imported by user automation code
(`import domains`) and by generated entities.py's `services` attribute —
ported from hapy/generators/domains.py, including the defensive `.get()`
usage on service field data (not every HA service ships a `description`
or `fields` — see plan doc, bug #4).
"""
from .. import helpers

types = {
    'number': float,
    'boolean': bool,
}

INDENT = 4

domain_tmpl = "from custom_components.hapy_automation.runtime import models"


def generate_field(field_name, field_data, required=False):
    example = field_data.get('example')
    selector = field_data.get('selector') or {}
    if example:
        field_type = type(example)
    elif selector:
        selector_key = list(selector.keys())[0]
        field_type = types.get(selector_key, str)
    else:
        field_type = str
    default = '' if required else ' = None'
    field_name = helpers.Pythonize.parameter_name(field_name)
    return f'{field_name}: {field_type.__name__}' + default


def generate_fields(fields_data, is_method=True):
    fields = ['self'] if is_method else []
    for field_name, field_data in (fields_data or {}).items():
        fields.append(generate_field(field_name, field_data or {}))
    return ', '.join(fields)


def get_field_docstring(field_name, field_data, indent_level=2):
    indent = indent_level * INDENT
    field_docstring_lines = [
        f'\n{" " * indent}:{field_name}: {field_data.get("description", "")}',
        f'{" " * (indent + INDENT)}{field_data.get("selector", "")}',
        f'{" " * (indent + INDENT)}Example: {field_data.get("example", "")}'
    ]
    return '\n'.join(field_docstring_lines)


def generate_docstring(service_data: dict, indent_level: int = 2) -> str:
    indent = indent_level * INDENT
    fields_docstrings = [
        get_field_docstring(field_name, field_data or {}, indent_level=indent_level)
        for field_name, field_data in (service_data.get('fields') or {}).items()
    ]
    docstring_lines = [
        f'{" " * indent}""" {service_data.get("description", "")}',
    ] + fields_docstrings + [f'{" " * indent}"""']
    return '\n'.join(docstring_lines)


def generate_service_method(service_name, service_data, indent_level=1):
    def_indent = indent_level * INDENT
    fields = generate_fields(service_data.get('fields'))
    docstring = generate_docstring(service_data, indent_level=indent_level + 1)
    method_lines = [
        f'\n{" " * def_indent}def {service_name}({fields}):',
        docstring
    ]
    return '\n'.join(method_lines)


def generate_domain_mixin(domain_name, domain_data):
    class_name = helpers.Pythonize.class_name(domain_name)
    service_methods = [
        generate_service_method(service_name, service_data or {})
        for service_name, service_data in domain_data.items()
    ]
    mixin_lines = [f'\n\nclass {class_name}(models.Domain):']
    return '\n'.join(mixin_lines + service_methods)


def generate_domain_module(register):
    if 'domains' not in register:
        raise ValueError('No domains to generate')
    domain_mixins = [domain_tmpl] + [
        generate_domain_mixin(domain_name, domain_data)
        for domain_name, domain_data in register['domains'].items()
    ]
    return '\n'.join(domain_mixins)


def write_domain_module(register, module_path):
    with open(module_path, 'w', encoding="utf-8") as f:
        f.write(generate_domain_module(register))
    return module_path
