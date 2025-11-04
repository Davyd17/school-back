from fastapi import Depends

from domain.gateway.generic_crud_gateway import GenericCrudGateway
from domain.model.entities.role import Role
from domain.usecase.role.role_find_all_usecase import RoleFindAllUseCase

from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.role_repository import RoleRepository


def get_role_repository(session: session_dep) -> GenericCrudGateway:
    return RoleRepository(session)

def find_all_usecase(repository: GenericCrudGateway[Role] = Depends(get_role_repository)) -> RoleFindAllUseCase:
    return RoleFindAllUseCase(repository)