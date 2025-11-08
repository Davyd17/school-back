from fastapi import Depends

from app.config.database_provider import session_dep
from application.gateway.repository.model.user_repository import UserRepository
from application.usecase.user.find_all_users import FindAllUsers
from infraestructure.repository.SQLModel.repository.user_repository_impl import UserRepositoryImpl


def __provide_repository(session: session_dep) -> UserRepository:
    return UserRepositoryImpl(session)

def provide_find_all_users(repository: UserRepository = Depends(__provide_repository)) -> FindAllUsers:
    return FindAllUsers(repository)