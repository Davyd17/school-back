from typing import List

from application.gateway.repository.model.user_repository import UserRepository
from domain.entities.user.user import User


class FindAllUsers:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> List[User]:
        return self.repository.get_all()