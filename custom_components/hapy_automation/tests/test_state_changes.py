"""Regression test ported from
hapy/tests/test_entities/test_state_changes.py::test_state_changed_survives_clock_skew_ahead_of_local_clock.

Pure logic, no Home Assistant fixture needed: constructs a runtime.models.State
directly and confirms `.changed()` still returns True when the source
timestamps last_changed a few milliseconds *ahead* of this process's own
clock (e.g. Home Assistant running on another host with a slightly-ahead
clock) — the abs()/total_seconds() fix in runtime/models.py, not
`.seconds`, is what makes this pass. Do not revert that fix.
"""
from datetime import datetime, timedelta, timezone

from custom_components.hapy_automation.runtime import models


def test_state_changed_survives_clock_skew_ahead_of_local_clock():
    state = models.State(actual_entity_id='light.test', state_value='off')

    future_ts = datetime.now(timezone.utc) + timedelta(milliseconds=50)
    state.set_state(state_value='on', last_changed=future_ts, last_updated=future_ts)

    assert state.changed() is True


def test_state_changed_respects_offset_window():
    state = models.State(actual_entity_id='light.test', state_value='off')
    old_ts = datetime.now(timezone.utc) - timedelta(seconds=120)
    state.set_state(state_value='on', last_changed=old_ts, last_updated=old_ts)

    assert state.changed(offset=60) is False
    assert state.changed(offset=300) is True


def test_changed_always_false_during_discovery_mode():
    state = models.State(actual_entity_id='light.test', state_value='off')
    now = datetime.now(timezone.utc)
    state.set_state(state_value='on', last_changed=now, last_updated=now)
    assert state.changed() is True

    models.enter_discovery_mode()
    try:
        assert state.changed() is False
    finally:
        models.exit_discovery_mode()
