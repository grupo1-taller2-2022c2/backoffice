from app.models.metric_models import FederatedIdRegistrationCounter, MailPasswordRegistrationCounter


class RegistrationCounterFactory:
    def create_counter_for_method(method):
        if method == "mailpassword":
            return MailPasswordRegistrationCounter
        if method == "federatedidentity":
            return FederatedIdRegistrationCounter
        else:
            raise ValueError('Registration method does not exist')
