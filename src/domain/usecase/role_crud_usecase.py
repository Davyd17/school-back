from typing import List
from domain.gateway.role_gateway import RoleGateway
from domain.model.entities.role import Role


class RoleCrudUseCase:
    def __init__(self, repository: RoleGateway):
        self.repository = repository

    def create(self, role: Role) -> Role:
        return self.repository.create(role)
    
    def get_by_id(self, id: int) -> Role:
        return self.repository.get_by_id(id)
    
    def get_all(self) -> List[Role]:
        roles_db = self.repository.get_all()
        return roles_db

    def update(self, id: int, role: Role) -> Role:
        return self.repository.update(id, role)

    def delete(self, id: int):
        self.repository.delete(id)