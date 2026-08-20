"""Zigbee/zha-quirks device-trigger resolution — ported from
hapy/generators/devices.py and hapy/register.py's register_signatures().

The only behavioral change from the original: zigpy/zhaquirks/zha.quirks
are no longer separate pip dependencies of this package (which risked
version drift against whatever HA's own `zha` integration has loaded —
see manifest.json's `after_dependencies: ["zha"]`). Instead we import
whatever the running HA instance already has loaded for its `zha`
integration; if the user doesn't have ZHA set up at all, every function
here degrades gracefully (empty signatures, no device triggers) instead
of crashing generation for everyone else.
"""
import importlib
import inspect
import logging
import pkgutil

from . import helpers

logger = logging.getLogger(__name__)


def _import_zigbee_stack():
    """Returns (zhaquirks, zigpy_quirks, zha_quirks_v2) or (None, None, None)
    if ZHA isn't installed/loaded in this Home Assistant instance."""
    try:
        import zhaquirks
        import zigpy.quirks as zigpy_quirks
        import zha.quirks as zha_quirks_v2
    except ImportError:
        return None, None, None
    return zhaquirks, zigpy_quirks, zha_quirks_v2


class V2QuirkTriggers:
    """Adapter exposing a v2 QuirkBuilder quirk's device_automation_triggers
    as an attribute, matching how v1 quirk classes carry it, so
    get_action_references()/Device.handle_action_data() don't need to care
    which quirk generation produced it."""

    def __init__(self, triggers):
        self.device_automation_triggers = triggers


def get_device_quirk(manufacturer, model):
    """Resolve (manufacturer, model) to a zha-quirks class exposing
    device_automation_triggers, trying (in order) the legacy v1 registry,
    the v2 registry, and the newer QuirkBuilder-based registry. Returns
    (quirk, quirk_attribute_name) or (None, None) if nothing matches or
    ZHA isn't loaded."""
    zhaquirks, zigpy_quirks, zha_quirks_v2 = _import_zigbee_stack()
    if zhaquirks is None:
        return None, None

    zhaquirks.setup(zhaquirks.__path__[0])
    registry_v1 = zigpy_quirks.DEVICE_REGISTRY.registry_v1
    # registry_v2 was removed from newer zigpy releases; degrade gracefully
    # instead of crashing at import time if it's gone.
    registry_v2 = getattr(zigpy_quirks.DEVICE_REGISTRY, 'registry_v2', {})

    # Try the exact manufacturer, then a manufacturer-agnostic quirk for
    # this *exact* model — some quirks (e.g. generic Tuya scene switches
    # like TS0043) are registered under manufacturer=None to match any
    # vendor's re-branding of the same hardware. Deliberately NOT also
    # wildcarding the model: a manufacturer-only match (any model from
    # this vendor) is how zigpy's own device-matching chain behaves, but
    # for known, specific (manufacturer, model) pairs it's more likely to
    # silently attach an unrelated quirk than to find a real match.
    for candidate_manufacturer in (manufacturer, None):
        bucket = registry_v1.get(candidate_manufacturer)
        if bucket and model in bucket:
            quirk = list(bucket[model])[0]
            return quirk, 'device_automation_triggers'

    if (manufacturer, model) in registry_v2:
        quirk = list(registry_v2[(manufacturer, model)])[0]
        return quirk, 'device_automation_triggers_metadata'

    # QuirkBuilder-based (v2) quirks register into a separate registry keyed
    # by ModelInfo(manufacturer, model), each entry's triggers living under
    # zha_device_factory.quirk_definition. This is a private attribute
    # (_registry) because zha.quirks doesn't expose a public static lookup —
    # only device-instance matching (match_entry) — so this may need
    # revisiting on future zha-quirks upgrades.
    key = zha_quirks_v2.ModelInfo(manufacturer, model)
    for entry in getattr(zha_quirks_v2.DEVICE_REGISTRY, '_registry', {}).get(key, []):
        triggers = entry.zha_device_factory.quirk_definition.device_automation_triggers
        if triggers:
            return V2QuirkTriggers(triggers), 'device_automation_triggers'

    return None, None


def get_action_references(quirk, quirk_attribute):
    """Yield (action_name,) boolean-attribute names for a resolved quirk's
    device_automation_triggers, e.g. 'remote_button_short_press_turn_on'."""
    if quirk is not None and quirk_attribute and hasattr(quirk, quirk_attribute):
        for action_names in getattr(quirk, quirk_attribute):
            yield helpers.get_action_name(*action_names)


def build_device_signatures() -> dict:
    """Walk zha-quirks to build a "<manufacturer> <model>" -> quirk class
    lookup. Some upstream quirk/builder modules ship with broken relative
    imports (a known zha-quirks packaging issue); skip those instead of
    letting one bad module abort generation for everyone. Returns {} if
    ZHA isn't installed/loaded."""
    zhaquirks, _, _ = _import_zigbee_stack()
    if zhaquirks is None:
        return {}

    signatures = {}
    for _, package_name, ispkg in pkgutil.walk_packages(
            path=zhaquirks.__path__, onerror=lambda x: None
    ):
        if not ispkg:
            continue
        package_route = f"zhaquirks.{package_name}"
        try:
            package = importlib.import_module(package_route)
        except Exception as e:
            logger.debug('skipping unimportable package %s: %s', package_route, e)
            continue
        for _, module_name, is_pkg in pkgutil.walk_packages(package.__path__):
            if is_pkg:
                continue
            module_route = f"{package_route}.{module_name}"
            try:
                module = importlib.import_module(module_route)
            except Exception as e:
                logger.debug('skipping unimportable module %s: %s', module_route, e)
                continue
            for _, obj in inspect.getmembers(module, inspect.isclass):
                signature = getattr(obj, 'signature', None)
                if not signature:
                    continue
                device_key = zhaquirks.const.MODELS_INFO
                if device_key not in signature:
                    continue
                for device_brand_names in signature[device_key]:
                    if not device_brand_names:
                        continue
                    device_title = helpers.get_device_title(*device_brand_names)
                    signatures[device_title] = [module_route, obj.__name__]
    return signatures
