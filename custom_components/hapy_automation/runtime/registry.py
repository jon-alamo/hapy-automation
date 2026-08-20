"""Builds the in-memory "register" dict consumed by the generators —
ported from hapy/register.py, but sourced directly from a live Home
Assistant instance (entity_registry, device_registry, hass.states, the
service registry) instead of REST/WebSocket calls against a remote HA.

No persistent cache: this is called fresh on every reload (cheap — it's
all in-memory reads, no network), so it always reflects HA's current
state exactly and never accumulates entries for entities/devices that no
longer exist — replacing hapy/register.py's `.registry` JSON file, which
merged additively forever and never pruned (see plan doc, bug #5).
"""
import enum
import re

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.service import async_get_all_descriptions

from . import helpers
from .zigbee import build_device_signatures


def _json_safe(value):
    """Recursively convert a state-attribute value into something whose
    repr() is valid Python source. Real HA entity attributes routinely
    carry live Python objects, not just JSON-ish primitives — e.g. a
    light's `color_mode`/`supported_color_modes` are `ColorMode` enum
    members and `supported_features` is an `IntFlag` — and repr() of
    those (`<ColorMode.ONOFF: 'onoff'>`) is not valid Python, which broke
    entities.py generation with a SyntaxError the first time this ran
    against real live state (the old REST/WS-based generator never hit
    this because REST responses are already JSON, so attributes arriving
    that way are always plain str/int/float/bool/list/dict/None)."""
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_json_safe(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def entity_allowed(entity_id: str, pattern: str, always_included_domains) -> bool:
    """Entities in `always_included_domains` (light/switch/climate/...) are
    always kept. Everything else only if it matches `pattern` (the
    ENTITY_INCLUDE_PATTERN / `_hapy`-suffix convention) — or if `pattern`
    is empty, in which case nothing is filtered."""
    domain = (entity_id or '').split('.', 1)[0]
    if domain in always_included_domains:
        return True
    if not pattern:
        return True
    return bool(re.search(pattern, entity_id or ''))


async def async_build_register(
        hass: HomeAssistant, entity_include_pattern: str, always_included_domains
) -> dict:
    register = {
        'domains': {},
        'entities': {},
        'devices2entities': {},
        'devices': {},
        'device2classname': {},
        'device_signatures': {},
    }

    descriptions = await async_get_all_descriptions(hass)
    for domain, services in descriptions.items():
        register['domains'][domain] = {
            name: (service_data or {}) for name, service_data in services.items()
        }

    ent_reg = er.async_get(hass)
    dev_reg = dr.async_get(hass)

    for device in dev_reg.devices.values():
        name = device.name_by_user or device.name
        register['devices'][device.id] = {
            'id': device.id,
            'name': name,
            'model': device.model,
            'manufacturer': device.manufacturer,
            'area_id': device.area_id,
        }
        register['device2classname'][device.id] = helpers.get_device_class_name(name, device.id)

    for state in hass.states.async_all():
        entity_id = state.entity_id
        if not entity_allowed(entity_id, entity_include_pattern, always_included_domains):
            continue
        reg_entry = ent_reg.async_get(entity_id)
        attributes = _json_safe(dict(state.attributes))
        attributes['last_changed'] = state.last_changed.isoformat()
        attributes['last_updated'] = state.last_updated.isoformat()
        attributes['state_value'] = state.state
        device_id = reg_entry.device_id if reg_entry else None
        register['entities'][entity_id] = {
            'id': entity_id,
            'unique_id': reg_entry.unique_id if reg_entry else None,
            'name': (reg_entry.name if reg_entry and reg_entry.name else None)
                    or attributes.get('friendly_name', entity_id),
            'attributes': attributes,
            'device_id': device_id,
            'area_id': reg_entry.area_id if reg_entry else None,
        }
        if device_id:
            register['devices2entities'].setdefault(device_id, []).append(entity_id)

    register['device_signatures'] = build_device_signatures()
    return register
