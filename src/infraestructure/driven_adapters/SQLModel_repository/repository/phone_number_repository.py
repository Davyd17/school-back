from typing import Optional, List

from sqlmodel import Session, select

from domain.gateway.phone_number_repository_gateway import PhoneNumberRepositoryGateway
from domain.model.entities.phone_number import PhoneNumber
from ..mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.phone_number_model import PhoneNumberModel


class PhoneNumberRepository(PhoneNumberRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = PhoneNumberModel

    def get_by_id(self, id: int) -> Optional[PhoneNumber]:
        pass

    def get_all(self) -> List[PhoneNumber]:

        phone_numbers_db = self.session.exec(select(self.model)).all()
        return [PhoneNumberModelMapper.to_domain(phone_number_db) for phone_number_db in phone_numbers_db]

    def create(self, entity: PhoneNumber) -> PhoneNumber:
        pass

    def update(self, id: int, entity: PhoneNumber) -> PhoneNumber:
        pass

    def delete(self, id: int):
        pass