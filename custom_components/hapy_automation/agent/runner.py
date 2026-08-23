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
    CONF_AUDIO_API_BASE_URL,
    CONF_AUDIO_API_KEY,
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


def _safe_truncate_history(history: list[dict], max_len: int) -> list[dict]:
    """A flat `history[-max_len:]` can cut in the middle of an
    assistant(tool_calls) -> tool sequence, leaving a stored history that
    *starts* with an orphaned `tool` message with no preceding tool_calls
    to answer. The next turn then sends that straight to the LLM API,
    which rejects the whole request outright — found for real via a
    "messages with role 'tool' must be a response to a preceding message
    with 'tool_calls'" 400 from OpenAI. A `user` message never has that
    dependency (it always starts a fresh turn), so trim forward to the
    first one at or after the naive cutoff instead of cutting blindly."""
    if len(history) <= max_len:
        return history
    trimmed = history[-max_len:]
    for i, message in enumerate(trimmed):
        if message.get('role') == 'user':
            return trimmed[i:]
    # No user message anywhere in the window (pathological — a single
    # turn alone exceeded max_len). Safer to drop it than send an
    # unpaired tool message and get the whole request rejected.
    return []


def _describe_error(e: Exception) -> str:
    """str(e) is empty for several common exceptions — notably
    asyncio.TimeoutError, which is exactly what a slow reasoning model's
    chat completion raises if it runs past the HTTP timeout. Found for
    real via Telegram: the user just saw "Error del agente:" with nothing
    after it. Always include the exception type so there's something to
    go on either way."""
    message = str(e)
    return f"{type(e).__name__}: {message}" if message else type(e).__name__


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
            audio_base_url=data.get(CONF_AUDIO_API_BASE_URL) or None,
            audio_api_key=data.get(CONF_AUDIO_API_KEY) or None,
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
        logger.info('[hapy_automation agent] starting telegram poll loop')
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
            # `_handle_message` runs as a fire-and-forget task (see `_run`'s
            # `hass.async_create_task` call) — nothing awaits it, so any
            # exception that escapes this method is only ever surfaced via
            # asyncio's default "Task exception was never retrieved"
            # handler, if at all. Found for real: the previous code only
            # wrapped the LLM call itself in try/except, leaving
            # download_file/transcribe/send_message/synthesize/send_voice
            # completely unprotected — a failure in any of those (e.g. the
            # final send_message call) meant the user got no reply and no
            # error, with nothing actionable in the logs either. This outer
            # catch-all guarantees at least one attempt at telling the user
            # something went wrong, and always logs the real exception.
            try:
                logger.info(
                    '[hapy_automation agent] message received from chat_id %s (voice=%s)',
                    chat_id, 'voice' in message,
                )
                await self._process_message(chat_id, message)
                logger.info('[hapy_automation agent] reply sent to chat_id %s', chat_id)
            except Exception as e:
                logger.exception('[hapy_automation agent] processing message failed')
                with contextlib.suppress(Exception):
                    await self.telegram.send_message(chat_id, f'Error del agente: {_describe_error(e)}')

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

        async def _notify_still_working() -> None:
            with contextlib.suppress(Exception):
                await self.telegram.send_message(
                    chat_id, 'Sigo investigando, dame un momento…'
                )

        new_history, response_text = await agent_loop.run(history, text, _notify_still_working)
        self._histories[chat_id] = _safe_truncate_history(new_history, MAX_HISTORY_MESSAGES)

        if is_voice:
            audio = await self.llm.synthesize(response_text)
            if audio:
                await self.telegram.send_voice(chat_id, audio)
                return
        await self.telegram.send_message(chat_id, response_text)
