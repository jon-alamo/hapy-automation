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
#
# NOTE: this list is a reconstruction, not the original production
# ENTITY_INCLUDE_PATTERN value (never found in either repo's .env — it
# was set directly on the deploy host). The original filter was a single
# regex applied uniformly to every entity_id, with no domain concept at
# all; "actionable domains kept in full" was achieved by that regex
# itself also matching those domains' entity_ids, not by separate logic.
# Splitting it into pattern + hardcoded domain allowlist here means this
# list can miss a domain the real pattern happened to cover — found for
# real against production data (missing input_datetime broke automations
# referencing entities.InputDatetimeOfficeAcOnTime). Treat additions to
# this list as expected/normal as more gaps surface, not as bugs in the
# splitting approach itself.
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
        "humidifier",
        "alarm_control_panel",
        "siren",
        "valve",
        "select",
        "input_boolean",
        "input_number",
        "input_select",
        "input_text",
        "input_datetime",
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
