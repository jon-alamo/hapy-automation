"""Tool definitions (OpenAI tool-calling schema) and dispatcher for the
agent. State/service access is unrestricted (the whole Home Assistant
instance, as requested); file read/write/commit/push is scoped to this
config entry's own automations-repo checkout only.
"""
from __future__ import annotations

import json
import logging
import os
import re

from homeassistant.core import HomeAssistant

from ..runtime.automations import AutomationHandler

logger = logging.getLogger(__name__)

MAX_LIST_STATES_RESULTS = 100

_API_REFERENCE_PATH = os.path.join(os.path.dirname(__file__), 'AUTOMATION_API_REFERENCE.md')


class ToolError(Exception):
    """Message is safe to feed back to the LLM as the tool result."""


TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_state",
            "description": "Get the current real state and attributes of one entity by its entity_id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "entity_id": {"type": "string"},
                },
                "required": ["entity_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_states",
            "description": (
                "List entities and their current state. Must be narrowed with "
                "`domain` and/or `search` (a substring match against entity_id "
                "or friendly name) — results are capped and an unnarrowed query "
                "on a real instance would return too much to be useful."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "domain": {"type": "string", "description": "e.g. 'light', 'climate', 'sensor'"},
                    "search": {"type": "string", "description": "substring to match against entity_id/friendly_name"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "call_service",
            "description": "Call a real Home Assistant service (e.g. domain='light', service='turn_on').",
            "parameters": {
                "type": "object",
                "properties": {
                    "domain": {"type": "string"},
                    "service": {"type": "string"},
                    "entity_id": {"type": "string", "description": "Target entity_id, if applicable"},
                    "data": {"type": "object", "description": "Extra service data fields"},
                },
                "required": ["domain", "service"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_automation_files",
            "description": "List every Python file in the automations repo checkout (automations/, helpers/, etc).",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_automation_file",
            "description": "Read the full contents of a file in the automations repo, by path relative to the repo root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_automation_file",
            "description": (
                "Write (create or overwrite) a file in the automations repo, by "
                "path relative to the repo root. Does not commit or push by "
                "itself — call git_commit_and_push afterwards. If this creates a "
                "new top-level module directly under automations/ (e.g. "
                "automations/foo.py), it is automatically wired into "
                "automations/__init__.py for you (a module that isn't imported "
                "there is never executed and does nothing at all, silently) — "
                "the response tells you if that happened. This does NOT replace "
                "using the real hapy.Automation class API — see "
                "get_automation_api_reference before writing any automation logic."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_commit_and_push",
            "description": (
                "Commit every pending change in the automations repo checkout and "
                "push it, then trigger a real reload and report whether it actually "
                "succeeded. Always check the reload result before telling the user "
                "a change is live — a failed reload means the previous code is "
                "still the one actually running. On success this ALSO returns "
                "`bindings`: which automations actually attached to real "
                "entities/devices vs. which ended up with none (`unbound_or_failed`, "
                "with the error if there was one). reload_ok=true does NOT mean "
                "your automation does anything — a wrong entities.X/devices.X name "
                "inside init_condition() silently produces zero bindings without "
                "failing the reload. Any automation you just wrote appearing in "
                "unbound_or_failed means it does nothing at all; investigate with "
                "list_states/get_state (don't guess a corrected name) and fix it "
                "in the same conversation before telling the user it's done."
            ),
            "parameters": {
                "type": "object",
                "properties": {"message": {"type": "string", "description": "Commit message"}},
                "required": ["message"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_reload_status",
            "description": (
                "Get the current reload status: commit SHA running, last reload "
                "ok/error, and which automations are actually bound to real "
                "entities/devices vs. bound to nothing (`bindings.unbound_or_failed`)."
            ),
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_automation_api_reference",
            "description": (
                "Get the reference guide for the hapy.Automation authoring API "
                "(class contract, entities.X/devices.X access patterns, binding "
                "discovery caveats, repo layout conventions). Call this before "
                "writing or editing automation code, not just from memory."
            ),
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


def _binding_summary() -> dict:
    """Ground truth for "did the automation I just wrote actually attach to
    anything real" — reload_ok alone can't answer that (see
    AutomationHandler.binding_results' docstring): a wrong entities.X/
    devices.X reference inside init_condition() is swallowed as a warning,
    not a reload failure, leaving the automation registered but bound to
    nothing. `unbound` is the list to actually look at after writing new
    automation code."""
    results = AutomationHandler.binding_results
    unbound = {
        automation_id: info["error"]
        for automation_id, info in results.items()
        if not info["bound_to"]
    }
    bound = {
        automation_id: info["bound_to"]
        for automation_id, info in results.items()
        if info["bound_to"]
    }
    return {"bound": bound, "unbound_or_failed": unbound}


class AgentTools:
    def __init__(self, hass: HomeAssistant, coordinator):
        self.hass = hass
        self.coordinator = coordinator

    async def dispatch(self, name: str, arguments: dict) -> str:
        handler = getattr(self, f"_tool_{name}", None)
        if handler is None:
            return json.dumps({"error": f"unknown tool {name}"})
        try:
            result = await handler(**arguments)
        except ToolError as e:
            return json.dumps({"error": str(e)})
        except Exception as e:  # noqa: BLE001 — surfaced to the LLM, not raised
            logger.exception('[hapy_automation agent] tool %s failed', name)
            return json.dumps({"error": f"{type(e).__name__}: {e}"})
        return json.dumps(result, default=str)

    # -- Home Assistant state/services ----------------------------------

    async def _tool_get_state(self, entity_id: str) -> dict:
        state = self.hass.states.get(entity_id)
        if state is None:
            raise ToolError(f"entity {entity_id} not found")
        return {
            "entity_id": state.entity_id,
            "state": state.state,
            "attributes": dict(state.attributes),
            "last_changed": state.last_changed.isoformat(),
        }

    async def _tool_list_states(self, domain: str | None = None, search: str | None = None) -> dict:
        if not domain and not search:
            raise ToolError("narrow the query with `domain` and/or `search`")
        results = []
        for state in self.hass.states.async_all():
            if domain and state.domain != domain:
                continue
            if search:
                needle = search.lower()
                haystack = f"{state.entity_id} {state.attributes.get('friendly_name', '')}".lower()
                if needle not in haystack:
                    continue
            results.append({
                "entity_id": state.entity_id,
                "state": state.state,
                "friendly_name": state.attributes.get("friendly_name"),
            })
            if len(results) >= MAX_LIST_STATES_RESULTS:
                break
        return {"count": len(results), "entities": results}

    async def _tool_call_service(
            self, domain: str, service: str,
            entity_id: str | None = None, data: dict | None = None,
    ) -> dict:
        service_data = dict(data or {})
        if entity_id:
            service_data["entity_id"] = entity_id
        await self.hass.services.async_call(domain, service, service_data, blocking=True)
        return {"called": f"{domain}.{service}", "data": service_data}

    # -- automations repo -------------------------------------------------

    def _resolve_path(self, relative_path: str) -> str:
        repo_path = os.path.realpath(self.coordinator.repo_path)
        candidate = os.path.realpath(os.path.join(repo_path, relative_path))
        if candidate != repo_path and not candidate.startswith(repo_path + os.sep):
            raise ToolError(f"path {relative_path!r} escapes the repo checkout")
        return candidate

    async def _tool_list_automation_files(self) -> dict:
        def _walk() -> list[str]:
            repo_path = self.coordinator.repo_path
            files = []
            for root, dirs, filenames in os.walk(repo_path):
                dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
                for filename in filenames:
                    if filename.endswith('.py'):
                        full = os.path.join(root, filename)
                        files.append(os.path.relpath(full, repo_path))
            return sorted(files)
        return {"files": await self.hass.async_add_executor_job(_walk)}

    async def _tool_read_automation_file(self, path: str) -> dict:
        full_path = self._resolve_path(path)

        def _read() -> str:
            if not os.path.isfile(full_path):
                raise ToolError(f"file {path!r} does not exist")
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        return {"path": path, "content": await self.hass.async_add_executor_job(_read)}

    async def _tool_write_automation_file(self, path: str, content: str) -> dict:
        full_path = self._resolve_path(path)

        def _write() -> None:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        await self.hass.async_add_executor_job(_write)

        wired = await self.hass.async_add_executor_job(self._ensure_wired_into_init, path)

        result = {"path": path, "bytes_written": len(content.encode('utf-8'))}
        if wired:
            result["note"] = (
                f"Also added 'from .{wired} import *' to automations/__init__.py — "
                "a new module under automations/ does nothing at all until it's "
                "imported there; this is done for you, but double check it with "
                "read_automation_file if anything about the layout looks unusual."
            )
        return result

    def _ensure_wired_into_init(self, written_path: str) -> str | None:
        """A new top-level module under automations/ (e.g. automations/foo.py)
        is completely inert — never imported, never bound to anything — unless
        automations/__init__.py imports it. Found for real: an agent wrote a
        whole automation this way, reload reported "ok" (there was nothing
        broken to fail on, since the dead file was never touched), and it
        silently did nothing. Rather than rely on remembering this step
        (documented in AUTOMATION_API_REFERENCE.md, and still missed), just
        do it automatically for the common flat-module-under-automations/
        case; returns the module name if it wired something in, else None."""
        normalized = written_path.replace(os.sep, '/')
        match = re.fullmatch(r'automations/([A-Za-z_][A-Za-z0-9_]*)\.py', normalized)
        if not match:
            return None
        module_name = match.group(1)
        if module_name == '__init__':
            return None

        init_path = os.path.join(self.coordinator.repo_path, 'automations', '__init__.py')
        import_line = f'from .{module_name} import *\n'
        existing = ''
        if os.path.isfile(init_path):
            with open(init_path, 'r', encoding='utf-8') as f:
                existing = f.read()
        if f'.{module_name} import' in existing:
            return None  # already wired, e.g. this was an update not a new file

        with open(init_path, 'a', encoding='utf-8') as f:
            if existing and not existing.endswith('\n'):
                f.write('\n')
            f.write(import_line)
        return module_name

    async def _tool_git_commit_and_push(self, message: str) -> dict:
        sha = await self.hass.async_add_executor_job(
            self.coordinator.git.commit_and_push, message
        )
        if sha is None:
            return {"pushed": False, "reason": "nothing to commit"}
        result = await self.coordinator.async_reload(force=True)
        response = {
            "pushed": True,
            "sha": sha,
            "reload_ok": result.ok,
            "reload_error": result.error,
        }
        if result.ok:
            response["bindings"] = _binding_summary()
        return response

    async def _tool_get_reload_status(self) -> dict:
        c = self.coordinator
        return {
            "current_sha": c.current_sha,
            "last_reload_status": c.last_reload_status,
            "last_reload_error": c.last_reload_error,
            "last_reload_at": c.last_reload_at.isoformat() if c.last_reload_at else None,
            "bindings": _binding_summary(),
        }

    async def _tool_get_automation_api_reference(self) -> dict:
        def _read() -> str:
            with open(_API_REFERENCE_PATH, 'r', encoding='utf-8') as f:
                return f.read()
        return {"reference": await self.hass.async_add_executor_job(_read)}
