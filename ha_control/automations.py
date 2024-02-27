import time
import asyncio
import threading


class AutomationHandler(type):
    automations = {}
    _base_class = None

    def __new__(cls, classname, bases, class_dict):
        new_class = type.__new__(cls, classname, bases, class_dict)
        if cls._base_class is None and classname == 'Automation':
            cls._base_class = new_class
        else:
            cls.automations[classname] = new_class
        return new_class

    @classmethod
    def run_automations(cls):
        for automation_class in cls.automations.values():
            automation = automation_class()
            if automation.init_condition():
                threading.Thread(target=automation.run).start()


class Automation(metaclass=AutomationHandler):
    step_time = 0.1
    time_out = 10

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
            time.sleep(self.step_time)
            self.action()
            if self.is_time_out(t0):
                break
