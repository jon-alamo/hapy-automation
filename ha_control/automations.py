import time
import ha_control.models as models
import threading


class AutomationHandler(type):
    automations = {}
    running_automations = {}
    _base_class = None

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if cls._base_class is None and classname == 'Automation':
            cls._base_class = new_class
        else:
            cls.automations[classname] = new_class
        return new_class

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
            for automation in cls.automations.values()
            if automation().init_condition()
        }
        cls.running_automations.update(to_run)
        for automation in to_run.values():
            thread = threading.Thread(target=automation.run)
            thread.start()


class Automation(metaclass=AutomationHandler):
    step_time = 0.1
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
        self.action()
        t0 = time.time()
        while not self.exit_condition():
            self.action()
            time.sleep(self.step_time)
            if self.is_time_out(t0):
                return
            if self.force_exit:
                return
