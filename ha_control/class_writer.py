import re


def pythonize(s):
    s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
    s = ''.join([c.capitalize() for c in s.split('-')])
    s = re.sub('[^0-9a-zA-Z_]', '', s)
    return re.sub('^[^a-zA-Z_]+', '', s)


def parse_value(value):
    if type(value) is str:
        return f'"{value}"'
    return value


def generate_class_definition(class_name, attributes, template):
    class_definition = template.format(class_name=class_name)
    class_definition += '\n'.join(
        f'    {key} = {parse_value(value)}' for key, value in attributes.items()
    )
    return class_definition
