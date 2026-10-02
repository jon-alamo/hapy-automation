"""Runs shell commands on the Home Assistant host over SSH, for the agent's
`run_host_command` tool — the one thing the REST/WebSocket API can't do:
install or uninstall add-ons and integrations, edit config files, run the
`ha` CLI, check disk space, tail real logs.

Uses the system `ssh` binary (already required by git_manager's SSH auth and
ssh_keygen) rather than adding a pip dependency. Unrestricted by design —
whoever can message the bot can run anything the configured SSH user can —
which is why it's opt-in and why the Telegram chat_id allowlist matters.
"""
from __future__ import annotations

import asyncio
import contextlib
import logging

logger = logging.getLogger(__name__)


def truncate_output(text: str, limit: int) -> str:
    """Keeps the head and tail: the start usually says what ran, the end
    usually holds the error or the final result — a middle cut loses less
    than chopping either end off."""
    if len(text) <= limit:
        return text
    half = limit // 2
    omitted = len(text) - 2 * half
    return f"{text[:half]}\n…[{omitted} caracteres omitidos]…\n{text[-half:]}"


class HostShell:
    def __init__(
            self, host: str, port: int, user: str, key_path: str,
            known_hosts_path: str, max_output_chars: int,
    ):
        self.host = host
        self.port = port
        self.user = user
        self.key_path = key_path
        self.known_hosts_path = known_hosts_path
        self.max_output_chars = max_output_chars

    def _ssh_args(self, command: str) -> list[str]:
        return [
            'ssh',
            '-i', self.key_path,
            '-p', str(self.port),
            # No password prompts / interactive questions — fail fast instead.
            '-o', 'BatchMode=yes',
            # Pin the host key on first connect, refuse if it later changes.
            '-o', 'StrictHostKeyChecking=accept-new',
            '-o', f'UserKnownHostsFile={self.known_hosts_path}',
            '-o', 'ConnectTimeout=10',
            f'{self.user}@{self.host}',
            command,
        ]

    async def run(self, command: str, timeout_seconds: float) -> dict:
        logger.warning('[hapy_automation agent] host shell (%s@%s): %s', self.user, self.host, command)
        process = await asyncio.create_subprocess_exec(
            *self._ssh_args(command),
            stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout_seconds)
        except asyncio.TimeoutError:
            with contextlib.suppress(ProcessLookupError):
                process.kill()
            await process.wait()
            return {
                'error': f'timeout tras {timeout_seconds:.0f}s — el comando fue cancelado',
                'timed_out': True,
            }
        return {
            # 255 is ssh's own failure code (couldn't connect / auth failed),
            # not the remote command's — stderr says which.
            'exit_code': process.returncode,
            'stdout': truncate_output(stdout.decode(errors='replace'), self.max_output_chars),
            'stderr': truncate_output(stderr.decode(errors='replace'), self.max_output_chars),
        }
