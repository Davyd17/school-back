from application.gateway.repository.model.phone_number_repository import PhoneNumberRepository
from domain.entities.phone_number import PhoneNumber
from application.usecase.phone_number.phone_number_usecase import PhoneNumberUsecase


class CreatePhone(PhoneNumberUsecase):
    def __init__(self, repository: PhoneNumberRepository):
        super().__init__(repository)

    def execute(self) -> PhoneNumber:
        pass

