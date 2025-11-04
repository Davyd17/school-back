from typing import List

from ...gateway.phone_number_repository_gateway import PhoneNumberRepositoryGateway
from ...model.entities.phone_number import PhoneNumber


class PhoneNumberFindAllUseCase:
    def __init__(self, repository: PhoneNumberRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[PhoneNumber]:
        return self.repository.get_all()