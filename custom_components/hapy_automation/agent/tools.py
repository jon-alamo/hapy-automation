"""Tool definitions (OpenAI tool-calling schema) and dispatcher for the
agent. State/service access is unrestricted (the whole Home Assistant
instance, as requested); file read/write/commit/push is scoped to this
config entry's own automations-repo checkout only.
"""
from __future__ import annotations

import json
import logging
import os

from homeassistant.core import HomeAssistant

logger = logging.getLogger(__name__)

MAX_LIST_STATES_RESULTS = 100


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
                "itself — call git_commit_and_push afterwards."
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
                "still the one actually running."
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
            "description": "Get the current reload status: commit SHA running, last reload ok/error.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


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
        return {"path": path, "bytes_written": len(content.encode('utf-8'))}

    async def _tool_git_commit_and_push(self, message: str) -> dict:
        sha = await self.hass.async_add_executor_job(
            self.coordinator.git.commit_and_push, message
        )
        if sha is None:
            return {"pushed": False, "reason": "nothing to commit"}
        result = await self.coordinator.async_reload(force=True)
        return {
            "pushed": True,
            "sha": sha,
            "reload_ok": result.ok,
            "reload_error": result.error,
        }

    async def _tool_get_reload_status(self) -> dict:
        c = self.coordinator
        return {
            "current_sha": c.current_sha,
            "last_reload_status": c.last_reload_status,
            "last_reload_error": c.last_reload_error,
            "last_reload_at": c.last_reload_at.isoformat() if c.last_reload_at else None,
        }
