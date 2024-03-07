import json
import logging
import websocket
import requests

logger = logging.getLogger('homeassistant')


ws_ref = {
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


api_ref = {
    # GET
    'entities': 'entities/',
    'config': 'config',
    'events': 'events',
    'services': 'services',
    'devices': 'devices/{device_id}',
    'history': 'history/period/{timestamp}',
    'logbook': 'logbook/{timestamp}',
    'states': 'states',
    'entity_state': 'states/{entity_id}',
    'error_log': 'error_log',
    'camera_proxy': 'camera_proxy/{entity_id}',
    'calendars': 'calendars',
    'calendar': 'calendars/{calendar_id}',
    # POST
    'state': 'states/{entity_id}',
    'event': 'events/{event_type}',
    'service': 'services/{domain}/{service}',
    'template': 'template',
}


auth_headers = {
    "Authorization": "Bearer {token}",
    "content-type": "application/json",
}


class HAInstance:

    def __init__(self, ha_api_url, ha_ws_url, ha_token):
        self._global_id = 0
        self._ha_api_url = ha_api_url
        self._ha_ws_url = ha_ws_url
        self._ha_token = ha_token
        self._auth_headers = auth_headers
        self._auth_headers['Authorization'] = self._auth_headers['Authorization'].format(token=ha_token)
        self._socket = None
        self._event_socket = None

    def _get_id(self):
        self._global_id += 1
        return self._global_id

    def _authenticate(self, ws):
        auth_message = {
            "type": "auth",
            "access_token": self._ha_token
        }
        ws.send(json.dumps(auth_message))
        ws.recv()

    def _ws_connect(self):
        self._socket = websocket.create_connection(self._ha_ws_url)
        self._authenticate(self._socket)

    def _ws_send(self, data, data_id=None):
        if 'id' not in data and data_id is None:
            data['id'] = self._get_id()
        elif 'id' not in data:
            data['id'] = data_id
        data_id = data['id']
        if not self._socket:
            self._ws_connect()
        self._socket.send(json.dumps(data))
        for _ in range(50):
            response = json.loads(self._socket.recv())
            if 'id' in response and response['id'] == data_id:
                return response
        return None

    def _format_values(self, iterable, **kwargs):
        if type(iterable) is dict:
            for k, v in iterable.items():
                if type(v) is str:
                    iterable[k] = v.format(**kwargs)
                else:
                    self._format_values(v, **kwargs)
        elif type(iterable) in [list, tuple, set]:
            for i, v in enumerate(iterable):
                if type(v) is str:
                    iterable[i] = v.format(**kwargs)
                else:
                    self._format_values(v, **kwargs)
        return iterable

    def _api_request(self, url, method='get', data=None):
        method = getattr(requests, method)
        response = method(url, json=data, headers=self._auth_headers)
        if 200 <= response.status_code < 300:
            return response.json()
        logger.error(f'API Error {response.status_code}: {response.text}')
        return None

    def get_message(self, message_type, **kwargs):
        message = ws_ref[message_type].copy()
        message = self._format_values(message, **kwargs)
        return message

    def get_devices(self):
        return self._ws_send(self.get_message('get_devices'))

    def get_entities(self):
        return self._ws_send(self.get_message('get_entities'))

    def get_state(self, entity_id):
        url = f'{self._ha_api_url}/{api_ref["entity_state"].format(entity_id=entity_id)}'
        return self._api_request(url)

    def get_states(self):
        url = f'{self._ha_api_url}/{api_ref["states"]}'
        return self._api_request(url)

    def get_services(self):
        url = f'{self._ha_api_url}/{api_ref["services"]}'
        return self._api_request(url)

    def call_service(self, domain, service, data):
        url = f'{self._ha_api_url}/{api_ref["service"].format(domain=domain, service=service)}'
        return self._api_request(url, method='post', data=data)

    def get_config(self):
        url = f'{self._ha_api_url}/{api_ref["config"]}'
        return self._api_request(url)

    def get_events(self):
        url = f'{self._ha_api_url}/{api_ref["events"]}'
        return self._api_request(url)

    def get_logbook(self, timestamp):
        url = f'{self._ha_api_url}/{api_ref["logbook"].format(timestamp=timestamp)}'
        return self._api_request(url)

    def get_device(self, device_id):
        url = f'{self._ha_api_url}/{api_ref["devices"].format(device_id=device_id)}'
        return self._api_request(url)
