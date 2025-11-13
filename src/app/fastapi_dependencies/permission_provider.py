from fastapi.params import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.permission_repository import PermissionRepository
from application.usecase.permission.find_all_permissions import FindAllPermissions
from infraestructure.repository.SQLModel.repository.permission_repository_impl import PermissionRepositoryImpl


def __provide_repository(session: session_dep) -> PermissionRepository:
    return PermissionRepositoryImpl(session)

def provide_find_all_permissions(repository: PermissionRepository = Depends(__provide_repository)) -> FindAllPermissions:
    return FindAllPermissions(repository)
