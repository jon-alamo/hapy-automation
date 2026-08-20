"""Config flow: repo URL, branch, auth method, entity filter, poll
interval, dry-run toggle — the per-user settings that let anyone point
this integration at their own automations repo without touching the
integration's code (see plan doc: "cualquier persona puede instalarla y
usarla con su propio repo")."""
from __future__ import annotations

import os
import secrets
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import (
    AUTH_METHOD_NONE,
    AUTH_METHOD_PAT,
    AUTH_METHOD_SSH_KEY,
    CONF_AUTH_METHOD,
    CONF_BRANCH,
    CONF_DRY_RUN,
    CONF_ENABLE_WEBHOOK,
    CONF_ENTITY_INCLUDE_PATTERN,
    CONF_PAT,
    CONF_POLL_INTERVAL_MINUTES,
    CONF_REPO_URL,
    CONF_SSH_KEY_PATH,
    CONF_WEBHOOK_ID,
    DEFAULT_BRANCH,
    DEFAULT_DRY_RUN,
    DEFAULT_ENABLE_WEBHOOK,
    DEFAULT_ENTITY_INCLUDE_PATTERN,
    DEFAULT_POLL_INTERVAL_MINUTES,
    DOMAIN,
)

AUTH_METHODS = [AUTH_METHOD_SSH_KEY, AUTH_METHOD_PAT, AUTH_METHOD_NONE]


def _base_schema(defaults: dict) -> vol.Schema:
    return vol.Schema({
        vol.Required(CONF_REPO_URL, default=defaults.get(CONF_REPO_URL, '')): str,
        vol.Required(CONF_BRANCH, default=defaults.get(CONF_BRANCH, DEFAULT_BRANCH)): str,
        vol.Required(CONF_AUTH_METHOD, default=defaults.get(CONF_AUTH_METHOD, AUTH_METHOD_SSH_KEY)):
            vol.In(AUTH_METHODS),
        vol.Optional(CONF_SSH_KEY_PATH, default=defaults.get(CONF_SSH_KEY_PATH, '')): str,
        vol.Optional(CONF_PAT, default=defaults.get(CONF_PAT, '')): str,
        vol.Optional(
            CONF_ENTITY_INCLUDE_PATTERN,
            default=defaults.get(CONF_ENTITY_INCLUDE_PATTERN, DEFAULT_ENTITY_INCLUDE_PATTERN),
        ): str,
        vol.Optional(
            CONF_POLL_INTERVAL_MINUTES,
            default=defaults.get(CONF_POLL_INTERVAL_MINUTES, DEFAULT_POLL_INTERVAL_MINUTES),
        ): vol.All(vol.Coerce(int), vol.Range(min=1, max=120)),
        vol.Optional(CONF_DRY_RUN, default=defaults.get(CONF_DRY_RUN, DEFAULT_DRY_RUN)): bool,
        vol.Optional(
            CONF_ENABLE_WEBHOOK, default=defaults.get(CONF_ENABLE_WEBHOOK, DEFAULT_ENABLE_WEBHOOK)
        ): bool,
    })


def _validate(user_input: dict) -> dict:
    errors = {}
    if user_input[CONF_AUTH_METHOD] == AUTH_METHOD_SSH_KEY:
        key_path = user_input.get(CONF_SSH_KEY_PATH)
        if not key_path:
            errors[CONF_SSH_KEY_PATH] = 'ssh_key_path_required'
        elif not os.path.isfile(key_path):
            errors[CONF_SSH_KEY_PATH] = 'ssh_key_path_not_found'
    elif user_input[CONF_AUTH_METHOD] == AUTH_METHOD_PAT:
        if not user_input.get(CONF_PAT):
            errors[CONF_PAT] = 'pat_required'
    return errors


class HapyAutomationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        errors: dict[str, str] = {}
        if user_input is not None:
            errors = _validate(user_input)
            if not errors:
                data = dict(user_input)
                if data.get(CONF_ENABLE_WEBHOOK):
                    data[CONF_WEBHOOK_ID] = secrets.token_hex(16)
                return self.async_create_entry(
                    title=data[CONF_REPO_URL].rsplit('/', 1)[-1] or 'Hapy Automation',
                    data=data,
                )
        return self.async_show_form(
            step_id='user', data_schema=_base_schema(user_input or {}), errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return HapyAutomationOptionsFlow(config_entry)


class HapyAutomationOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict[str, Any] | None = None):
        errors: dict[str, str] = {}
        current = {**self.config_entry.data, **self.config_entry.options}
        if user_input is not None:
            errors = _validate(user_input)
            if not errors:
                data = dict(user_input)
                if data.get(CONF_ENABLE_WEBHOOK) and not current.get(CONF_WEBHOOK_ID):
                    data[CONF_WEBHOOK_ID] = secrets.token_hex(16)
                elif current.get(CONF_WEBHOOK_ID):
                    data[CONF_WEBHOOK_ID] = current[CONF_WEBHOOK_ID]
                self.hass.config_entries.async_update_entry(
                    self.config_entry, data={**self.config_entry.data, **data}
                )
                return self.async_create_entry(title='', data={})
        return self.async_show_form(
            step_id='init', data_schema=_base_schema(current), errors=errors,
        )
