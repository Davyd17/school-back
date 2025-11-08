from typing import List

from application.gateway.repository.model.permission_repository import PermissionRepository
from domain.entities.permission import Permission

class FindAllPermissions:
    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def execute(self) -> List[Permission]:
        return self.repository.get_all()

