import websocket
import json
import logging
import importlib
import types
import time
import ssl
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import hapy.events as events
import hapy.automations as automations
import hapy.models as models
import hapy.helpers as helpers


logger = logging.getLogger('Application')


init_message = """
::::::::: hapy automations running :::::::::::
Connected to Home Assistant instance at: 
{ha_url}

- {aut:<5}  automations
- {dev:<5}  devices
- {ent:<5}  entities
::::::::::::::::::::::::::::::::::::::::::::::
"""

reload_message = """
::::::::: hapy automations reloaded ::::::::::
Reloaded automations at:
{dt}

- {aut:<5} automations
::::::::::::::::::::::::::::::::::::::::::::::
"""


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        super(FileChangeHandler, self).__init__()
        self.callback = callback

    def on_any_event(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        if filename.endswith(".py"):
            logger.info(f"File {filename} has been changed, reloading ...")
            self.callback()


class Application(websocket.WebSocketApp):

    def __init__(self, automations_module, ha_api_url, ha_ws_url, ha_token, registry):
        self.ha_api_url = ha_api_url
        self.ha_ws_url = ha_ws_url
        self.ha_token = ha_token
        self.registry = registry
        self._id = 0
        self.automations_module = automations_module
        self.observer = Observer()
        self.observer.schedule(
            FileChangeHandler(self.reload), path='.', recursive=True
        )
        self.observer.start()
        self._reload_timer = time.time()
        self._reload_wait = 5
        super().__init__(
            self.ha_ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
        )

    def get_id(self):
        self._id += 1
        return self._id

    def send(self, data: dict, opcode=websocket.ABNF.OPCODE_TEXT):
        if 'event' in data['type']:
            data['id'] = self.get_id()
        return self.sock.send(json.dumps(data))

    def on_open(self, ws):
        self.send(events.send_auth_message(self.ha_token))
        self.send(events.subscribe_to_state_changes())
        self.send(events.subscribe_to_zha_events())

    def on_message(self, ws, message):
        events.handle_message(json.loads(message))
        automations.AutomationHandler.handle_exit_conditions()
        automations.AutomationHandler.run_automations()
        models.DeviceHandler.reset_fired_actions()

    def on_error(self, ws, error):
        logger.error(error)

    def recursively_import_modules(self, module, imported=None):
        if 'hapy' not in module.__name__:
            importlib.reload(module)
        imported = imported or []
        for name, mod in vars(self.automations_module).items():
            if name in imported:
                continue
            elif isinstance(mod, types.ModuleType):
                imported.append(name)
                self.recursively_import_modules(mod, imported)

    def reload(self):
        if time.time() - self._reload_timer < self._reload_wait:
            return
        automations.AutomationHandler.reset_automations()
        self.recursively_import_modules(self.automations_module)
        current_automations = len(automations.AutomationHandler.automations)
        models.EntityHandler.read_states()
        print(reload_message.format(
            aut=current_automations,
            dt=helpers.get_now().strftime('%Y-%m-%d %H:%M:%S')
        ))
        self._reload_timer = time.time()

    def run_forever(self, *args, **kwargs):
        print(init_message.format(
            ha_url=self.ha_api_url.split('/api')[0],
            aut=len(automations.AutomationHandler.automations),
            dev=len(models.DeviceHandler.devices),
            ent=len(models.EntityHandler.entities)
        ))
        models.EntityHandler.read_states()
        if 'wss' in self.ha_ws_url:
            kwargs['sslopt'] = {"cert_reqs": ssl.CERT_NONE}
        super().run_forever(*args, **kwargs)
