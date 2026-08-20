"""The "iterate until done" agent loop: send the conversation + tool
definitions to the LLM; if it asks for tool calls, execute them and feed
the results back; repeat until it answers with plain content, or a safety
limit (iteration count or wall-clock time) is hit — in which case the user
is told the agent gave up, instead of the conversation just hanging.
"""
from __future__ import annotations

import json
import logging
import time

from .llm_client import LLMClient
from .tools import TOOL_SCHEMAS, AgentTools

logger = logging.getLogger(__name__)


class AgentLoop:
    def __init__(
            self, llm: LLMClient, tools: AgentTools, system_prompt: str,
            max_iterations: int, max_seconds: float,
    ):
        self.llm = llm
        self.tools = tools
        self.system_prompt = system_prompt
        self.max_iterations = max_iterations
        self.max_seconds = max_seconds

    async def run(self, history: list[dict], user_message: str) -> tuple[list[dict], str]:
        """`history` is the prior conversation (no system message — that's
        prepended fresh each call so an edited system prompt takes effect
        immediately on the next message, not just for new conversations).
        Returns (new_history, final_text_response); `new_history` is what
        the caller should persist for the next turn.
        """
        history = list(history) + [{"role": "user", "content": user_message}]
        messages = [{"role": "system", "content": self.system_prompt}] + history

        start = time.monotonic()
        for iteration in range(self.max_iterations):
            if time.monotonic() - start > self.max_seconds:
                text = (
                    "No he podido terminar la tarea a tiempo (límite de "
                    f"{self.max_seconds:.0f}s alcanzado). ¿Quieres que lo "
                    "intente de nuevo o prefieres acotar la petición?"
                )
                history.append({"role": "assistant", "content": text})
                return history, text

            assistant_message = await self.llm.chat(messages, TOOL_SCHEMAS)
            messages.append(assistant_message)
            history.append(assistant_message)

            tool_calls = assistant_message.get("tool_calls")
            if not tool_calls:
                text = assistant_message.get("content") or "(sin respuesta del modelo)"
                return history, text

            for call in tool_calls:
                fn = call["function"]
                name = fn["name"]
                try:
                    arguments = json.loads(fn.get("arguments") or "{}")
                except json.JSONDecodeError:
                    arguments = {}
                logger.debug('[hapy_automation agent] tool call: %s(%s)', name, arguments)
                result = await self.tools.dispatch(name, arguments)
                tool_message = {
                    "role": "tool",
                    "tool_call_id": call["id"],
                    "content": result,
                }
                messages.append(tool_message)
                history.append(tool_message)

        text = (
            f"No he podido terminar la tarea en {self.max_iterations} pasos. "
            "¿Quieres que siga, o prefieres replantear la petición?"
        )
        history.append({"role": "assistant", "content": text})
        return history, text
