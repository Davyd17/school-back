from fastapi import Depends

from domain.gateway.role_gateway import RoleGateway
from domain.usecase.role.role_find_all_usecase import RoleFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.role_repository import RoleRepository


def get_role_repository(session: session_dep) -> RoleGateway:
    return RoleRepository(session)

def find_all_usecase(repository: RoleGateway = Depends(get_role_repository)) -> RoleFindAllUseCase:
    return RoleFindAllUseCase(repository)