import re


INDENT = 4

reserved_names = [
    'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'True', 'try', 'while', 'with', 'yield'
]


def get_device_title(manufacturer: [str | None], model: str) -> str:
    if not manufacturer:
        return model
    if not model:
        return manufacturer
    return f'{manufacturer} {model}'


class Pythonize:
    @staticmethod
    def class_name(s):
        s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
        s = ''.join([c.capitalize() for c in s.split('-')])
        s = re.sub('[^0-9a-zA-Z_]', '', s)
        return re.sub('^[^a-zA-Z_]+', '', s)

    @staticmethod
    def method_name(s):
        s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
        s = '_'.join([c.lower() for c in s.split('-')])
        s = re.sub('[^0-9a-zA-Z_]', '', s)
        return re.sub('^[^a-zA-Z_]+', '', s)

    @staticmethod
    def parameter_name(s):
        if s in reserved_names:
            s = f'_{s}'
        s = re.sub('[^0-9a-zA-Z_]', '', s)
        return re.sub('^[^a-zA-Z_]+', '', s)


def get_device_class_name(device_name: [str | None], device_id: str) -> str:
    if device_name:
        return Pythonize.class_name(device_name + device_id[-2:])
    return Pythonize.class_name(device_id)
