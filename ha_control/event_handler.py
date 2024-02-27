import json


def subscribe_to_events(ws):
    subscribe_message = {
        "id": 1,
        "type": "subscribe_events",
        "event_type": "*"
    }
    return ws.send(json.dumps(subscribe_message))


def send(ws, data):
    return ws.send(json.dumps(data))


def send_auth_message(ws, ha_token):
    auth_message = {
        "type": "auth",
        "access_token": ha_token
    }
    return send(ws, auth_message)


def get_handler(ha_token):

    def on_message(ws, message):
        data = json.loads(message)
        if data['type'] == 'auth_required':
            send_auth_message(ws, ha_token)

    return on_message