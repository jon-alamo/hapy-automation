import asyncio


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
    async def run_automations(cls):
        automations = [automation() for automation in cls.automations.values()]
        tasks = [
            automation for automation in automations if automation.init_condition()
        ]
        await asyncio.gather(*tasks)


class Automation(metaclass=AutomationHandler):

    def action(self):
        raise NotImplementedError('action method must be implemented')

    async def run(self):
        await asyncio.to_thread(self.action)
