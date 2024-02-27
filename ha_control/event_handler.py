import json


def send(ws, data):
    return ws.send(json.dumps(data))


def subscribe_to_events():
    return {
        "type": "subscribe_events",
        "event_type": "*"
    }


def send_auth_message(ha_token):
    return {
        "type": "auth",
        "access_token": ha_token
    }


def get_handler(ha_token):

    def on_message(ws, message):
        data = json.loads(message)
        if data['type'] == 'auth_required':
            send_auth_message(ws, ha_token)
        print(data)

    return on_message
