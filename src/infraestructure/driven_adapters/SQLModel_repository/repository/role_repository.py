from typing import List, Optional

from sqlmodel import Session, select
from domain.gateway.generic_crud_gateway import GenericCrudGateway
from domain.model.entities.role import Role
from ..mapper.role_model_mapper import RoleModelMapper
from ..model.role_model import RoleModel

class RoleRepository(GenericCrudGateway[Role]):
    def __init__(self, session: Session):
        self.session = session
        self.model = RoleModel


    def get_by_id(self, id: int) -> Optional[Role]:

        role_db: Optional[RoleModel] = self.session.get(self.model, id)

        if not role_db:
            return None

        return RoleModelMapper.to_domain(role_db)

    def get_all(self) -> List[Role]:

        roles_db = self.session.exec(select(RoleModel)).all()
        print("here")
        print(roles_db)

        return [RoleModelMapper.to_domain(role_db) for role_db in roles_db]

    def create(self, role: Role) -> Role:

        role_model = RoleModelMapper.to_model(role)

        self.session.add(role_model)
        self.session.commit()
        self.session.refresh(role_model)

        return RoleModelMapper.to_domain(role_model)

    def update(self, id: int, role: Role) -> Role:
        pass

    def delete(self, id: int):
        pass





    