# Hapy Automation

A Home Assistant integration that runs **Python-authored automations** directly
inside Home Assistant's own process, deployed straight from a git repository
you own. Write automations with a small, typed API against your instance's
real entities, devices and services — push to your repo, and Hapy Automation
picks it up automatically.

No separate container, no external service, no outbound connection to Home
Assistant to maintain: the integration runs in-process, reads live state from
`hass`, and reloads itself by polling (and optionally a webhook) your repo.

## How it works

1. You point the integration at a git repository containing your automations,
   written in Python against the API described below.
2. On every reload, Hapy Automation generates three modules in memory —
   `entities.py`, `devices.py`, `domains.py` — from your Home Assistant
   instance's *current* live state (`hass.states`, the entity/device
   registries, the service registry). These give you a typed class per
   entity/device/service domain to write automations against, and IDE
   autocompletion when you export them locally (see below).
3. Your repository's `automations` package is imported against those
   generated modules. Every `hapy.Automation` subclass you define registers
   and binds itself automatically — no manual wiring.
4. The integration polls your repo on an interval (and/or listens on a
   webhook) for new commits. On a new commit: fetch, checkout, regenerate,
   reimport, rebind — atomically. If anything in that sequence fails, the
   previous known-good state keeps running untouched and the checkout rolls
   back; nothing is left half-updated.

## Installation

Not yet published to the default HACS store. Add it as a custom repository:

1. HACS → Integrations → ⋮ menu → **Custom repositories**.
2. Add `https://github.com/jon-alamo/hapy-automation`, category **Integration**.
3. Install **Hapy Automation**, then restart Home Assistant.
4. Settings → Devices & services → **Add integration** → search for
   *Hapy Automation*.

## Configuration

The config flow asks for:

| Field | Description |
|---|---|
| Repository URL | SSH (`git@github.com:you/your-automations.git`) or HTTPS |
| Branch | Defaults to `main` |
| Auth method | `ssh_key`, `personal_access_token`, or `none` for a public repo |
| SSH key path | For `ssh_key`: path to a private key file already placed under `/config/.ssh/` (e.g. `/config/.ssh/id_ed25519`). Generate one yourself and add the public half as a **deploy key** on your repository — this integration never generates or stores keys for you. **Read-only is enough** if the repo already has an `automations/` package; give the deploy key **write access** if you want an empty repo auto-scaffolded (see below), or if you'll enable the conversational agent's `git_commit_and_push`. |
| Personal access token | For `personal_access_token`: a token with read access to the repo — **write access too** for the same auto-scaffold/agent-push cases as above |
| Entity include pattern | Regex; see **Entity filtering** below |
| Poll interval (minutes) | How often to check the repo for new commits (default 1) |
| Dry run | See below (default **on**) |
| Enable webhook | Registers a Home Assistant webhook for near-instant reload on push, in addition to polling |

All of these can be changed later from the integration's **Configure** options.

### Dry run

New installs start in dry-run mode. In dry run, everything runs for real —
your repo is cloned, entities/devices/domains are generated, automations are
imported and bound, and `init_condition()` is evaluated on every real event —
**except** that no Home Assistant service call actually goes out;
`entities.X.services.turn_on(...)` etc. are logged instead of executed. Use
this to verify your repository loads cleanly and automations bind to what you
expect (check the diagnostic sensors below) before flipping it off.

### Empty repo → auto-scaffold

You can point this integration at a brand-new, completely empty GitHub repo.
If reload doesn't find an `automations/__init__.py` in it, it writes a
minimal starter package itself (a docstring showing the API, ready for your
own modules) and **pushes that commit itself**, then proceeds normally. A
repo that already has an `automations/` package is left completely
untouched — this only ever happens once, the first time.

**This requires write access on whatever credentials you configured**
(deploy key or personal access token) — a read-only key works fine for
day-to-day reload of an already-populated repo, but can't push the initial
scaffold to an empty one. If you don't want to grant write access, just
create the `automations/` package (with an empty `__init__.py`) yourself
before pointing the integration at the repo, and read-only stays enough.

### Entity filtering

A real Home Assistant instance can have thousands of entities; generating a
class for every single one makes `entities.py` unwieldy and slow to browse.
By convention:

- Entities in directly-actionable domains (`light`, `switch`, `climate`,
  `cover`, `input_boolean`, `select`, `sun`, `zone`, `person`, and similar —
  see `const.ALWAYS_INCLUDED_DOMAINS`) are always included.
