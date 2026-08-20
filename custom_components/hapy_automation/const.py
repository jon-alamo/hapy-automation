"""Constants for the Hapy Automation integration."""

DOMAIN = "hapy_automation"

CONF_REPO_URL = "repo_url"
CONF_BRANCH = "branch"
CONF_AUTH_METHOD = "auth_method"
CONF_SSH_KEY_PATH = "ssh_key_path"
CONF_PAT = "personal_access_token"
CONF_ENTITY_INCLUDE_PATTERN = "entity_include_pattern"
CONF_POLL_INTERVAL_MINUTES = "poll_interval_minutes"
CONF_DRY_RUN = "dry_run"
CONF_ENABLE_WEBHOOK = "enable_webhook"
CONF_WEBHOOK_ID = "webhook_id"

AUTH_METHOD_SSH_KEY = "ssh_key"
AUTH_METHOD_PAT = "personal_access_token"
AUTH_METHOD_NONE = "none"

DEFAULT_BRANCH = "main"
DEFAULT_POLL_INTERVAL_MINUTES = 1
DEFAULT_ENTITY_INCLUDE_PATTERN = r"_hapy$"
DEFAULT_DRY_RUN = True
DEFAULT_ENABLE_WEBHOOK = False

# Domains whose entities are always considered "actionable" and are never
# filtered out by CONF_ENTITY_INCLUDE_PATTERN, matching the pre-existing
# home-automations convention (light/switch/climate/etc. kept in full,
# sensor/binary_sensor/device_tracker curated via the `_hapy` suffix).
ALWAYS_INCLUDED_DOMAINS = frozenset(
    {
        "light",
        "switch",
        "climate",
        "cover",
        "fan",
        "lock",
        "media_player",
        "vacuum",
        "water_heater",
        "input_boolean",
        "input_number",
        "input_select",
        "input_text",
        "scene",
        "script",
    }
)

STATE_EVENT_TYPE = "state_changed"
ZHA_EVENT_TYPE = "zha_event"

REPO_SUBDIR = "repo"
GENERATED_SUBDIR = "generated"

STATUS_OK = "ok"
STATUS_ERROR = "error"
STATUS_UNKNOWN = "unknown"

SERVICE_RELOAD = "reload"
SERVICE_EXPORT_STUBS = "export_stubs"

SIGNAL_RELOAD_COMPLETE = f"{DOMAIN}_reload_complete"
