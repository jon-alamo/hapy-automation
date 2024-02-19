import os
import json
import websocket
import dotenv

dotenv.load_dotenv()

HA_URL = os.getenv('HA_URL')
HA_URL = HA_URL.replace('https://', '').replace('http://', '')
WS_API_URL = f"ws://{HA_URL}/api/websocket"

api_reference = {
    'auth_message': {
        'type': 'auth',
        'access_token': '{access_token}'
    },
    'state_changes': {
        'type': 'subscribe_events',
        'event_type': 'state_changed'
    },
    'zha_events': {
        'type': 'subscribe_events',
        'event_type': 'zha_event'
    },
    'get_states': {
        'type': 'get_states'
    },
    'get_services': {
        'type': 'get_services'
    },
    'get_domains': {
        'type': 'get_domains'
    },
    'get_areas': {
        'type': 'config/area_registry/list'
    },
    'get_devices': {
        'type': 'config/device_registry/list'
    },
    'get_entities': {
        'type': 'config/entity_registry/list'
    },
}


def format_values(iterable, **kwargs):
    if type(iterable) is dict:
        for k, v in iterable.items():
            if type(v) is str:
                iterable[k] = v.format(**kwargs)
            else:
                format_values(v, **kwargs)
    elif type(iterable) in [list, tuple, set]:
        for i, v in enumerate(iterable):
            if type(v) is str:
                iterable[i] = v.format(**kwargs)
            else:
                format_values(v, **kwargs)
    return iterable


def get_message(message_type, **kwargs):
    message = api_reference[message_type].copy()
    message = format_values(message, **kwargs)
    return message


def send_auth_message(ws):
    auth_message = {
        "type": "auth",
        "access_token": os.getenv('HA_TOKEN')
    }
    return ws.send(json.dumps(auth_message))


socket = websocket.create_connection(WS_API_URL)
send_auth_message(socket)
socket.recv()

global_id = 1


def get_id():
    global global_id
    global_id += 1
    return global_id


def send(data, data_id=None):
    if 'id' not in data and data_id is None:
        data['id'] = get_id()
    elif 'id' not in data:
        data['id'] = data_id
    data_id = data['id']
    socket.send(json.dumps(data))
    for _ in range(50):
        response = json.loads(socket.recv())
        if 'id' in response and response['id'] == data_id:
            return response
    return None


def get_devices():
    return send(get_message('get_devices'))


def get_entities():
    return send(get_message('get_entities'))


