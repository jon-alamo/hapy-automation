import websocket
import json
import logging
import importlib
import types

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import ha_control.event_handler as event_handler
import ha_control.automations as automations
import ha_control.models as models


logger = logging.getLogger('Application')


init_message = """
::::::::::::::::::: Running :::::::::::::::::::::::::
App connected to Home Assistant instance at: {ha_url}

- Registered automations:   {automations}
- Registered devices:       {devices}
- Registered entities:      {entities}

:::::::::::::::::::::::::::::::::::::::::::::::::::::

"""

reload_message = """
::::::::::::::::::: Reloading :::::::::::::::::::::::

- Registered automations:   {automations}

:::::::::::::::::::::::::::::::::::::::::::::::::::::

"""


def get_ws_url(ha_url):
    return f"{ha_url.replace('https', 'ws').replace('http', 'ws')}/api/websocket"


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        super(FileChangeHandler, self).__init__()
        self.callback = callback

    def on_any_event(self, event):
        if event.is_directory:
            return
        self.callback()


class Application(websocket.WebSocketApp):

    def __init__(self, automations_module, ha_url, ha_token, registry):
        self.ha_url = ha_url
        self.ha_token = ha_token
        self.ws_url = get_ws_url(ha_url)
        self.registry = registry
        self._id = 0
        self.automations_module = automations_module
        self.observer = Observer()
        self.observer.schedule(
            FileChangeHandler(self.reload), path='.', recursive=True
        )
        self.observer.start()
        super().__init__(
            self.ws_url,
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
        self.send(event_handler.send_auth_message(self.ha_token))
        self.send(event_handler.subscribe_to_state_changes())
        self.send(event_handler.subscribe_to_zha_events())

    def on_message(self, ws, message):
        event_handler.handle_message(json.loads(message))
        automations.AutomationHandler.handle_exit_conditions()
        automations.AutomationHandler.run_automations()
        models.DeviceHandler.reset_fired_actions()

    def on_error(self, ws, error):
        logger.error(error)

    def recursively_import_modules(self, module):
        importlib.reload(module)
        for name, mod in vars(self.automations_module).items():
            if isinstance(mod, types.ModuleType):
                self.recursively_import_modules(mod)

    def reload(self):
        importlib.reload(self.automations_module)
        self.recursively_import_modules(self.automations_module)
        current_automations = len(automations.AutomationHandler.automations)
        print(reload_message.format(automations=current_automations))

    def run_forever(self, *args, **kwargs):
        print(init_message.format(
            ha_url=self.ha_url,
            automations=len(automations.AutomationHandler.automations),
            devices=len(models.DeviceHandler.devices),
            entities=len(models.EntityHandler.entities)
        ))
        models.EntityHandler.read_states()
        super().run_forever(*args, **kwargs)
