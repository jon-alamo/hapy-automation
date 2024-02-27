from ha_control import Automation

import entities
import devices


class MyAutomation(Automation):

    def init_condition(self):
        return True

    def exit_condition(self):
        return True

    def action(self):
        print('Hello from MyAutomation')
