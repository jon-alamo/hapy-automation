"""Real end-to-end coverage (local bare git repos, no mocking) for the
empty-repo auto-scaffold: a fresh repo with no automations/ package gets
one written and pushed automatically; a repo that already has one is left
completely untouched."""
import os
import subprocess
import tempfile

from custom_components.hapy_automation.git_manager import GitManager
from custom_components.hapy_automation.scaffold import write_scaffold


def _git(*args, cwd):
    subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True)


def test_empty_repo_gets_scaffolded_and_pushed():
    with tempfile.TemporaryDirectory() as tmp:
        origin = os.path.join(tmp, 'origin.git')
        clone_path = os.path.join(tmp, 'clone')
        _git('init', '--bare', origin, cwd=tmp)

        gm = GitManager(repo_path=clone_path, repo_url=origin, branch='main', auth_method='none')
        gm.ensure_cloned()
        assert gm.is_empty()
        assert not gm.has_automations_package()

        gm.ensure_branch_checked_out()
        write_scaffold(gm.repo_path)
        sha = gm.commit_and_push('scaffold')

        assert sha is not None
        assert gm.has_automations_package()
        # Actually landed on the remote, not just locally.
        assert gm.fetch_remote_sha() == sha
        with open(os.path.join(clone_path, 'automations', '__init__.py')) as f:
            assert 'hapy.Automation' in f.read()


def test_populated_repo_is_left_untouched():
    with tempfile.TemporaryDirectory() as tmp:
        origin = os.path.join(tmp, 'origin.git')
        seed_path = os.path.join(tmp, 'seed')
        clone_path = os.path.join(tmp, 'clone')
        _git('init', '--bare', origin, cwd=tmp)
        _git('clone', origin, seed_path, cwd=tmp)
        os.makedirs(os.path.join(seed_path, 'automations'))
        with open(os.path.join(seed_path, 'automations', '__init__.py'), 'w') as f:
            f.write('MARKER = "do not touch"\n')
        _git('add', '-A', cwd=seed_path)
        _git('-c', 'user.email=t@example.com', '-c', 'user.name=t', 'commit', '-m', 'real automations', cwd=seed_path)
        _git('push', 'origin', 'HEAD:main', cwd=seed_path)

        gm = GitManager(repo_path=clone_path, repo_url=origin, branch='main', auth_method='none')
        gm.ensure_cloned()

        assert gm.has_automations_package()
        with open(os.path.join(clone_path, 'automations', '__init__.py')) as f:
            assert f.read() == 'MARKER = "do not touch"\n'
