from typing import List

from application.gateway.repository.model.phone_number_repository import PhoneNumberRepository
from domain.entities.phone_number import PhoneNumber


class FindALlPhoneNumbers:
    def __init__(self, repository: PhoneNumberRepository):
        self.repository = repository

    def execute(self) -> List[PhoneNumber]:
        return self.repository.get_all()