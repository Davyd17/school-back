from typing import Optional, List

from sqlmodel import Session, select

from application.gateway.repository.model.phone_number_repository import PhoneNumberRepository
from domain.entities.phone_number import PhoneNumber
from ..mapper.phone_number_model_mapper import PhoneNumberModelMapper


class PhoneNumberRepositoryImpl(PhoneNumberRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Optional[PhoneNumber]:
        pass

    def get_all(self) -> List[PhoneNumber]:

        phone_numbers_db = self.session.exec(select(PhoneNumber)).all()
        return [PhoneNumberModelMapper.to_domain(phone_number_db) for phone_number_db in phone_numbers_db]

    def create(self, create: PhoneNumber) -> PhoneNumber:
        pass

    def update(self, id: int, update: PhoneNumber) -> PhoneNumber:
        pass

    def delete(self, id: int):
        pass