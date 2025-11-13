from fastapi.params import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.admin_repository import AdminRepository
from application.usecase.admin.find_all_admins import FindAllAdmins
from infraestructure.repository.SQLModel.repository.admin_repository_impl import AdminRepositoryImpl


def __provide_repository(session: session_dep) -> AdminRepository:
    return AdminRepositoryImpl(session)

def provide_find_all_admins(repository: AdminRepository
                               = Depends(__provide_repository)) -> FindAllAdmins:
    return FindAllAdmins(repository)