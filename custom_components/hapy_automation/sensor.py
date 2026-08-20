"""Diagnostic sensors — this is the "verify real content, not just logs"
requirement made concrete: the user can see exactly which commit is
running, whether the last reload succeeded, and (in dry-run) which
automation would have fired, without reading a log file."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, SIGNAL_RELOAD_COMPLETE
from .coordinator import HapyCoordinator


async def async_setup_entry(
        hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator: HapyCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        CurrentCommitSensor(coordinator, entry),
        LastReloadStatusSensor(coordinator, entry),
        LastWouldHaveFiredSensor(coordinator, entry),
    ])


class _BaseHapySensor(SensorEntity):
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_should_poll = False

    def __init__(self, coordinator: HapyCoordinator, entry: ConfigEntry):
        self.coordinator = coordinator
        self._entry = entry

    async def async_added_to_hass(self) -> None:
        self.async_on_remove(
            async_dispatcher_connect(self.hass, SIGNAL_RELOAD_COMPLETE, self._handle_update)
        )

    def _handle_update(self) -> None:
        self.async_write_ha_state()

    @property
    def device_info(self):
        return {
            'identifiers': {(DOMAIN, self._entry.entry_id)},
            'name': self._entry.title,
            'manufacturer': 'hapy-automation',
        }


class CurrentCommitSensor(_BaseHapySensor):
    _attr_name = 'Hapy Automation Current Commit'
    _attr_icon = 'mdi:source-commit'

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{entry.entry_id}_current_commit'

    @property
    def native_value(self):
        sha = self.coordinator.current_sha
        return sha[:8] if sha else None

    @property
    def extra_state_attributes(self):
        return {'full_sha': self.coordinator.current_sha}


class LastReloadStatusSensor(_BaseHapySensor):
    _attr_name = 'Hapy Automation Last Reload Status'
    _attr_icon = 'mdi:reload'

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{entry.entry_id}_last_reload_status'

    @property
    def native_value(self):
        return self.coordinator.last_reload_status

    @property
    def extra_state_attributes(self):
        return {
            'last_error': self.coordinator.last_reload_error,
            'last_reload_at': self.coordinator.last_reload_at.isoformat()
            if self.coordinator.last_reload_at else None,
        }


class LastWouldHaveFiredSensor(_BaseHapySensor):
    _attr_name = 'Hapy Automation Last Would-Have-Fired'
    _attr_icon = 'mdi:flash-outline'

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{entry.entry_id}_last_would_have_fired'

    @property
    def native_value(self):
        if not self.coordinator.last_would_have_fired:
            return None
        name, _ts = self.coordinator.last_would_have_fired
        return name

    @property
    def extra_state_attributes(self):
        if not self.coordinator.last_would_have_fired:
            return {}
        _name, ts = self.coordinator.last_would_have_fired
        return {'at': ts.isoformat()}
