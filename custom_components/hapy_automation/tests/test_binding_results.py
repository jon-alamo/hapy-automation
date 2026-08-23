"""AutomationHandler.binding_results is the ground truth an agent (or a
human) can use to tell whether an automation actually attached to anything
real — reload succeeding proves the code imports, not that a wrong
entities.X/devices.X reference didn't just silently produce zero bindings.
Found for real: an agent wrote two automations referencing entities/devices
that don't exist; both "reloaded ok" and did nothing at all.
"""
from custom_components.hapy_automation.runtime import models
from custom_components.hapy_automation.runtime.automations import Automation, AutomationHandler


def test_binding_results_records_real_bindings():
    AutomationHandler.reset_automations()

    class SomeEntity(models.Entity):
        entity_id = "sensor.some_entity"
        state = models.State(actual_entity_id=entity_id, state_value="on")

    class RealAutomation(Automation):
        def init_condition(self):
            return SomeEntity.state.changed()

        def action(self):
            pass

    result = AutomationHandler.binding_results[RealAutomation.get_id()]
    assert result == {"bound_to": ["sensor.some_entity"], "error": None}


def test_binding_results_records_the_error_for_a_bad_reference():
    AutomationHandler.reset_automations()

    class BrokenAutomation(Automation):
        def init_condition(self):
            return this_name_does_not_exist.whatever  # noqa: F821

        def action(self):
            pass

    result = AutomationHandler.binding_results[BrokenAutomation.get_id()]
    assert result["bound_to"] == []
    assert "this_name_does_not_exist" in result["error"]


def test_reset_automations_clears_binding_results_too():
    AutomationHandler.reset_automations()

    class SomeEntity2(models.Entity):
        entity_id = "sensor.some_entity_2"
        state = models.State(actual_entity_id=entity_id, state_value="on")

    class SomeAutomation(Automation):
        def init_condition(self):
            return SomeEntity2.state.changed()

        def action(self):
            pass

    assert AutomationHandler.binding_results

    AutomationHandler.reset_automations()
    assert AutomationHandler.binding_results == {}
