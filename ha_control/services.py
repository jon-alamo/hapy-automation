import ha_control.ha_restapi as ha_restapi


def service_call(domain_name):
    def wrap(fcn):
        def wrapper(self, **kwargs):
            entity_id = self.entity_id
            service_name = fcn.__name__
            kwargs['entity_id'] = entity_id
            return ha_restapi.call_service(
                domain=domain_name, service=service_name, data=kwargs
            )

        return wrapper
    return wrap