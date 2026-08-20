"""Git checkout management for a config entry's automations repo.

Ported concept from hapy/git_sync.py, but reshaped for the new reload
design (see plan doc, "Reload fiable"):
  - No filesystem-based CommitGuard (`.hapy_last_good_commit` /
    `.hapy_blocked_commit` files next to the checkout). SHA bookkeeping is
    the caller's (coordinator's) responsibility, backed by the config
    entry, not loose files.
  - No SSH key auto-generation (hapy/git_sync.py's setup_ssh()). This is
    now a generic integration for any user's repo, so the config flow
    asks for a path to a deploy key the user already placed under
    /config/.ssh/ (or an HTTPS personal access token) instead of the
    integration minting and printing its own key.
  - All git operations are blocking (GitPython) — callers must run them
    via hass.async_add_executor_job, never directly on the event loop.
"""
from __future__ import annotations

import logging
import os
import shutil

import git

from .const import AUTH_METHOD_PAT, AUTH_METHOD_SSH_KEY

logger = logging.getLogger(__name__)


class GitOperationError(Exception):
    """Raised when a git operation fails; message is safe to show the user."""


class GitManager:
    def __init__(
            self,
            repo_path: str,
            repo_url: str,
            branch: str,
            auth_method: str,
            ssh_key_path: str | None = None,
            personal_access_token: str | None = None,
    ):
        self.repo_path = repo_path
        self.repo_url = repo_url
        self.branch = branch
        self.auth_method = auth_method
        self.ssh_key_path = ssh_key_path
        self.personal_access_token = personal_access_token

    # -- auth -----------------------------------------------------------

    def _git_env(self) -> dict:
        env = dict(os.environ)
        if self.auth_method == AUTH_METHOD_SSH_KEY and self.ssh_key_path:
            env['GIT_SSH_COMMAND'] = (
                f'ssh -i "{self.ssh_key_path}" -o IdentitiesOnly=yes '
                f'-o StrictHostKeyChecking=accept-new'
            )
        return env

    def _clone_url(self) -> str:
        if self.auth_method == AUTH_METHOD_PAT and self.personal_access_token:
            if self.repo_url.startswith('https://'):
                return self.repo_url.replace(
                    'https://', f'https://x-access-token:{self.personal_access_token}@', 1
                )
        return self.repo_url

    # -- plumbing (blocking — call via hass.async_add_executor_job) -----

    def ensure_cloned(self) -> None:
        git_dir = os.path.join(self.repo_path, '.git')
        if os.path.isdir(git_dir):
            return
        os.makedirs(self.repo_path, exist_ok=True)
        try:
            git.Repo.clone_from(
                self._clone_url(),
                self.repo_path,
                branch=self.branch,
                env=self._git_env(),
            )
        except git.GitCommandError as e:
            shutil.rmtree(self.repo_path, ignore_errors=True)
            raise GitOperationError(
                f"No se pudo clonar {self.repo_url} (rama {self.branch}): {e}"
            ) from e

    def _repo(self) -> git.Repo:
        return git.Repo(self.repo_path)

    def fetch_remote_sha(self) -> str:
        """Fetch and return the remote branch's current commit SHA, without
        touching the local working tree."""
        repo = self._repo()
        with repo.git.custom_environment(**self._git_env()):
            repo.remotes.origin.fetch()
        return repo.commit(f'origin/{self.branch}').hexsha

    def current_sha(self) -> str | None:
        try:
            return self._repo().head.commit.hexsha
        except Exception:
            return None

    def checkout_sha(self, sha: str) -> None:
        repo = self._repo()
        repo.git.reset('--hard', sha)

    def checkout_branch_head(self) -> str:
        """Fetch + hard-reset to origin/<branch>'s current head, returns the
        SHA that ended up checked out."""
        repo = self._repo()
        with repo.git.custom_environment(**self._git_env()):
            repo.remotes.origin.fetch()
        sha = repo.commit(f'origin/{self.branch}').hexsha
        repo.git.reset('--hard', sha)
        return sha
