"""Generates an SSH deploy keypair on request, so a user can skip SSHing
into their Home Assistant host to run `ssh-keygen` by hand. Deliberately
opt-in (see const.AUTH_METHOD_SSH_KEY_GENERATE) rather than automatic on
every setup — the original pip-based hapy/git_sync.py always auto-generated
and printed a key to the log; this integration is meant for any repo/host
combination, where an existing key may already be the right choice.
"""
from __future__ import annotations

import os
import subprocess


class SshKeygenError(Exception):
    """Message is safe to show the user."""


def generate_keypair(key_path: str, comment: str) -> str:
    """Blocking — call via hass.async_add_executor_job. Generates an
    ed25519 keypair at `key_path` if one doesn't already exist there
    (re-entering the config flow after generating once must not silently
    generate a second, different key), and returns the public key text."""
    os.makedirs(os.path.dirname(key_path), exist_ok=True)
    if not os.path.exists(key_path):
        try:
            subprocess.run(
                ['ssh-keygen', '-t', 'ed25519', '-f', key_path, '-N', '', '-C', comment],
                check=True, capture_output=True, text=True,
            )
        except FileNotFoundError as e:
            raise SshKeygenError(
                "ssh-keygen no está disponible en este contenedor de Home Assistant — "
                "genera una clave tú mismo y pon la ruta manualmente."
            ) from e
        except subprocess.CalledProcessError as e:
            raise SshKeygenError(f"ssh-keygen falló: {e.stderr}") from e
        os.chmod(key_path, 0o600)

    with open(key_path + '.pub', 'r', encoding='utf-8') as f:
        return f.read().strip()
