from typing import List

from domain.gateway.group_repository_gateway import GroupRepositoryGateway
from domain.model.entities.group import Group


class GroupFindAllUseCase:
    def __init__(self, repository: GroupRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[Group]:
        return self.repository.get_all()
