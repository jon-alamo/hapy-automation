import time
import logging
import threading
import sys
import types
import hapy.models as models

logger = logging.getLogger('hapy.automations')

register_modules = ['entities', 'devices']

base_classes = [models.Entity, models.Device]


class AutomationHandler(type):
    to_check_automations = []
    running_automations = {}
    automation_bindings = {}
    automations = {}
    modules = {}
    _base_class = None

    @classmethod
    def register_change(cls, item):
        if item.id in cls.automation_bindings:
            automation = cls.automation_bindings[item.id]
            cls.to_check_automations.extend(automation)
            logging.info(f'register_change: {automation.name}')

    @classmethod
    def is_found_object(cls, obj):
        for base_class in base_classes:
            try:
                if issubclass(obj, base_class):
                    return True
            except TypeError:
                pass
        return False

    @classmethod
    def find_trigger_items(cls, function, contexts: list):
        for name in function.__code__.co_names:
            for context in list(contexts):
                if hasattr(context, name):
                    obj = getattr(context, name)
                    if type(obj) is types.FunctionType:
                        yield from cls.find_trigger_items(obj, contexts)
                    elif type(obj) is types.ModuleType or type(obj) == type:
                        contexts.append(obj)
                    elif cls.is_found_object(obj):
                        yield obj
                        break

    @classmethod
    def make_bindings(cls, new_class):
        contexts = [sys.modules[new_class.__module__]]
        for obj in cls.find_trigger_items(new_class.init_condition, contexts):
            if obj.id not in cls.automation_bindings:
                cls.automation_bindings[obj.id] = []
            cls.automation_bindings[obj.id].append(new_class)
            logger.info(
                f'make_bindings: {new_class.__name__} bound to {obj.id}.'
            )

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if cls._base_class is None and classname == 'Automation':
            cls._base_class = new_class
        else:
            cls.automations[classname] = new_class
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
                logger.info(f'handle_exit_conditions: {name} leaving.')
                automation.force_exit = True
                cls.running_automations.pop(name)

    @classmethod
    def run_automations(cls):
        to_run = {
            automation.__name__: automation()
            for automation in cls.to_check_automations
        }
        logger.info(f'run_automations: {len(to_run)} automations to the queue.')
        cls.running_automations.update(to_run)
        cls.to_check_automations = []
        for automation in to_run.values():
            thread = threading.Thread(target=automation.run)
            thread.start()


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
        if not self.init_condition():
            logger.info(f'{self.__class__.__name__}.run: did not meet init '
                f'condition. Exiting.'
            )
            return
        logger.info(
            f'{self.__class__.__name__}.run: met init condition. '
            f'Running action.'
        )
        self.action()
        t0 = time.time()
        loops = 0
        while not self.exit_condition():
            loops += 1
            self.action()
            time.sleep(self.step_time)
            if self.is_time_out(t0):
                logger.info(
                    f'{self.__class__.__name__}.run: timed out. Leaving.'
                )
                return
            if self.force_exit:
                logger.info(
                    f'{self.__class__.__name__}.run was forced to exit.'
                    f' Leaving.'
                )
                return

        logger.info(
            f'{self.__class__.__name__}.run: met exit condition after '
            f'{loops} loops. Leaving.'
        )
