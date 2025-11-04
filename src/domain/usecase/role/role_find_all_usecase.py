from typing import List

from domain.gateway.role_repository_gateway import RoleRepositoryGateway
from domain.model.entities.role import Role


class RoleFindAllUseCase:
    def __init__(self, repository: RoleRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[Role]:
        roles_db = self.repository.get_all()
        return roles_db