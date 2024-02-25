import ha_control

ha_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxZmUxYjRhMTRhYTY0NzEwYmJlNmRjNjU3ODRiMzI4MCIsImlhdCI6MTcwODY3NTI1NSwiZXhwIjoyMDI0MDM1MjU1fQ.qDnU-2hSI9svnv8XpkUNBVeACeuRuFTTsp8Kukbj6IA"
ha_url="http://192.168.1.20:8123"

ha_control.generate_modules('test_hac', ha_url, ha_token)


entities.LightOfficeMainLightLight2.services.turn_off(transition=10)


{
    ('remote_button_short_press', 'turn_on'): {'command': 'on', 'cluster_id': 6, 'endpoint_id': 1},
    ('remote_button_long_press', 'dim_up'): {'command': 'move_with_on_off', 'cluster_id': 8, 'endpoint_id': 1, 'params': {'move_mode': 0}},
    ('remote_button_long_release', 'dim_up'): {'command': 'stop_with_on_off', 'cluster_id': 8, 'endpoint_id': 1},
    ('remote_button_short_press', 'turn_off'): {'command': 'off', 'cluster_id': 6, 'endpoint_id': 1},
    ('remote_button_long_press', 'dim_down'): {'command': 'move', 'cluster_id': 8, 'endpoint_id': 1, 'params': {'move_mode': 1}},
    ('remote_button_long_release', 'dim_down'): {'command': 'stop', 'cluster_id': 8, 'endpoint_id': 1}
}