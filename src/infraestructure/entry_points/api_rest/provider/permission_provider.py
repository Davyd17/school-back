from fastapi.params import Depends

from domain.gateway.permission_repository_gateway import PermissionRepositoryGateway
from domain.usecase.permission.permission_find_all_usecase import PermissionFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.permission_repository import PermissionRepository
from infraestructure.driven_adapters.SQLModel_repository.repository.role_repository import RoleRepository


def get_permission_repository(session: session_dep) -> PermissionRepositoryGateway:
    return PermissionRepository(session)

def get_permission_find_all_usecase(repository: PermissionRepository = Depends(get_permission_repository)) -> PermissionFindAllUseCase:
    return PermissionFindAllUseCase(repository)
