from fastapi import Depends

from domain.gateway.user_repository_gateway import UserRepositoryGateway
from domain.usecase.user.user_find_all_usecase import UserFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.user_repository import UserRepository


def get_user_repository(session: session_dep) -> UserRepositoryGateway:
    return UserRepository(session)

def get_user_find_all_usecase(repository: UserRepositoryGateway = Depends(get_user_repository)) -> UserFindAllUseCase:
    return UserFindAllUseCase(repository)