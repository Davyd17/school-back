from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.permission_repository_gateway import PermissionRepositoryGateway
from domain.model.entities.permission import Permission
from ..mapper.permission_model_mapper import PermissionModelMapper
from ..model.permission_model import PermissionModel


class PermissionRepository(PermissionRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = PermissionModel

    def get_by_id(self, id: int) -> Optional[Permission]:
        pass

    def get_all(self) -> List[Permission]:

        permissions_db = self.session.exec(select(PermissionModel)).all()

        return [PermissionModelMapper.to_domain(permission_db) for permission_db in permissions_db]


    def create(self, entity: Permission) -> Permission:
        pass

    def update(self, id: int, entity: Permission) -> Permission:
        pass

    def delete(self, id: int):
        pass