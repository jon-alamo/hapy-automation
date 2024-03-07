import json
import logging
import hapy.models as models
import hapy.automations as automations


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


def get_differences(old, new):
    old_data = {'state_value': old.get('state'), **old.get('attributes', {})}
    new_data = {'state_value': new.get('state'), **new.get('attributes', {})}
    return ', '.join([
        f'{k} changed ({old_data[k]} -> {new_data[k]})' for k in old_data
        if old_data[k] != new_data[k]
    ])


def handle_state_change(data):
    entity = models.EntityHandler.entities.get(data['entity_id'])
    if entity:
        automations.AutomationHandler.register_change(entity)
        entity.state.set_from_state_event(data)
        changes = get_differences(data.get('old_state', {}), data.get('new_state', {}))
        logger.info(f'handle_state_change: {entity.entity_id}: {changes}')


def handle_zha_event(data):
    device = models.DeviceHandler.devices.get(data['device_id'])
    if device and device.quirk is not None:
        logger.info(f'handle_zha_event: {data}')
        automations.AutomationHandler.register_change(device)
        device.handle_action_data(data)


def unknown_event(data):
    logger.info(f'unknown_event: {data}')


event_handlers = {
    'state_changed': handle_state_change,
    'zha_event': handle_zha_event
}


def handle_message(message):
    logger.info(f'handle_message: {message}')
    if message['type'] != 'event':
        return
    event = message['event']
    event_handler = event_handlers.get(event['event_type'], unknown_event)
    data = event['data']
    event_handler(data)
