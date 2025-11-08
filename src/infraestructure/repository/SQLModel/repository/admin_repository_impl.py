from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.admin_repository import AdminRepository
from domain.entities.user.admin import Admin
from ..config.connection import get_session
from ..mapper.admin_model_mapper import AdminModelMapper
from ..model.user_model.admin_model import AdminModel
from ..model.user_model.user_model import UserModel


class AdminRepositoryImpl(AdminRepository):
    def __init__(self,  session: Session = get_session):
        self.session = session

    def get_by_id(self, id: int) -> Optional[Admin]:
        pass

    def get_all(self) -> List[Admin]:

        user_admin_db = self.session.exec(select(AdminModel, UserModel).join(UserModel)).all()
        return [AdminModelMapper.to_domain(admin_db, user_db) for admin_db, user_db in user_admin_db]

    def create(self, create: Admin) -> Admin:
        pass

    def update(self, id: int, update: Admin) -> Admin:
        pass

    def delete(self, id: int):
        pass