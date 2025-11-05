from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.user_repository_gateway import UserRepositoryGateway
from domain.model.entities.user.user import User
from infraestructure.driven_adapters.SQLModel_repository.mapper.user_model_mapper import UserModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.user_model import UserModel


class UserRepository(UserRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = UserModel

    def get_by_id(self, id: int) -> Optional[User]:
        pass

    def get_all(self) -> List[User]:
        users_db = self.session.exec(select(self.model)).all()
        return [UserModelMapper.to_domain(user_db) for user_db in users_db]

    def create(self, entity: User) -> User:
        pass

    def update(self, id: int, entity: User) -> User:
        pass

    def delete(self, id: int):
        pass