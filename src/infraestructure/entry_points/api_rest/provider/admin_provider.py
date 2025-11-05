from fastapi.params import Depends

from domain.gateway.admin_repository_gateway import AdminRepositoryGateway
from domain.usecase.admin.admin_find_all_use_case import AdminFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.admin_repository import AdminRepository


def get_admin_repository(session: session_dep) -> AdminRepositoryGateway:
    return AdminRepository(session)

def get_admin_find_all_usecase(repository: AdminRepositoryGateway
                               = Depends(get_admin_repository)) -> AdminFindAllUseCase:
    return AdminFindAllUseCase(repository)