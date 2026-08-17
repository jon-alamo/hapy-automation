from importlib.machinery import SourceFileLoader
from datetime import datetime, timezone, timedelta
import unittest

import hapy.events as events


entities_path = 'hapy/tests/fixtures/modules/entities.py'
devices_path = 'hapy/tests/fixtures/modules/devices.py'
automations_path = 'hapy/tests/fixtures/modules/automations.py'


class TestStateChanges(unittest.TestCase):

    def test_state_changed_event_takes_effect(self):
        entities = SourceFileLoader("entities", entities_path).load_module()
        cur_iso_time = datetime.now(timezone.utc).isoformat()
        data = {
            'entity_id': 'light.living_down_light_01',
            'new_state': {
                'state': 'on',
                "last_changed": cur_iso_time,
                "last_updated": cur_iso_time,
                'attributes': {'brightness': 100}
            },
            'old_state': {
                'state': 'off',
                "last_changed": "2024-03-04T13:40:48.021760+00:00",
                "last_updated": "2024-03-04T13:40:48.021760+00:00",
                'attributes': {'brightness': 0}
            }
        }
        events.handle_state_change(data)

        self.assertTrue(entities.LightLivingDownLight01.state.state_value, 'on')
        self.assertTrue(entities.LightLivingDownLight01.state.old.state_value, 'off')
        self.assertFalse(entities.LightLivingDownLight01.state.changed(offset=0))
        self.assertTrue(entities.LightLivingDownLight01.state.changed())

    def test_state_changed_survives_clock_skew_ahead_of_local_clock(self):
        """Regression test: if the source (e.g. Home Assistant on another
        host) timestamps last_changed a few milliseconds ahead of this
        process's own clock, (now - last_changed) is negative. Using
        timedelta.seconds on a negative delta silently normalizes it to
        ~86400 (Python represents negative timedeltas as a negative day
        count plus a positive seconds remainder), which used to make
        changed() incorrectly return False for a change that just
        happened."""
        entities = SourceFileLoader(
            "entities_clock_skew", entities_path
        ).load_module()
        future_iso_time = (
            datetime.now(timezone.utc) + timedelta(milliseconds=50)
        ).isoformat()
        data = {
            'entity_id': 'light.living_down_light_01',
            'new_state': {
                'state': 'on',
                "last_changed": future_iso_time,
                "last_updated": future_iso_time,
                'attributes': {'brightness': 100}
            },
            'old_state': {
                'state': 'off',
                "last_changed": "2024-03-04T13:40:48.021760+00:00",
                "last_updated": "2024-03-04T13:40:48.021760+00:00",
                'attributes': {'brightness': 0}
            }
        }
        events.handle_state_change(data)

        self.assertTrue(entities.LightLivingDownLight01.state.changed())
