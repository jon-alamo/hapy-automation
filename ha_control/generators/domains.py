import ha_control.helpers as helpers

types = {
    'number': float,
    'boolean': bool
}


INDENT = 4


domain_tmpl = "from ha_control.services import service_call"


def generate_field(field_name, selector, example=None, required=False):
    if example:
        field_type = type(example)
    else:
        selector_key = list(selector.keys())[0]
        field_type = types.get(selector_key, str)
    default = '' if required else ' = None'
    return f'{field_name}: {field_type.__name__}' + default


def generate_fields(fields_data, is_method=True):
    fields = ['cls'] if is_method else []
    for field_name, field_data in fields_data.items():
        field = generate_field(field_name, field_data)
        fields.append(field)
    return ', '.join(fields)


def get_field_docstring(field_name, field_data, indent_level=2):
    indent = indent_level * INDENT
    field_docstring_lines = [
        f'\n{" " * indent}:{field_name}: {field_data.get("description", "")}',
        f'{" " * (indent + INDENT)}{field_data.get("selector", "")}',
        f'{" " * (indent + INDENT)}Example: {field_data.get("example", "")}'
    ]
    return '\n'.join(field_docstring_lines)


def generate_docstring(service_data: dict, indent_level: int=2) -> str:
    indent = indent_level * INDENT
    fields_docstrings = [
        get_field_docstring(field_name, field_data, indent_level=indent_level)
        for field_name, field_data in service_data['fields'].items()
    ]
    docstring_lines = [
        f'{" " * indent}""" {service_data["description"]}',
    ] + fields_docstrings + [f'{" " * indent}"""']
    return '\n'.join(docstring_lines)


def generate_service_method(domain_name, service_name, service_data, indent_level=1):
    def_indent = indent_level * INDENT
    fields = generate_fields(service_data['fields'])
    docstring = generate_docstring(service_data, indent_level=indent_level + 1)
    method_lines = [
        f'\n{" " * def_indent}@classmethod',
        f'{" " * def_indent}@service_call("{domain_name}")',
        f'{" " * def_indent}def {service_name}({fields}):',
        docstring
    ]
    return '\n'.join(method_lines)


def generate_domain_mixin(domain_name, domain_data):
    class_name = helpers.Pythonize.class_name(domain_name)
    service_methods = [
        generate_service_method(domain_name, service_name, service_data)
        for service_name, service_data in domain_data.items()
    ]
    mixing_lines = [
        f'\n\nclass {class_name}:'
    ]
    return '\n'.join(mixing_lines + service_methods)


def generate_domain_module(register):
    if 'domains' not in register:
        raise ValueError('No domains to generate')
    domain_mixins = [domain_tmpl] + [
        generate_domain_mixin(domain_name, domain_data)
        for domain_name, domain_data in register['domains'].items()
    ]
    return '\n'.join(domain_mixins)


def write_domain_module(register, module_path):
    domain_module = generate_domain_module(register)
    with open(module_path, 'w') as f:
        f.write(domain_module)
