"""Host shell access for the agent: opt-in, so the tool must not even be
offered to the LLM (or executable if it names it anyway) unless enabled;
the ssh invocation must be non-interactive and pin host keys; output and
runtime are bounded.
"""
import asyncio
import json
from types import SimpleNamespace

from custom_components.hapy_automation.agent import host_shell
from custom_components.hapy_automation.agent.host_shell import HostShell, truncate_output
from custom_components.hapy_automation.agent.tools import (
    HOST_SHELL_SCHEMA,
    TOOL_SCHEMAS,
    AgentTools,
)


class FakeProcess:
    def __init__(self, stdout=b"", stderr=b"", returncode=0, hang=False):
        self._stdout, self._stderr, self.returncode, self._hang = stdout, stderr, returncode, hang
        self.killed = False

    async def communicate(self):
        if self._hang:
            await asyncio.sleep(10)
        return self._stdout, self._stderr

    def kill(self):
        self.killed = True

    async def wait(self):
        return self.returncode


def _shell():
    return HostShell(
        host="core-ssh", port=22, user="root", key_path="/config/.ssh/k",
        known_hosts_path="/config/.ssh/kh", max_output_chars=100,
    )


def _patch_subprocess(monkeypatch, process):
    captured = {}

    async def fake_exec(*args, **kwargs):
        captured["args"], captured["kwargs"] = args, kwargs
        return process

    monkeypatch.setattr(host_shell.asyncio, "create_subprocess_exec", fake_exec)
    return captured


def test_ssh_invocation_is_noninteractive_and_pins_host_keys(monkeypatch):
    captured = _patch_subprocess(monkeypatch, FakeProcess(stdout=b"ok\n"))

    result = asyncio.run(_shell().run("ha core check", 30))

    args = list(captured["args"])
    assert args[0] == "ssh"
    assert args[-2:] == ["root@core-ssh", "ha core check"]
    assert "BatchMode=yes" in args
    assert "StrictHostKeyChecking=accept-new" in args
    assert "UserKnownHostsFile=/config/.ssh/kh" in args
    assert captured["kwargs"]["stdin"] == asyncio.subprocess.DEVNULL
    assert result == {"exit_code": 0, "stdout": "ok\n", "stderr": ""}


def test_nonzero_exit_is_returned_not_raised(monkeypatch):
    _patch_subprocess(monkeypatch, FakeProcess(stderr=b"boom", returncode=3))

    result = asyncio.run(_shell().run("false", 30))

    assert result["exit_code"] == 3
    assert result["stderr"] == "boom"


def test_timeout_kills_the_process(monkeypatch):
    process = FakeProcess(hang=True)
    _patch_subprocess(monkeypatch, process)

    result = asyncio.run(_shell().run("sleep 999", 0.05))

    assert process.killed
    assert result["timed_out"] is True
    assert "timeout" in result["error"]


def test_truncate_output_keeps_head_and_tail():
    text = "A" * 50 + "B" * 50 + "C" * 50
    out = truncate_output(text, 40)
    assert out.startswith("A" * 20)
    assert out.endswith("C" * 20)
    assert "omitidos" in out
    assert truncate_output("short", 40) == "short"


def _tools(data):
    coordinator = SimpleNamespace(entry=SimpleNamespace(data=data))
    hass = SimpleNamespace(config=SimpleNamespace(path=lambda *p: "/config/" + "/".join(p)))
    return AgentTools(hass, coordinator)


def test_tool_is_only_offered_when_enabled():
    assert _tools({}).schemas == TOOL_SCHEMAS
    assert HOST_SHELL_SCHEMA not in _tools({"enable_host_shell": False}).schemas
    assert HOST_SHELL_SCHEMA in _tools({"enable_host_shell": True}).schemas


def test_disabled_tool_cannot_be_called_even_if_the_llm_names_it():
    result = json.loads(asyncio.run(_tools({}).dispatch("run_host_command", {"command": "id"})))
    assert "unknown tool" in result["error"]


def test_enabled_but_unconfigured_reports_how_to_finish_setup():
    tools = _tools({"enable_host_shell": True})
    result = json.loads(asyncio.run(tools.dispatch("run_host_command", {"command": "id"})))
    assert "not configured" in result["error"]


def test_enabled_tool_runs_command_with_clamped_timeout(monkeypatch):
    seen = {}

    async def fake_run(self, command, timeout_seconds):
        seen.update(command=command, timeout=timeout_seconds, host=self.host, user=self.user)
        return {"exit_code": 0, "stdout": "", "stderr": ""}

    monkeypatch.setattr(HostShell, "run", fake_run)
    tools = _tools({
        "enable_host_shell": True, "host_shell_host": "192.168.1.20",
        "host_shell_key_path": "/config/.ssh/k",
    })

    asyncio.run(tools.dispatch("run_host_command", {"command": "ha core check", "timeout_seconds": 99999}))

    assert seen == {"command": "ha core check", "timeout": 300, "host": "192.168.1.20", "user": "root"}
