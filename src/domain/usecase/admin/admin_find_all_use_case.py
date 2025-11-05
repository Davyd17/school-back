from typing import List

from ...gateway.admin_repository_gateway import AdminRepositoryGateway
from ...model.entities.user.admin import Admin


class AdminFindAllUseCase:
    def __init__(self, repository: AdminRepositoryGateway):
        self.admin_repository_gateway = repository

    def execute(self) -> List[Admin]:
        return self.admin_repository_gateway.get_all()