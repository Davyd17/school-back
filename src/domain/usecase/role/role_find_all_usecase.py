from typing import List

from domain.gateway.generic_crud_gateway import GenericCrudGateway
from domain.model.entities.role import Role


class RoleFindAllUseCase:
    def __init__(self, repository: GenericCrudGateway[Role]):
        self.repository = repository

    def execute(self) -> List[Role]:
        roles_db = self.repository.get_all()
        return roles_db