from typing import List

from application.gateway.repository.model.admin_repository import AdminRepository
from domain.entities.user.admin import Admin


class FindAllAdmins:
    def __init__(self, repository: AdminRepository):
        self.repository = repository

    def execute(self) -> List[Admin]:
        return self.repository.get_all()