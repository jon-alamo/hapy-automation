"""LLMClient's audio (STT/TTS) provider can be split from the chat
provider — needed because not every OpenAI-compatible chat backend also
exposes /audio/transcriptions and /audio/speech (OpenRouter, for one, is
chat-only). Left unset, audio calls must fall back to the chat
base_url/api_key exactly as before this split existed.
"""
from custom_components.hapy_automation.agent.llm_client import LLMClient


def test_audio_falls_back_to_chat_provider_when_unset():
    client = LLMClient(
        hass=None, base_url="https://openrouter.ai/api/v1", api_key="chat-key",
        model="z-ai/glm-5.2", stt_model="whisper-1", tts_model="tts-1", tts_voice="alloy",
    )
    assert client.audio_base_url == "https://openrouter.ai/api/v1"
    assert client.audio_api_key == "chat-key"


def test_audio_uses_separate_provider_when_set():
    client = LLMClient(
        hass=None, base_url="https://openrouter.ai/api/v1", api_key="chat-key",
        model="z-ai/glm-5.2", stt_model="whisper-1", tts_model="tts-1", tts_voice="alloy",
        audio_base_url="https://api.openai.com/v1", audio_api_key="audio-key",
    )
    assert client.audio_base_url == "https://api.openai.com/v1"
    assert client.audio_api_key == "audio-key"
    # Chat provider is untouched.
    assert client.base_url == "https://openrouter.ai/api/v1"
    assert client.api_key == "chat-key"


def test_trailing_slash_is_stripped_from_both_base_urls():
    client = LLMClient(
        hass=None, base_url="https://openrouter.ai/api/v1/", api_key="k",
        model="m", stt_model="s", tts_model="t", tts_voice="v",
        audio_base_url="https://api.openai.com/v1/",
    )
    assert client.base_url == "https://openrouter.ai/api/v1"
    assert client.audio_base_url == "https://api.openai.com/v1"
