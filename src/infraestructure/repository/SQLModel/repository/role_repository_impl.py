from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.role_repository import RoleRepository
from domain.entities.role import Role
from ..mapper.role_model_mapper import RoleModelMapper
from ..model.role_model import RoleModel

class RoleRepositoryImpl(RoleRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_by_name(self, name:str) -> Optional[Role]:

        statement = select(RoleModel).where(RoleModel.name == name)
        role_model = self.__session.exec(statement).first()
        return RoleModelMapper.to_domain(role_model)

    def get_by_id(self, id: int) -> Optional[Role]:

        role_db: Optional[RoleModel] = self.__session.get(RoleModel, id)
        return RoleModelMapper.to_domain(role_db)

    def get_all(self) -> List[Role]:

        roles_db = self.__session.exec(select(RoleModel)).all()

        return [RoleModelMapper.to_domain(role_db) for role_db in roles_db]

    def create(self, role: Role) -> Role:

        role_model = RoleModelMapper.to_model(role)

        self.__session.add(role_model)
        self.__session.commit()
        self.__session.refresh(role_model)

        return RoleModelMapper.to_domain(role_model)

    def update(self, id: int, role: Role) -> Role:
        pass

    def delete(self, id: int):
        pass





    