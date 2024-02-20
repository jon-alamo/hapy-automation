import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('HA_TOKEN', '')
HA_URL = os.getenv('HA_URL', '')
base_url = f'{HA_URL}/api'

auth_headers = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}


endpoints = {
    # GET
    'config': 'config',
    'events': 'events',
    'services': 'services',
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


def api_request(url, method='get', data=None):
    response = requests.get(url, json=data, headers=auth_headers)
    if 200 <= response.status_code < 300:
        return response.json()
    return response.json()


def get_state(entity_id):
    url = f'{base_url}/{endpoints["entity_state"].format(entity_id=entity_id)}'
    return api_request(url)
