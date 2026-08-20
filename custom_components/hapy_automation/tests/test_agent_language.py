"""AgentRunner._system_prompt() always appends an explicit language
directive — this is what fixes replies drifting into the wrong language
(and, downstream, TTS mispronouncing them) regardless of what language the
user's audio/text came in as."""
from custom_components.hapy_automation.agent.runner import AgentRunner
from custom_components.hapy_automation.const import (
    CONF_ENABLE_AGENT,
    CONF_LANGUAGE,
    CONF_LLM_API_BASE_URL,
    CONF_LLM_API_KEY,
    CONF_LLM_MODEL,
    CONF_TELEGRAM_ALLOWED_CHAT_IDS,
    CONF_TELEGRAM_BOT_TOKEN,
)


class FakeEntry:
    def __init__(self, data):
        self.data = data


BASE_DATA = {
    CONF_ENABLE_AGENT: True,
    CONF_TELEGRAM_BOT_TOKEN: "dummy",
    CONF_TELEGRAM_ALLOWED_CHAT_IDS: "1",
    CONF_LLM_API_BASE_URL: "https://api.openai.com/v1",
    CONF_LLM_API_KEY: "dummy",
    CONF_LLM_MODEL: "gpt-4o-mini",
}


def _make_runner(extra_data=None):
    entry = FakeEntry({**BASE_DATA, **(extra_data or {})})
    return AgentRunner(hass=None, entry=entry, coordinator=None)


def test_default_language_is_spanish_and_appended_to_prompt():
    runner = _make_runner()
    prompt = runner._system_prompt()
    assert "español" in prompt
    assert "es)" in prompt


def test_configured_language_overrides_default():
    runner = _make_runner({CONF_LANGUAGE: "en"})
    prompt = runner._system_prompt()
    assert "English" in prompt
    assert "en)" in prompt


def test_unlisted_language_code_falls_back_to_the_code_itself():
    runner = _make_runner({CONF_LANGUAGE: "nl"})
    prompt = runner._system_prompt()
    assert "nl" in prompt


def test_language_directive_present_even_with_custom_system_prompt():
    runner = _make_runner({"system_prompt": "Eres un asistente muy breve."})
    prompt = runner._system_prompt()
    assert prompt.startswith("Eres un asistente muy breve.")
    assert "Responde SIEMPRE en español" in prompt
