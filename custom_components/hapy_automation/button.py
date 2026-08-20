"""Manual "reload now" button — lets the user force a reload and watch
the diagnostic sensors update, instead of waiting for the poll interval
or trusting a webhook fired, when they want to confirm right now that a
push landed."""
from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import HapyCoordinator


async def async_setup_entry(
        hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator: HapyCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([ReloadButton(coordinator, entry)])


class ReloadButton(ButtonEntity):
    _attr_name = 'Hapy Automation Reload Now'
    _attr_icon = 'mdi:source-pull'
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator: HapyCoordinator, entry: ConfigEntry):
        self.coordinator = coordinator
        self._entry = entry
        self._attr_unique_id = f'{entry.entry_id}_reload_button'

    @property
    def device_info(self):
        return {
            'identifiers': {(DOMAIN, self._entry.entry_id)},
            'name': self._entry.title,
            'manufacturer': 'hapy-automation',
        }

    async def async_press(self) -> None:
        await self.coordinator.async_reload(force=True)
