from typing import List

from domain.gateway.user_repository_gateway import UserRepositoryGateway
from domain.model.entities.user.user import User


class UserFindAllUseCase:
    def __init__(self, repository: UserRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[User]:
        return self.repository.get_all()