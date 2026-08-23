"""AgentTools file-access guardrail: the agent must never be able to
read/write outside its own automations-repo checkout, even via `../`
tricks in a path argument."""
import asyncio
import json
import os
import tempfile

import pytest

from custom_components.hapy_automation.agent.tools import AgentTools, ToolError, _binding_summary
from custom_components.hapy_automation.runtime import models
from custom_components.hapy_automation.runtime.automations import Automation, AutomationHandler


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


def test_write_automation_file_auto_wires_new_module_into_init():
    """Found for real: an agent wrote a whole new automation module under
    automations/ but never added the import line to automations/__init__.py
    — the module was never executed, silently did nothing, and reload
    reported "ok" the whole time since there was nothing broken to fail on."""
    with tempfile.TemporaryDirectory() as repo_path:
        os.makedirs(os.path.join(repo_path, 'automations'))
        with open(os.path.join(repo_path, 'automations', '__init__.py'), 'w') as f:
            f.write('from .kitchen import *\n')
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(tools.dispatch(
            'write_automation_file',
            {'path': 'automations/guests.py', 'content': 'x = 1\n'},
        )))
        assert 'note' in result

        with open(os.path.join(repo_path, 'automations', '__init__.py')) as f:
            init_content = f.read()
        assert 'from .guests import *' in init_content
        assert 'from .kitchen import *' in init_content  # untouched


def test_write_automation_file_does_not_duplicate_existing_import():
    with tempfile.TemporaryDirectory() as repo_path:
        os.makedirs(os.path.join(repo_path, 'automations'))
        with open(os.path.join(repo_path, 'automations', '__init__.py'), 'w') as f:
            f.write('from .guests import *\n')
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))

        result = json.loads(asyncio.run(tools.dispatch(
            'write_automation_file',
            {'path': 'automations/guests.py', 'content': 'x = 2\n'},
        )))
        assert 'note' not in result

        with open(os.path.join(repo_path, 'automations', '__init__.py')) as f:
            assert f.read().count('from .guests import') == 1


def test_write_automation_file_outside_automations_dir_is_not_wired():
    with tempfile.TemporaryDirectory() as repo_path:
        tools = AgentTools(hass=FakeHass(), coordinator=FakeCoordinator(repo_path))
        result = json.loads(asyncio.run(tools.dispatch(
            'write_automation_file',
            {'path': 'helpers/utils.py', 'content': 'x = 1\n'},
        )))
        assert 'note' not in result


def test_binding_summary_separates_bound_from_unbound_or_failed():
    AutomationHandler.reset_automations()

    class WorkingEntity(models.Entity):
        entity_id = "sensor.working"
        state = models.State(actual_entity_id=entity_id, state_value="on")

    class WorkingAutomation(Automation):
        def init_condition(self):
            return WorkingEntity.state.changed()

        def action(self):
            pass

    class HallucinatedAutomation(Automation):
        def init_condition(self):
            return entities.TotalPeople.state  # noqa: F821 — deliberately undefined, like the real incident

        def action(self):
            pass

    summary = _binding_summary()
    assert summary["bound"][WorkingAutomation.get_id()] == ["sensor.working"]
    assert HallucinatedAutomation.get_id() in summary["unbound_or_failed"]
    assert "entities" in summary["unbound_or_failed"][HallucinatedAutomation.get_id()]


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
