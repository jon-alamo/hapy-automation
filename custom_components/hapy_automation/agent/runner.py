"""Wires the Telegram long-poll loop to the LLM agent loop: one background
task per config entry with the agent enabled, one conversation history and
lock per Telegram chat_id (so a single chat's messages are handled one at a
time, but different chats/config entries don't block each other).
"""
from __future__ import annotations

import asyncio
import contextlib
import logging

from homeassistant.core import HomeAssistant

from ..const import (
    AGENT_MAX_ITERATIONS,
    AGENT_MAX_SECONDS,
    CONF_LANGUAGE,
    CONF_LLM_API_BASE_URL,
    CONF_LLM_API_KEY,
    CONF_LLM_MODEL,
    CONF_SYSTEM_PROMPT,
    CONF_STT_MODEL,
    CONF_TELEGRAM_ALLOWED_CHAT_IDS,
    CONF_TELEGRAM_BOT_TOKEN,
    CONF_TTS_MODEL,
    CONF_TTS_VOICE,
    DEFAULT_LANGUAGE,
    DEFAULT_STT_MODEL,
    DEFAULT_SYSTEM_PROMPT,
    DEFAULT_TTS_MODEL,
    DEFAULT_TTS_VOICE,
    LANGUAGE_NAMES,
    TELEGRAM_POLL_TIMEOUT,
)
from .llm_client import LLMClient
from .loop import AgentLoop
from .telegram_client import TelegramClient
from .tools import AgentTools

logger = logging.getLogger(__name__)

MAX_HISTORY_MESSAGES = 40


def _parse_chat_ids(raw: str) -> set[int]:
    ids = set()
    for part in raw.split(','):
        part = part.strip()
        if part:
            try:
                ids.add(int(part))
            except ValueError:
                logger.warning('[hapy_automation agent] ignoring invalid chat_id %r', part)
    return ids


class AgentRunner:
    def __init__(self, hass: HomeAssistant, entry, coordinator):
        self.hass = hass
        self.entry = entry
        self.coordinator = coordinator

        data = entry.data
        self.telegram = TelegramClient(hass, data[CONF_TELEGRAM_BOT_TOKEN])
        self.allowed_chat_ids = _parse_chat_ids(data.get(CONF_TELEGRAM_ALLOWED_CHAT_IDS, ''))
        self.llm = LLMClient(
            hass,
            base_url=data[CONF_LLM_API_BASE_URL],
            api_key=data[CONF_LLM_API_KEY],
            model=data[CONF_LLM_MODEL],
            stt_model=data.get(CONF_STT_MODEL, DEFAULT_STT_MODEL),
            tts_model=data.get(CONF_TTS_MODEL, DEFAULT_TTS_MODEL),
            tts_voice=data.get(CONF_TTS_VOICE, DEFAULT_TTS_VOICE),
        )
        self.tools = AgentTools(hass, coordinator)

        self._histories: dict[int, list[dict]] = {}
        self._chat_locks: dict[int, asyncio.Lock] = {}
        self._offset: int | None = None
        self._task: asyncio.Task | None = None

    def _language(self) -> str:
        return self.entry.data.get(CONF_LANGUAGE) or DEFAULT_LANGUAGE

    def _system_prompt(self) -> str:
        base = self.entry.data.get(CONF_SYSTEM_PROMPT) or DEFAULT_SYSTEM_PROMPT
        language = self._language()
        language_name = LANGUAGE_NAMES.get(language, language)
        # Appended, not baked into the editable prompt field itself, so
        # changing `language` always takes effect even if the user has
        # customized system_prompt and forgotten to update it there too.
        # Explicit and unconditional on purpose — found for real: without
        # this, replies drifted into whatever language the model guessed
        # from the (sometimes mis-transcribed) input, which then also
        # made the TTS voice mispronounce everything.
        directive = (
            f"\n\nResponde SIEMPRE en {language_name} ({language}), "
            "sin excepción, sea cual sea el idioma en el que te escriban "
            "o hablen — nunca cambies de idioma a mitad de conversación."
        )
        return base + directive

    def start(self) -> None:
        self._task = self.hass.async_create_background_task(
            self._run(), name='hapy_automation agent telegram poll',
        )

    async def stop(self) -> None:
        if self._task is not None:
            self._task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._task
            self._task = None

    async def _run(self) -> None:
        if not self.allowed_chat_ids:
            logger.warning(
                '[hapy_automation agent] no telegram_allowed_chat_ids configured — '
                'the agent will never respond to anyone. Configure it from the '
                'integration options.'
            )
        await self._discard_backlog()
        while True:
            try:
                updates = await self.telegram.get_updates(
                    self._offset, timeout=TELEGRAM_POLL_TIMEOUT
                )
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception('[hapy_automation agent] getUpdates failed, retrying in 5s')
                await asyncio.sleep(5)
                continue
            for update in updates:
                self._offset = update['update_id'] + 1
                message = update.get('message')
                if message:
                    self.hass.async_create_task(self._handle_message(message))

    async def _discard_backlog(self) -> None:
        """On (re)start, skip whatever was queued before we came up rather
        than replaying possibly-stale messages — Telegram keeps undelivered
        updates until acknowledged via offset."""
        try:
            updates = await self.telegram.get_updates(None, timeout=1)
        except Exception:
            logger.exception('[hapy_automation agent] initial getUpdates failed')
            return
        if updates:
            self._offset = updates[-1]['update_id'] + 1

    async def _handle_message(self, message: dict) -> None:
        chat_id = message.get('chat', {}).get('id')
        if chat_id not in self.allowed_chat_ids:
            logger.debug('[hapy_automation agent] ignoring message from unauthorized chat_id %s', chat_id)
            return

        lock = self._chat_locks.setdefault(chat_id, asyncio.Lock())
        async with lock:
            await self._process_message(chat_id, message)

    async def _process_message(self, chat_id: int, message: dict) -> None:
        is_voice = 'voice' in message
        if is_voice:
            ogg_bytes = await self.telegram.download_file(message['voice']['file_id'])
            text = await self.llm.transcribe(ogg_bytes, language=self._language())
            if text is None:
                await self.telegram.send_message(
                    chat_id, 'No he podido transcribir el audio — ¿puedes escribirlo?'
                )
                return
        elif 'text' in message:
            text = message['text']
        else:
            return

        agent_loop = AgentLoop(
            self.llm, self.tools, self._system_prompt(),
            AGENT_MAX_ITERATIONS, AGENT_MAX_SECONDS,
        )
        history = self._histories.get(chat_id, [])
        try:
            new_history, response_text = await agent_loop.run(history, text)
        except Exception as e:
            logger.exception('[hapy_automation agent] agent loop failed')
            await self.telegram.send_message(chat_id, f'Error del agente: {e}')
            return
        self._histories[chat_id] = new_history[-MAX_HISTORY_MESSAGES:]

        if is_voice:
            audio = await self.llm.synthesize(response_text)
            if audio:
                await self.telegram.send_voice(chat_id, audio)
                return
        await self.telegram.send_message(chat_id, response_text)
