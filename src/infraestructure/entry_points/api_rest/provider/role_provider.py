from fastapi import Depends

from domain.gateway.role_repository_gateway import RoleRepositoryGateway
from domain.usecase.role.role_find_all_usecase import RoleFindAllUseCase

from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.role_repository import RoleRepository


def get_role_repository(session: session_dep) -> RoleRepositoryGateway:
    return RoleRepository(session)

def get_role_find_all_usecase(repository: RoleRepositoryGateway = Depends(get_role_repository)) -> RoleFindAllUseCase:
    return RoleFindAllUseCase(repository)