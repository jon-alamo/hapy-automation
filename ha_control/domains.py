import ha_control.helpers as helpers


class BaseDomain:
    domain = None
    entity_id = None

    def call_service(self, domain, service, fields):
        pass


domain_template = """
class {class_name}(BaseDomain):
    domain = "{domain_name}"
"""

service_template = """
    def {method_name}({fields}):
        pass
"""


def generate_field(field_name, field_data):
    if "selector" in field_data:
        field_string = f'{field_name} : str'
        if "required" not in field_data or field_data["required"] is False:
            field_string += " = None"
        return field_string


def generate_fields(fields_data):
    fields = []


def generate_service_code(service_data):
    service = service_data['service']
    service_method_name = helpers.Pythonize.method_name(service)


def generate_domain(domain_data):
    class_code = domain_template.format(domain_name=domain_data['domain'])
    for service in domain_data['services']:
        pass