import logging

from hapy import Automation

logger = logging.getLogger()

try:
    import entities
    import devices
except ImportError:
    logger.warning('entities.py or devices.py modules not generated?')


class MyAutomation(Automation):

    def init_condition(self):
        return True

    def exit_condition(self):
        return True

    def action(self):
        print('Hello from MyAutomation')
