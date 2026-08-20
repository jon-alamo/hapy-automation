"""Minimal starter content written into a freshly-configured automations
repo that doesn't have an `automations/` package yet — so pointing this
integration at a brand-new, empty GitHub repo works out of the box instead
of requiring the user to hand-create the expected layout first. See
coordinator._maybe_scaffold_repo, the only caller."""
import os

INIT_PY_CONTENT = '''"""Your hapy_automation automations live here.

This package started empty — add your own modules (e.g. `lighting.py`,
`climate.py`) and import them below, one line per module:

    from .lighting import *
    from .climate import *

Each module defines one or more hapy.Automation subclasses. Example:

    import hapy
    import entities


    class OnMyLightTurnedOn(hapy.Automation):

        def init_condition(self):
            return entities.MyLight.state.changed(old_value='off', new_value='on')

        def action(self):
            entities.MySecondLight.services.turn_off()

`entities`/`devices`/`domains` are generated fresh from your live Home
Assistant state on every reload — never write or commit them yourself.
See the integration's README, or ask its conversational agent (if you
enabled it) to explain the API.
"""
'''

GITIGNORE_CONTENT = "__pycache__/\n*.pyc\n"


def write_scaffold(repo_path: str) -> None:
    automations_dir = os.path.join(repo_path, 'automations')
    os.makedirs(automations_dir, exist_ok=True)
    with open(os.path.join(automations_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(INIT_PY_CONTENT)

    gitignore_path = os.path.join(repo_path, '.gitignore')
    if not os.path.isfile(gitignore_path):
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write(GITIGNORE_CONTENT)
