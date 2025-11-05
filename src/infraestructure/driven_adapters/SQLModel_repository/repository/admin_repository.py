from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.admin_repository_gateway import AdminRepositoryGateway
from domain.model.entities.user.admin import Admin
from ..mapper.admin_model_mapper import AdminModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.admin_model import AdminModel
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.user_model import UserModel


class AdminRepository(AdminRepositoryGateway):
    def __init__(self,  session: Session):
        self.session = session
        self.model = AdminModel

    def get_by_id(self, id: int) -> Optional[Admin]:
        pass

    def get_all(self) -> List[Admin]:

        user_admin_db = self.session.exec(select(self.model, UserModel).join(UserModel)).all()
        return [AdminModelMapper.to_domain(admin_db, user_db) for admin_db, user_db in user_admin_db]

    def create(self, entity: Admin) -> Admin:
        pass

    def update(self, id: int, entity: Admin) -> Admin:
        pass

    def delete(self, id: int):
        pass