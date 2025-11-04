from typing import List

from domain.gateway.permission_repository_gateway import PermissionRepositoryGateway
from domain.model.entities.permission import Permission

class PermissionFindAllUseCase:
    def __init__(self, repository: PermissionRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[Permission]:
        return self.repository.get_all()

