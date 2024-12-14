import time
import logging
import threading
import hapy.models as models
import hapy.helpers as helpers


logger = helpers.get_logger('hapy.automations')


register_modules = ['entities', 'devices']

base_classes = [models.Entity, models.Device]


class AutomationHandler(type):
    to_check_automations = []
    to_run_automations = {}
    running_automations = {}
    automation_bindings = {}
    automations = {}
    modules = {}
    _base_class = None

    @classmethod
    def make_bindings(cls, new_class):
        try:
            automation_obj = new_class().init_condition()
        except Exception as e:
            logger.warning(
                f'{new_class.__name__} not bound to any entity or device due to '
                f'init_condition error: {e}.'
            )
            return
        for entity_id in models.EntityHandler.track_access:
            if entity_id not in cls.automation_bindings:
                cls.automation_bindings[entity_id] = {}
            cls.automation_bindings[entity_id][new_class.get_id()] = new_class
            logger.info(
                f'[AUTOMATIONS] - make_bindings: {new_class.__name__} bound to {entity_id}.'
            )
        for device_id in models.DeviceHandler.track_access:
            if device_id not in cls.automation_bindings:
                cls.automation_bindings[device_id] = {}
            cls.automation_bindings[device_id][new_class.get_id()] = new_class
            logger.info(
                f'[AUTOMATIONS] - make_bindings: {new_class.__name__} bound to {device_id}.'
            )
        models.EntityHandler.reset_access()
        models.DeviceHandler.reset_access()

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if cls._base_class is None and classname == 'Automation':
            cls._base_class = new_class
        else:
            cls.automations[new_class.get_id()] = new_class
        cls.make_bindings(new_class)
        return new_class

    @classmethod
    def reset_automations(cls):
        cls.automation_bindings = {}
        cls.automations = {}

    @classmethod
    def handle_exit_conditions(cls):
        for name in list(cls.running_automations.keys()):
            automation = cls.running_automations[name]
            if automation.exit_condition():
                logger.info(f'[AUTOMATIONS] - handle_exit_conditions: {name} leaving.')
                automation.force_exit = True
                cls.running_automations.pop(name)

    @classmethod
    def register_change(cls, item):
        if item.id in cls.automation_bindings:
            automations = [
                automation() for automation in cls.automation_bindings[item.id].values()
            ]
            cls.to_check_automations.extend(automations)
            logging.info(
                f'[AUTOMATIONS] - register_change: {item.id} triggering {len(automations)} checks.'
            )

    @classmethod
    def check_automations(cls):
        cls.to_run_automations = {
            automation.__class__.__name__: automation
            for automation in cls.to_check_automations
            if automation.init_condition()
        }
        cls.to_check_automations = []
        logger.info(f'[AUTOMATIONS] - check_automations: {len(cls.to_run_automations)} automations to the queue.')

    @classmethod
    def run_automations(cls):
        for name, automation in cls.to_run_automations.items():
            logger.info(
                f'[AUTOMATIONS] - run_automations: executing {name} automations.'
            )
            cls.running_automations[name] = automation
            thread = threading.Thread(target=automation.run)
            thread.start()
        cls.to_run_automations = []


class Automation(metaclass=AutomationHandler):
    step_time = 0.5
    timeout = 10

    def __init__(self):
        self.force_exit = False

    def action(self):
        raise NotImplementedError('action method must be implemented')

    def init_condition(self):
        return False

    def exit_condition(self):
        return True

    def is_time_out(self, t0):
        return time.time() - t0 > self.timeout

    def run(self):
        self.action()
        t0 = time.time()
        loops = 0
        while not self.exit_condition():
            loops += 1
            self.action()
            time.sleep(self.step_time)
            if self.is_time_out(t0):
                logger.info(
                    f'[AUTOMATIONS] - {self.__class__.__name__} timed out.'
                )
                return
            if self.force_exit:
                logger.info(
                    f'[AUTOMATIONS] - {self.__class__.__name__} was forced to exit.'
                )
                return
        times = 'once' if loops == 0 else f'{loops + 1} times'
        logger.info(
            f'[AUTOMATIONS] - {self.__class__.__name__} action triggered {times}.'
        )

    @classmethod
    def get_id(cls):
        return '.'.join([cls.__module__, cls.__name__])
