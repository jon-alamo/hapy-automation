"""Client for an OpenAI-compatible LLM endpoint: chat completions with
tool-calling (the de-facto standard shape across OpenAI itself and
self-hosted backends like Ollama/vLLM/LM Studio/OpenRouter), plus
best-effort speech-to-text and text-to-speech for the voice path. STT/TTS
are optional — not every OpenAI-compatible backend implements the audio
endpoints, so failures there are caught and reported as unavailable rather
than raised, letting the caller fall back to text.
"""
from __future__ import annotations

import logging

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(
            self, hass: HomeAssistant, base_url: str, api_key: str, model: str,
            stt_model: str, tts_model: str, tts_voice: str,
    ):
        self._hass = hass
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.model = model
        self.stt_model = stt_model
        self.tts_model = tts_model
        self.tts_voice = tts_voice

    @property
    def _session(self) -> aiohttp.ClientSession:
        return async_get_clientsession(self._hass)

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"}

    async def chat(self, messages: list[dict], tools: list[dict]) -> dict:
        """Returns the assistant message dict: {role, content, tool_calls?}."""
        payload = {
            "model": self.model,
            "messages": messages,
            "tools": tools,
            "tool_choice": "auto",
        }
        async with self._session.post(
                f"{self.base_url}/chat/completions",
                json=payload, headers=self._headers(),
                timeout=aiohttp.ClientTimeout(total=90),
        ) as resp:
            data = await resp.json()
            if resp.status >= 400:
                raise RuntimeError(f"LLM chat completion failed ({resp.status}): {data}")
        return data["choices"][0]["message"]

    async def transcribe(self, ogg_bytes: bytes) -> str | None:
        """Best-effort speech-to-text. Returns None if the endpoint
        doesn't support it or the call fails, rather than raising —
        callers should fall back to asking the user to type instead."""
        form = aiohttp.FormData()
        form.add_field("model", self.stt_model)
        form.add_field(
            "file", ogg_bytes, filename="voice.ogg", content_type="audio/ogg"
        )
        try:
            async with self._session.post(
                    f"{self.base_url}/audio/transcriptions",
                    data=form, headers=self._headers(),
                    timeout=aiohttp.ClientTimeout(total=60),
            ) as resp:
                data = await resp.json()
                if resp.status >= 400:
                    logger.warning('[hapy_automation agent] transcription failed: %s', data)
                    return None
                return data.get("text")
        except Exception:
            logger.exception('[hapy_automation agent] transcription request failed')
            return None

    async def synthesize(self, text: str) -> bytes | None:
        """Best-effort text-to-speech, requesting an Opus/Ogg payload
        (what Telegram's sendVoice wants directly). Returns None if the
        endpoint doesn't support it or the call fails."""
        payload = {
            "model": self.tts_model,
            "voice": self.tts_voice,
            "input": text,
            "response_format": "opus",
        }
        try:
            async with self._session.post(
                    f"{self.base_url}/audio/speech",
                    json=payload, headers=self._headers(),
                    timeout=aiohttp.ClientTimeout(total=60),
            ) as resp:
                if resp.status >= 400:
                    body = await resp.text()
                    logger.warning('[hapy_automation agent] speech synthesis failed: %s', body)
                    return None
                return await resp.read()
        except Exception:
            logger.exception('[hapy_automation agent] speech synthesis request failed')
            return None
