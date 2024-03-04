from importlib.machinery import SourceFileLoader
from datetime import datetime, timezone
import unittest

import ha_control.event_handler as event_handler


entities_path = 'ha_control/tests/fixtures/modules/entities.py'
devices_path = 'ha_control/tests/fixtures/modules/devices.py'
automations_path = 'ha_control/tests/fixtures/modules/automations.py'


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
        event_handler.handle_state_change(data)

        self.assertTrue(entities.LightLivingDownLight01.state.state_value, 'on')
        self.assertTrue(entities.LightLivingDownLight01.state.old.state_value, 'off')
        self.assertFalse(entities.LightLivingDownLight01.state.changed(seconds=0))
        self.assertTrue(entities.LightLivingDownLight01.state.changed())
