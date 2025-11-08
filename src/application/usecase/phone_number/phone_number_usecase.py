from application.gateway.repository.model.phone_number_repository import PhoneNumberRepository


class PhoneNumberUsecase:
    def __init__(self, repository: PhoneNumberRepository):
        self._repository = repository