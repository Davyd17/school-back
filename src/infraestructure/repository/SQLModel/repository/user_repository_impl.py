from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.user_repository import UserRepository
from domain.entities.user.user import User
from infraestructure.repository.SQLModel.mapper.user_model_mapper import UserModelMapper
from infraestructure.repository.SQLModel.model.user_model.user_model import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Optional[User]:
        pass

    def get_all(self) -> List[User]:
        users_db = self.session.exec(select(UserModel)).all()
        return [UserModelMapper.to_domain(user_db) for user_db in users_db]

    def create(self, create: User) -> User:
        pass

    def update(self, id: int, update: User) -> User:
        pass

    def delete(self, id: int):
        pass