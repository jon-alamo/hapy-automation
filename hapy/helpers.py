import re
import pytz
import sys
import logging
from hapy.config import settings
from datetime import datetime, timezone
import dateutil.parser as dt_parser


tzname = settings.timezone
tz = pytz.timezone(tzname)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger


def get_now():
    return datetime.now(tz)


def parse_date(last_changed):
    if type(last_changed) is str:
        return datetime.fromisoformat(last_changed).astimezone(tz)
    elif type(last_changed) is datetime:
        return last_changed
    else:
        return datetime.now(tz)


def parse_string_value(string: str | None):
    try:
        return float(string) if '.' in string else int(string)
    except (ValueError, TypeError):
        return string


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
        s = re.sub('[^0-9a-zA-Z_]', 'x', s)
        s = re.sub('^[^a-zA-Z_]+', 'x', s)
        if s in reserved_names:
            s += '_'
        return s

    @staticmethod
    def method_name(s):
        s = s.replace('_', '-').replace('.', '-').replace(' ', '-')
        s = '_'.join([c.lower() for c in s.split('-')])
        s = re.sub('[^0-9a-zA-Z_]', 'x', s)
        s = re.sub('^[^a-zA-Z_]+', 'x', s)
        if s in reserved_names:
            s += '_'
        return s

    @classmethod
    def parameter_name(cls, s):
        return cls.method_name(s)


def get_device_class_name(device_name: [str | None], device_id: str) -> str:
    if device_name:
        return Pythonize.class_name(device_name) + '_' + device_id[-2:]
    return Pythonize.class_name(device_id)


def get_action_name(action_type: str, action_name: str) -> str:
    return f'{action_type}_{action_name}'
