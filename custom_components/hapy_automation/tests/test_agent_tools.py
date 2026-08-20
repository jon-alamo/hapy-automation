"""AgentTools file-access guardrail: the agent must never be able to
read/write outside its own automations-repo checkout, even via `../`
tricks in a path argument."""
import asyncio
import json
import os
import tempfile

import pytest

from custom_components.hapy_automation.agent.tools import AgentTools, ToolError


class FakeCoordinator:
    def __init__(self, repo_path):
        self.repo_path = repo_path


class FakeHass:
    async def async_add_executor_job(self, func, *args):
        return func(*args)


def test_write_and_read_within_repo_roundtrip():
    with tempfile.TemporaryDirectory() as repo_path:
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(
            tools.dispatch("write_automation_file", {"path": "automations/foo.py", "content": "x = 1\n"})
        ))
        assert result["bytes_written"] == len("x = 1\n")

        result = json.loads(asyncio.run(
            tools.dispatch("read_automation_file", {"path": "automations/foo.py"})
        ))
        assert result["content"] == "x = 1\n"


def test_path_traversal_is_rejected():
    with tempfile.TemporaryDirectory() as repo_path:
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(
            tools.dispatch("read_automation_file", {"path": "../../etc/passwd"})
        ))
        assert "error" in result
        assert "escapes" in result["error"]


def test_write_outside_repo_via_absolute_path_is_rejected():
    with tempfile.TemporaryDirectory() as repo_path:
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(
            tools.dispatch("write_automation_file", {"path": "/etc/passwd", "content": "pwned"})
        ))
        assert "error" in result


def test_get_automation_api_reference_returns_real_guide_content():
    with tempfile.TemporaryDirectory() as repo_path:
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(
            tools.dispatch("get_automation_api_reference", {})
        ))
        assert "error" not in result
        reference = result["reference"]
        # Not just a smoke check that *some* string came back — confirm
        # the actual API surface an automation author needs is in there.
        assert "init_condition" in reference
        assert "exit_condition" in reference
        assert "entities.X.state.changed" in reference
        assert "devices.X" in reference
