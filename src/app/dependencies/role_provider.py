from fastapi import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.role_repository import RoleRepository
from application.usecase.role.find_role_by_id import FindRoleById
from application.usecase.role.find_all_roles import FindAllRoles
from infraestructure.repository.SQLModel.repository.role_repository_impl import RoleRepositoryImpl


def __provide_repository(session: session_dep) -> RoleRepository:
    return RoleRepositoryImpl(session)

def provide_find_all_roles(repository: RoleRepository
                              = Depends(__provide_repository)) -> FindAllRoles:
    return FindAllRoles(repository)

def provide_find_role_by_id(repository: RoleRepository
                              = Depends(__provide_repository)) -> FindRoleById:
    return FindRoleById(repository)