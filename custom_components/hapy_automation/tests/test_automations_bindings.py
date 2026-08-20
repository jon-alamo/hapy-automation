"""Regression test ported from
hapy/tests/test_automations/test_automations_bindings.py::test_or_chain_binds_every_entity_even_if_the_first_one_is_true.

init_condition() written as `a.state.changed(...) or b.state.changed(...)`
must bind to *both* a and b, even if a.state.changed() genuinely evaluates
True at the moment bindings are computed — which would otherwise
short-circuit the `or` and silently never bind b. The thread-local
discovery-mode machinery in runtime/models.py (enter_discovery_mode/
exit_discovery_mode, and State.changed()/updated() checking
in_discovery_mode() first) is what prevents that. Do not remove it.
"""
from custom_components.hapy_automation.runtime import helpers, models
from custom_components.hapy_automation.runtime.automations import Automation, AutomationHandler


def test_or_chain_binds_every_entity_even_if_the_first_one_is_true():
    class EntityA(models.Entity):
        entity_id = "sensor.or_chain_test_a"
        state = models.State(actual_entity_id=entity_id, state_value='off')

    class EntityB(models.Entity):
        entity_id = "sensor.or_chain_test_b"
        state = models.State(actual_entity_id=entity_id, state_value='off')

    # Make the first operand genuinely True outside of discovery mode.
    now = helpers.get_now()
    EntityA.state.set_state(state_value='on', last_changed=now, last_updated=now)
    assert EntityA.state.changed(offset=120) is True

    class OnEitherChanged(Automation):
        def init_condition(self):
            return (
                EntityA.state.changed(offset=120)
                or EntityB.state.changed(offset=120)
            )

        def action(self):
            pass

    assert EntityB.id in AutomationHandler.automation_bindings
    assert OnEitherChanged in AutomationHandler.automation_bindings[EntityB.id].values()
    assert EntityA.id in AutomationHandler.automation_bindings
    assert OnEitherChanged in AutomationHandler.automation_bindings[EntityA.id].values()
