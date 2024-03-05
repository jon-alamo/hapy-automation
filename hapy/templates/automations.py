import logging
import hapy

import entities
import devices


logger = logging.getLogger('automations')


class MyAutomation(hapy.Automation):

    def init_condition(self) -> bool:
        """ Define init condition for the automation here. It must be based on
        entities' states or device trigger actions:

            return devices.MySwitch.remote_button_short_press_turn_on
            return entities.MyLight.state.state_value == 'on'

        By the moment, automations are only triggered by devices or entities
        changes that affect to the entities or devices used in the current
        method when corresponding changes are published by homeassistant as
        websocket events.
        """
        return True

    def exit_condition(self) -> bool:
        """ Don't override this method if the automation triggers one-time
        action. In case the action needs to be executed in loop, define the
        exit condition here. This is not intended for long-running automations,
        but for short continuous actions such as dim-ups and downs. There's a
        default timeout of 10 seconds for any automation, but in case needed,
        it can be overwritten by defining the class attribute `timeout`
        in seconds. """
        return True

    def action(self):
        """ Define the action for the automation here. This is the method that
        will be executed when the init condition is met. In case the
        exit_condition method its overridden and met, the action will be
        executed in loop in default time steps of 0.5 seconds with a default
        timeout of 10 seconds. Time step can be set by overriding the class
        attribute `step_time` in seconds. Timeout can be set by overriding the
        class attribute `timeout` in seconds.
        """
        print('Hello from MyAutomation')
