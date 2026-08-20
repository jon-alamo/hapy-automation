"""Minimal Telegram Bot API client over aiohttp (the session HA already
manages via async_get_clientsession — no new pip dependency). Long-polling
only (getUpdates): no public HTTPS endpoint/webhook needed, matching the
rest of this integration's "no extra infrastructure" design.
"""
from __future__ import annotations

import logging

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

logger = logging.getLogger(__name__)

API_BASE = "https://api.telegram.org"


class TelegramError(Exception):
    pass


class TelegramClient:
    def __init__(self, hass: HomeAssistant, bot_token: str):
        self._hass = hass
        self._token = bot_token

    @property
    def _session(self) -> aiohttp.ClientSession:
        return async_get_clientsession(self._hass)

    def _url(self, method: str) -> str:
        return f"{API_BASE}/bot{self._token}/{method}"

    async def _post(self, method: str, http_timeout: int = 30, **params) -> dict:
        # `http_timeout` (our aiohttp client-side deadline) is deliberately
        # a different name from Telegram's own `timeout` request parameter
        # (the long-poll duration, sent as part of **params for getUpdates)
        # — passing both as `timeout=` collided as a duplicate keyword
        # argument, found the first time this actually ran against the
        # real bot (never exercised locally, since it needs a live token).
        client_timeout = aiohttp.ClientTimeout(total=http_timeout + 10)
        async with self._session.post(
                self._url(method), json=params, timeout=client_timeout
        ) as resp:
            data = await resp.json()
        if not data.get("ok"):
            raise TelegramError(f"{method} failed: {data}")
        return data["result"]

    async def get_updates(self, offset: int | None, timeout: int = 30) -> list[dict]:
        """Long-poll for new updates. Blocks up to `timeout` seconds
        server-side if there's nothing new yet."""
        params = {"timeout": timeout, "allowed_updates": ["message"]}
        if offset is not None:
            params["offset"] = offset
        return await self._post("getUpdates", http_timeout=timeout, **params)

    async def send_message(self, chat_id: int, text: str) -> None:
        # Telegram's hard limit is 4096 chars per message; split long
        # replies instead of letting the API reject them outright.
        chunk_size = 3900
        for i in range(0, len(text), chunk_size) or [0]:
            chunk = text[i:i + chunk_size] or "(sin contenido)"
            await self._post("sendMessage", chat_id=chat_id, text=chunk)

    async def send_voice(self, chat_id: int, ogg_bytes: bytes) -> None:
        form = aiohttp.FormData()
        form.add_field("chat_id", str(chat_id))
        form.add_field(
            "voice", ogg_bytes, filename="voice.ogg", content_type="audio/ogg"
        )
        async with self._session.post(self._url("sendVoice"), data=form) as resp:
            data = await resp.json()
        if not data.get("ok"):
            raise TelegramError(f"sendVoice failed: {data}")

    async def download_file(self, file_id: str) -> bytes:
        info = await self._post("getFile", file_id=file_id)
        file_path = info["file_path"]
        url = f"{API_BASE}/file/bot{self._token}/{file_path}"
        async with self._session.get(url) as resp:
            if resp.status != 200:
                raise TelegramError(f"download_file failed: HTTP {resp.status}")
            return await resp.read()
