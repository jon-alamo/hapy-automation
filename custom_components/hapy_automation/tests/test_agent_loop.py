"""Exercises AgentLoop's iterate-until-done logic against a fake LLM
client and fake tools — no network, no real Home Assistant needed. Covers
the three exit paths: plain-content answer after a tool call, the
iteration-count safety limit, and the wall-clock safety limit.
"""
import asyncio
import json

import pytest

from custom_components.hapy_automation.agent.loop import AgentLoop


class FakeLLM:
    """Replays a fixed script of assistant messages, one per .chat() call."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = 0

    async def chat(self, messages, tools):
        self.calls += 1
        return self.script.pop(0)


class FakeTools:
    def __init__(self):
        self.dispatched = []

    async def dispatch(self, name, arguments):
        self.dispatched.append((name, arguments))
        return json.dumps({"ok": True, "tool": name})


def _assistant_tool_call(name, arguments, call_id="call_1"):
    return {
        "role": "assistant",
        "content": None,
        "tool_calls": [{
            "id": call_id,
            "type": "function",
            "function": {"name": name, "arguments": json.dumps(arguments)},
        }],
    }


def _assistant_text(text):
    return {"role": "assistant", "content": text}


def test_loop_executes_tool_call_then_returns_final_answer():
    llm = FakeLLM([
        _assistant_tool_call("get_state", {"entity_id": "light.office"}),
        _assistant_text("La luz del despacho está encendida."),
    ])
    tools = FakeTools()
    agent = AgentLoop(llm, tools, system_prompt="system", max_iterations=5, max_seconds=30)

    history, response = asyncio.run(agent.run([], "¿cómo está la luz del despacho?"))

    assert response == "La luz del despacho está encendida."
    assert tools.dispatched == [("get_state", {"entity_id": "light.office"})]
    assert llm.calls == 2
    # history carries the user message, the tool-call assistant message,
    # the tool result, and the final assistant message — usable as-is for
    # the next turn's context.
    roles = [m["role"] for m in history]
    assert roles == ["user", "assistant", "tool", "assistant"]


def test_loop_stops_after_max_iterations():
    # The LLM never stops asking for tool calls — the loop must bail out
    # instead of looping forever or exhausting the fake script.
    llm = FakeLLM([_assistant_tool_call("get_state", {"entity_id": "light.office"})] * 3)
    tools = FakeTools()
    agent = AgentLoop(llm, tools, system_prompt="system", max_iterations=3, max_seconds=30)

    history, response = asyncio.run(agent.run([], "haz algo"))

    assert "no he podido" in response.lower() or "no pude" in response.lower()
    assert llm.calls == 3
    assert len(tools.dispatched) == 3


def test_loop_calls_on_progress_once_after_threshold_iteration():
    """Found for real via Telegram: a legitimate multi-step query (7+
    tool-calling rounds, ~4.5 minutes) looked identical to a hung/broken
    bot from the user's side, since nothing was sent until the final
    answer (or the timeout error). on_progress lets the caller send a
    single reassurance message partway through, without spamming one per
    round."""
    llm = FakeLLM([_assistant_tool_call("get_state", {"entity_id": "x"})] * 5 + [
        _assistant_text("listo")
    ])
    tools = FakeTools()
    agent = AgentLoop(llm, tools, system_prompt="system", max_iterations=10, max_seconds=30)

    progress_calls = []

    async def on_progress():
        progress_calls.append(True)

    history, response = asyncio.run(agent.run([], "haz algo largo", on_progress))

    assert response == "listo"
    assert len(progress_calls) == 1


def test_loop_does_not_call_on_progress_for_a_quick_answer():
    llm = FakeLLM([_assistant_text("respuesta rápida")])
    tools = FakeTools()
    agent = AgentLoop(llm, tools, system_prompt="system", max_iterations=10, max_seconds=30)

    progress_calls = []

    async def on_progress():
        progress_calls.append(True)

    asyncio.run(agent.run([], "pregunta simple", on_progress))

    assert progress_calls == []


def test_loop_stops_on_wall_clock_timeout():
    class SlowFakeLLM(FakeLLM):
        async def chat(self, messages, tools):
            await asyncio.sleep(0.05)
            return await super().chat(messages, tools)

    llm = SlowFakeLLM([_assistant_tool_call("get_state", {"entity_id": "x"})] * 100)
    tools = FakeTools()
    agent = AgentLoop(llm, tools, system_prompt="system", max_iterations=100, max_seconds=0.12)

    history, response = asyncio.run(agent.run([], "haz algo lento"))

    assert "tiempo" in response.lower()
    # Should have bailed out after a couple of iterations, not run all 100.
    assert llm.calls < 10
