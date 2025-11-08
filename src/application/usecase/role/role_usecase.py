from application.gateway.repository.model.role_repository import RoleRepository


class RoleUseCase:
    def __init__(self, repository: RoleRepository):
        self._repository = repository