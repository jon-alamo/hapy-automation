"""Pure-Python helpers ported from hapy/helpers.py.

No transport dependency here, so these port verbatim except for timezone
handling: instead of reading TIMEZONE from a .env file, the active Home
Assistant instance's configured timezone is injected once at integration
setup via `set_timezone()`, and defaults to UTC before that happens (e.g.
in unit tests that exercise this module directly).
"""
import re
from datetime import datetime
from zoneinfo import ZoneInfo

# hapy/helpers.py imported dateutil.parser as dt_parser at module level,
# so any automation code doing `hapy.helpers.dt_parser.parse(...)` (e.g.
# home-automations/automations/climate.py's is_on_time()) relied on it
# being re-exported transitively from the old library — not something
# used internally by this module, just carried through. Found for real:
# missing this made is_on_time() raise AttributeError, which — inside an
# `or` chain in action() — silently aborted the whole action() before the
# exception-safety fix in runtime/automations.py made it visible at all.
import dateutil.parser as dt_parser  # noqa: F401 — re-exported for automation code, not used here

_tz = ZoneInfo("UTC")


def set_timezone(tz_name: str) -> None:
    global _tz
    _tz = ZoneInfo(tz_name)


def get_now() -> datetime:
    return datetime.now(_tz)


def parse_date(value):
    if isinstance(value, str):
        return datetime.fromisoformat(value).astimezone(_tz)
    elif isinstance(value, datetime):
        return value
    else:
        return datetime.now(_tz)


def parse_string_value(value):
    try:
        return float(value) if '.' in value else int(value)
    except (ValueError, TypeError):
        return value


INDENT = 4

reserved_names = [
    'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'True', 'try', 'while', 'with', 'yield'
]


def get_device_title(manufacturer, model: str) -> str:
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


def get_device_class_name(device_name, device_id: str) -> str:
    if device_name:
        return Pythonize.class_name(device_name) + '_' + device_id[-2:]
    return Pythonize.class_name(device_id)


def get_action_name(action_type: str, action_name: str) -> str:
    return f'{action_type}_{action_name}'
