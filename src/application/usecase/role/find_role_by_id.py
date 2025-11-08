from application.gateway.repository.model.role_repository import RoleRepository
from domain.entities.role import Role
from application.usecase.role.role_usecase import RoleUseCase


class FindRoleById(RoleUseCase):
    def __init__(self, repository: RoleRepository):
        super().__init__(repository)

    def execute(self, id: int):
        role = self._repository.get_by_id(id)
        return self.__check_role_exists(role)

    def __check_role_exists(self, role: Role) -> Role:
        if not role:
            raise Exception(f"Role with id {role.id} not found")
        return role
