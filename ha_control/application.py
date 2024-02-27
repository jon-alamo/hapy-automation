import websocket
import json
import importlib

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import ha_control.event_handler as event_handler
import ha_control.automations as automations


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


class Application:
    def __init__(self, automations_module, ha_url, ha_token, registry):
        self.ha_url = ha_url
        self.ha_token = ha_token
        self.ws_url = get_ws_url(ha_url)
        self.registry = registry
        self.automations_module = automations_module
        self.observer = Observer()
        self.observer.schedule(
            FileChangeHandler(self.reload), path='.', recursive=True
        )
        self.observer.start()

    def reload(self):
        print('Reloading automations ...')
        self.automations_module = importlib.reload(self.automations_module)
        total_automations = len(automations.AutomationHandler.automations)
        print(f'Registered {total_automations} automations.')
        self.run()

    def run(self):
        try:
            ws = websocket.WebSocketApp(
                self.ws_url,
                on_message=event_handler.get_handler(self.ha_token)
            )
            ws.run_forever()
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

