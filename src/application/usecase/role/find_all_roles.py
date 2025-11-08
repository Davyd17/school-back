from typing import List

from application.gateway.repository.model.role_repository import RoleRepository
from domain.entities.role import Role


class FindAllRoles:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def execute(self) -> List[Role]:
        roles_db = self.repository.get_all()
        return roles_db