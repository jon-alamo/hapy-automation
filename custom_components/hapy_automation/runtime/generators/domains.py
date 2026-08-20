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


def get_field_docstring(field_name, field_data):
    return '\n'.join([
        f':{field_name}: {field_data.get("description", "")}',
        f'    {field_data.get("selector", "")}',
        f'    Example: {field_data.get("example", "")}',
    ])


def generate_docstring(service_data: dict, indent_level: int = 2) -> str:
    # Built as a single repr()-escaped string literal, not a hand-rolled
    # `""" ... """` block — real HA service/field descriptions are
    # arbitrary text from every installed integration, and embedding it
    # raw is an injection risk in miniature: any description that itself
    # contains `"""` (or, previously, a service *name* that was a
    # reserved keyword — see generate_domain_mixin) breaks the syntax of
    # the whole generated module, not just the one entry. repr() escapes
    # whatever's in there and stays valid Python regardless of content —
    # still a docstring either way, since a bare string literal as a
    # function's first statement is one no matter the quoting style.
    indent = indent_level * INDENT
    lines = [service_data.get('description', '')]
    for field_name, field_data in (service_data.get('fields') or {}).items():
        lines.append(get_field_docstring(field_name, field_data or {}))
    text = '\n'.join(lines)
    return f'{" " * indent}{text!r}'


def generate_service_method(method_name, service_data, indent_level=1):
    def_indent = indent_level * INDENT
    fields = generate_fields(service_data.get('fields'))
    docstring = generate_docstring(service_data, indent_level=indent_level + 1)
    method_lines = [
        f'\n{" " * def_indent}def {method_name}({fields}):',
        docstring
    ]
    return '\n'.join(method_lines)


def generate_domain_mixin(domain_name, domain_data):
    # Real HA service names are already valid Python identifiers almost
    # always — except when a service is literally named after a reserved
    # keyword (found for real: the `blueprint` domain has a service
    # called `import`). `def import(self, ...):` is a SyntaxError, and it
    # broke generation of the *entire* domains.py module for any instance
    # with that integration loaded, not just that one service. Pythonize
    # the method name (its reserved-keyword handling appends a trailing
    # underscore) and, whenever that differs from the real service name,
    # record the mapping so models.service_call can still target the
    # real name when actually calling the service — a Python-safe method
    # name isn't the same thing as a valid Home Assistant service name.
    class_name = helpers.Pythonize.class_name(domain_name)
    service_methods = []
    overrides = {}
    for service_name, service_data in domain_data.items():
        method_name = helpers.Pythonize.method_name(service_name)
        if method_name != service_name:
            overrides[method_name] = service_name
        service_methods.append(generate_service_method(method_name, service_data or {}))
    mixin_lines = [f'\n\nclass {class_name}(models.Domain):']
    if overrides:
        mixin_lines.append(f'    _hapy_service_names = {overrides!r}\n')
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
