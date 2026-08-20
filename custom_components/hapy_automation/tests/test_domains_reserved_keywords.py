"""Found for real on a friend's Home Assistant instance: the `blueprint`
domain has a service literally called `import`, a reserved Python keyword.
`def import(self, ...):` is a SyntaxError, which broke generation of the
*entire* domains.py module (not just that one service) for anyone with
that integration loaded. Covers both halves of the fix: the generated
Python method name must be safe, and calling it must still hit the real
Home Assistant service name, not the Python-safe one.
"""
import ast

from custom_components.hapy_automation.runtime import models
from custom_components.hapy_automation.runtime.generators import domains as domains_gen

REGISTER = {
    'domains': {
        'blueprint': {
            'import': {
                'description': 'Import a blueprint',
                'fields': {'url': {'description': 'URL', 'selector': {'text': {}}}},
            },
            'delete': {'description': 'Delete a blueprint', 'fields': {}},
        }
    }
}


def test_generated_module_is_valid_python():
    source = domains_gen.generate_domain_module(REGISTER)
    ast.parse(source)  # raises SyntaxError if this regresses
    assert 'def import(' not in source
    assert 'def import_(' in source
    assert "_hapy_service_names = {'import_': 'import'}" in source


def test_calling_the_generated_method_hits_the_real_service_name():
    class FakeInstance:
        def __init__(self):
            self.calls = []

        def call_service(self, domain, service, data):
            self.calls.append((domain, service, data))
            return None

    namespace = {'models': models}
    exec(domains_gen.generate_domain_module(REGISTER), namespace)
    blueprint_cls = namespace['Blueprint']

    instance = FakeInstance()
    entity = blueprint_cls(entity_id='blueprint.thing', state=None, instance=instance)
    entity.import_(url='http://example.com/blueprint.yaml')

    assert instance.calls == [
        ('blueprint', 'import', {'url': 'http://example.com/blueprint.yaml', 'entity_id': 'blueprint.thing'})
    ]


def test_service_without_a_keyword_clash_is_unaffected():
    source = domains_gen.generate_domain_module(REGISTER)
    assert 'def delete(' in source
    # Only the actual keyword clash needs an override entry.
    assert "'delete': 'delete'" not in source


def test_docstring_generation_is_safe_against_hostile_description_text():
    """Real HA service/field descriptions are arbitrary text from every
    installed integration — embedding it raw into a hand-rolled
    `\"\"\" ... \"\"\"` block breaks on any description containing a
    triple-quote itself. generate_docstring must stay valid Python
    regardless of content."""
    register = {
        'domains': {
            'evil': {
                'do_thing': {
                    'description': 'Breaks it """ maybe? or a backslash \\ or newline\n or emoji 🎉',
                    'fields': {
                        'x': {'description': 'field """ desc', 'selector': {'text': {}}, 'example': 'a"b'},
                    },
                },
            }
        }
    }
    source = domains_gen.generate_domain_module(register)
    ast.parse(source)  # raises SyntaxError if this regresses
