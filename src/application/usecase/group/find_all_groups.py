from typing import List

from application.gateway.repository.model.group_repository import GroupRepository
from domain.entities.group import Group

class FindAllGroups:
    def __init__(self, repository: GroupRepository):
        self.repository = repository

    def execute(self) -> List[Group]:
        return self.repository.get_all()
