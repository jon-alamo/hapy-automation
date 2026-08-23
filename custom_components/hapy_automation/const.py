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
AUTH_METHOD_SSH_KEY_GENERATE = "ssh_key_generate"
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
        # Low-cardinality singleton-ish domains (typically one `sun.sun`,
        # a handful of zones/persons per household) that automations
        # reference directly for presence/daylight state — found for real
        # on the Pi: entities.SunSun/ZoneHome missing broke
        # automations/general.py and climate.py. Unlike sensor/
        # binary_sensor/device_tracker (which can number in the hundreds
        # and is exactly what the `_hapy` curation exists for), there's no
        # entity-flood risk from including these wholesale.
        "sun",
        "zone",
        "person",
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

# -- Conversational agent (Telegram + OpenAI-compatible LLM) ---------------

CONF_ENABLE_AGENT = "enable_agent"
CONF_TELEGRAM_BOT_TOKEN = "telegram_bot_token"
CONF_TELEGRAM_ALLOWED_CHAT_IDS = "telegram_allowed_chat_ids"
CONF_LLM_API_BASE_URL = "llm_api_base_url"
CONF_LLM_API_KEY = "llm_api_key"
CONF_LLM_MODEL = "llm_model"
CONF_SYSTEM_PROMPT = "system_prompt"
CONF_STT_MODEL = "stt_model"
CONF_TTS_MODEL = "tts_model"
CONF_TTS_VOICE = "tts_voice"
CONF_LANGUAGE = "language"

DEFAULT_ENABLE_AGENT = False
DEFAULT_LLM_API_BASE_URL = "https://api.openai.com/v1"
DEFAULT_LLM_MODEL = "gpt-4o-mini"
DEFAULT_LANGUAGE = "es"

# ISO-639-1 -> human name, for the language directive appended to the
# system prompt. Falls back to the raw code for anything not listed here
# (still a valid Whisper `language` hint either way).
LANGUAGE_NAMES = {
    "es": "español",
    "en": "English",
    "ca": "català",
    "fr": "français",
    "de": "Deutsch",
    "it": "italiano",
    "pt": "português",
}
DEFAULT_STT_MODEL = "whisper-1"
DEFAULT_TTS_MODEL = "tts-1"
DEFAULT_TTS_VOICE = "alloy"

DEFAULT_SYSTEM_PROMPT = (
    "Eres el agente de automatizaciones de esta casa, integrado en Home "
    "Assistant a través de hapy_automation. Puedes consultar el estado "
    "real de cualquier entidad, llamar a servicios, y leer/escribir "
    "ficheros del repositorio de automatizaciones (Python, API "
    "hapy.Automation).\n\n"
    "Reglas:\n"
    "- Antes de escribir o modificar código de automatizaciones, llama a "
    "get_automation_api_reference y sigue esa guía — no confíes solo en "
    "lo que recuerdes de la API.\n"
    "- Antes de actuar o afirmar el estado de algo, consúltalo de verdad "
    "con las herramientas — no asumas ni inventes valores.\n"
    "- Nunca escribas entities.X / devices.X con un nombre que no hayas "
    "comprobado de verdad con list_states/get_state o leyendo automations/ "
    "existentes. Un nombre que 'suena razonable' pero no has verificado "
    "es una automatización que no hará nada — no hay forma de adivinarlo "
    "bien a la primera.\n"
    "- Al escribir o modificar una automatización, usa "
    "git_commit_and_push, que además dispara una recarga real; revisa "
    "SIEMPRE el resultado que te devuelve — tanto reload_ok/reload_error "
    "como el campo bindings.unbound_or_failed. reload_ok=true NO significa "
    "que la automatización haga algo: una entidad/dispositivo mal "
    "referenciado dentro de init_condition() no rompe la recarga, solo "
    "deja la automatización sin ningún binding, en silencio. Si tu "
    "automatización aparece en unbound_or_failed, no está terminada — "
    "corrige y reintenta tú mismo en la misma conversación antes de "
    "decir que ya está.\n"
    "- Sé ESCUETO: respuestas cortas y directas (1-2 frases si es "
    "posible), sin relatar los pasos intermedios ni las herramientas que "
    "has usado — solo el resultado. Nada de rodeos ni explicaciones no "
    "pedidas.\n"
    "- Si te preguntan por una entidad y el nombre exacto no existe pero "
    "hay una claramente equivalente (p.ej. te piden 'estudio' y no existe "
    "esa entidad pero sí una 'office' que es la misma habitación en otro "
    "idioma/nombre), úsala sin preguntar primero — indica en la misma "
    "respuesta, breve, qué entidad has usado en realidad (p.ej. 'La "
    "temperatura del office es 23°C'), en vez de decir que no existe.\n"
    "- Si una petición es ambigua o arriesgada (p.ej. afecta a "
    "climatización, riego, o cierres), pregunta antes de actuar."
)

AGENT_MAX_ITERATIONS = 12
AGENT_MAX_SECONDS = 120
TELEGRAM_POLL_TIMEOUT = 30
