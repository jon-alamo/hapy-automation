import websocket
import json


with open('.secret') as f:
    config = json.load(f)

ws_url = f"{config['ha_url'].replace('https', 'ws').replace('http', 'ws')}/api/websocket"

auth_message = {
    "type": "auth",
    "access_token": config['ha_token']
}


def subscribe_to_state_changes(ws):
    subscribe_message = {
        "id": 1,
        "type": "subscribe_events",
        "event_type": "*"
    }
    return ws.send(json.dumps(subscribe_message))


def on_state_change(ws, message):
    data = json.loads(message)
    print(data)
    if data['type'] == 'auth_required':
        ws.send(json.dumps(auth_message))
        subscribe_to_state_changes(ws)


if __name__ == '__main__':
    ws = websocket.WebSocketApp(ws_url, on_message=on_state_change)
    ws.run_forever()