- Everything else (most of `sensor`, `binary_sensor`, `device_tracker`, which
  can number in the hundreds) is only included if its `entity_id` matches
  **Entity include pattern**. The suggested convention is to rename entities
  you want available as `..._hapy` in Home Assistant and set the pattern to
  `_hapy$`.

### Webhook

If enabled, the integration registers a webhook at
`https://<your-ha-instance>/api/webhook/<webhook_id>` (the id is generated
automatically and shown in the integration's options). Point a GitHub Action
or your repo's webhook settings at it on push for near-instant reload; polling
remains as a reliable fallback if the webhook is unreachable.

## Diagnostic entities

Each configured repo gets:

- `sensor.<repo>_hapy_automation_current_commit` — the commit SHA currently
  running.
- `sensor.<repo>_hapy_automation_last_reload_status` — `ok` or `error`, with
  the full error message as an attribute if something failed.
- `sensor.<repo>_hapy_automation_last_would_have_fired` — in dry run, the
  last automation that would have executed `action()`.
- `button.<repo>_hapy_automation_reload_now` — force an immediate reload.

Check the current-commit sensor against your repo's actual HEAD, not just the
absence of errors in the log, when you want to confirm a push really landed —
these sensors are the source of truth, not the log. If your instance sets a
restrictive default log level (e.g. `logger: default: critical` in
`configuration.yaml`), this integration's own log lines — including real
errors — will be silently suppressed and you won't see them even though
something did go wrong; the diagnostic sensors above don't depend on log
level at all. To see the logs anyway for troubleshooting, call
`logger.set_level` with `custom_components.hapy_automation: debug` (Developer
Tools → Actions, or the `logger.set_level` service) — this resets on every
Home Assistant restart.

## Services

- `hapy_automation.reload` — force a reload of all configured repos now.
- `hapy_automation.export_stubs` — write the currently-generated
  `entities.py`/`devices.py`/`domains.py` to a folder (default
  `<config>/www/hapy_automation_stubs`) so you can copy them into your local
  checkout for IDE autocompletion. These files are never committed back to
  your repo automatically.

## Conversational agent (optional)

Talk to your automations over Telegram, in text or voice: an LLM (any
OpenAI-compatible endpoint — OpenAI itself, or a self-hosted one) with tool
access to your live Home Assistant state *and* to this repo can answer
questions, and read/write/commit/push automation code on request, iterating
with its tools until the request is actually done rather than answering in
one shot.

Disabled by default. Enable it either during initial setup (a second,
skippable "Agent" step right after the repo step) or later from
**Configure → Agente conversacional**.

### Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) on Telegram
   (`/newbot`) — you get a bot token.
2. Message your new bot once (anything), then find your numeric `chat_id`:
   `https://api.telegram.org/bot<TOKEN>/getUpdates` and look for
   `"chat":{"id": ...}`.
3. Fill in the agent step/options:

| Field | Description |
|---|---|
| Enable agent | Off by default |
| Telegram bot token | From @BotFather |
| Allowed chat_ids | Comma-separated. **Required** — a bot token alone isn't access control; messages from any other chat_id are silently ignored |
| LLM API base URL | e.g. `https://api.openai.com/v1`, or any OpenAI-compatible self-hosted endpoint |
| LLM API key | |
| LLM model | Any tool-calling-capable chat model, e.g. `gpt-4o-mini` |
| System prompt | Editable, sensible default provided — see below |
| Language | ISO-639-1 (default `es`) — pins both the expected speech-to-text language and the language the agent always replies in, regardless of what language it's addressed in |
| STT / TTS model, TTS voice | Only used for voice messages; default to OpenAI's `whisper-1`/`tts-1`/`alloy`. Not every OpenAI-compatible backend implements the audio endpoints — if yours doesn't, voice input degrades to "please type instead" instead of failing silently |

Changing the system prompt or language takes effect on the very next
message — no restart or reload needed.

### What it can do

Text in → text out; voice in → voice out (transcribed, then replied to with
a synthesized voice note). Tool access:

- **Home Assistant, unrestricted**: `get_state`, `list_states` (domain/search
  filtered), `call_service` — the whole instance, not just this repo's
  entities.
- **This repo's checkout, scoped and path-guarded**: `list_automation_files`,
  `read_automation_file`, `write_automation_file`, `git_commit_and_push`
  (stages everything, commits, pushes, then triggers a real reload and
  reports back whether it actually succeeded — the agent checks this and
  self-corrects before telling you it's done, same as it would for any other
  reload). **Needs write access** on the configured deploy key/token, same
  requirement as the empty-repo auto-scaffold above.
- **`get_automation_api_reference`**: a bundled guide to the `hapy.Automation`
  authoring API, which the default system prompt tells the agent to consult
  before writing or editing code rather than relying on memory.
- **`get_reload_status`**: same data as the diagnostic sensors.

There's no separate dry-run gate for the agent's own pushes — the safety net
is the same atomic reload-with-rollback every other push already goes
through (see **Dry run** above for what that guarantees).

Each Telegram chat gets its own conversation history (kept in memory, capped,
lost on restart) and its own request queue, so messages in one chat are
handled one at a time but different chats don't block each other. A single
request is capped at 12 tool-call iterations / 120 seconds — past that the
agent tells you it gave up instead of hanging.

## Writing automations

Your repository needs, at minimum, a top-level `automations` package —
typically a directory with an `__init__.py` that imports every submodule
(`from .lighting import *`, etc.), matching however you like to organize
files. Anything else in the repo (a `helpers` package, constants, etc.) is
just plain Python you can import from your automation modules.

Do **not** commit generated `entities.py`/`devices.py`/`domains.py` — they're
regenerated fresh from live state on every reload and would only go stale.

```python
import hapy
import entities
import devices


class OnMySwitchOn(hapy.Automation):

    def init_condition(self):
        return devices.MySwitch.remote_button_short_press_turn_on

    def action(self):
        entities.MyLight.services.turn_on()


class OnMySwitchDimUp(hapy.Automation):

    def init_condition(self):
        return devices.MySwitch.remote_button_long_press_dim_up

    def exit_condition(self):
        return devices.MySwitch.remote_button_long_release_dim_up

    def action(self):
        entities.MyLight.services.turn_on(brightness_step_pct=10)


class OnMyLightTurnedOn(hapy.Automation):

    def init_condition(self):
        return entities.MyLight.state.changed(old_value='off', new_value='on')

    def action(self):
        entities.MySecondLight.services.turn_off()
```

- `init_condition()` is evaluated on every relevant Home Assistant event; when
  it returns true, `action()` runs. The entities/devices your
  `init_condition()` touches are discovered automatically the moment the
  class is defined (on import/reload) — there's no explicit subscription
  step. Write `or`-chains freely (`a.state.changed() or b.state.changed()`)
  without worrying about one operand's real value at reload time hiding the
  binding for the rest of the chain.
- `exit_condition()` (optional) keeps `action()` running on a
  `step_time`-interval loop until it returns true, or `timeout` seconds pass —
  useful for "while this button is held" patterns.
- `entities.X.state.changed(old_value=None, new_value=None, offset=60)` /
  `.updated(attribute, ..., seconds=5)` — true if the value changed to what
  you expect within the last `offset`/`seconds`.
- `entities.X.services.<service_name>(...)` — calls the matching Home
  Assistant service for that entity's domain, with full IDE-visible keyword
  arguments and docstrings once you've exported stubs locally.
- `devices.X.<action_name>` — a boolean that's momentarily `True` when a ZHA
  device trigger (button press, etc.) fires; requires the `zha` integration
  configured with a device whose quirk exposes `device_automation_triggers`.

## Migrating from the old `hapy` pip package

If you used the previous `pip install hapy-automation` + Docker container
setup: your existing `automations`/`helpers` code should work with this
integration largely unchanged. `import hapy`, `import hapy.automations as
automations`, `import hapy.helpers as hapy_helpers` all keep working. Remove
any checked-in `entities.py`/`devices.py`/`domains.py`/`.registry` from your
repo — they're no longer needed and would just be dead weight (the
integration never reads them; everything is regenerated from live state).

## Known limitations

- One actively-configured automations repo per Home Assistant instance is the
  supported/tested case. Multiple config entries are mechanically possible
  but their generated `entities`/`devices`/`domains` modules aren't currently
  namespaced against each other.
- Reload and live automation execution are currently serialized against each
  other via a single process-wide lock, to guarantee correct entity/device
  bindings. This means two automations that would otherwise run truly
  concurrently (e.g. two held-down dimmer switches in different rooms at the
  same instant) briefly queue behind each other rather than executing in
  parallel — a deliberate correctness-over-concurrency trade-off.
