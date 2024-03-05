import time
import threading
import sys


register_modules = ['entities', 'devices']


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
            cls.to_check_automations.extend(cls.automation_bindings[item.id])

    @classmethod
    def make_bindings(cls, new_class):
        automation_module = sys.modules[new_class.__module__]
        for name in new_class.init_condition.__code__.co_names:
            if name in register_modules and hasattr(automation_module, name):
                cls.modules[name] = getattr(automation_module, name)
                continue
            for module_name, module_object in cls.modules.items():
                if hasattr(module_object, name):
                    module_class = getattr(module_object, name)
                    if module_class not in cls.automation_bindings:
                        cls.automation_bindings[module_class.id] = []
                    cls.automation_bindings[module_class.id].append(new_class)
                    break

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
                automation.force_exit = True
                cls.running_automations.pop(name)

    @classmethod
    def run_automations(cls):
        to_run = {
            automation.__name__: automation()
            for automation in cls.to_check_automations
        }
        cls.running_automations.update(to_run)
        cls.to_check_automations = []
        for automation in to_run.values():
            thread = threading.Thread(target=automation.run)
            thread.start()


class Automation(metaclass=AutomationHandler):
    step_time = 0.5
    time_out = 10

    def __init__(self):
        self.force_exit = False

    def action(self):
        raise NotImplementedError('action method must be implemented')

    def init_condition(self):
        return False

    def exit_condition(self):
        return True

    def is_time_out(self, t0):
        return time.time() - t0 > self.time_out

    def run(self):
        if not self.init_condition():
            return
        self.action()
        t0 = time.time()
        while not self.exit_condition():
            self.action()
            time.sleep(self.step_time)
            if self.is_time_out(t0):
                return
            if self.force_exit:
                return
