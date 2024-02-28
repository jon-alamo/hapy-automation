import json
import logging
import ha_control.models as models


logger = logging.getLogger('EventHandler')


def send(ws, data):
    return ws.send(json.dumps(data))


def subscribe_to_state_changes():
    return {
        "type": "subscribe_events",
        "event_type": "state_changed"
    }


def subscribe_to_zha_events():
    return {
        "type": "subscribe_events",
        "event_type": "zha_event"
    }


def send_auth_message(ha_token):
    return {
        "type": "auth",
        "access_token": ha_token
    }


def handle_state_change(data):
    entity = models.EntityHandler.entities.get(data['entity_id'])
    if entity:
        new_state = data.get('new_state', {})
        state_value = new_state.get('state')
        attributes = new_state.get('attributes', {})
        attributes['state_value'] = state_value
        entity.state.set_state(**attributes)


def handle_zha_event(data):
    device = models.DeviceHandler.devices.get(data['device_id'])
    if device and device.quirk is not None:
        logger.info(f'Handling ZHA event: {data}')
        device.handle_action_data(data)


def unknown_event(data):
    print(f'Unknown Event: {data}')


event_handlers = {
    'state_changed': handle_state_change,
    'zha_event': handle_zha_event
}


def handle_message(message):
    if message['type'] != 'event':
        return
    event = message['event']
    event_handler = event_handlers.get(event['event_type'], unknown_event)
    data = event['data']
    event_handler(data)
