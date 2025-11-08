from application.gateway.repository.model.group_repository import GroupRepository
from domain.entities.group import Group
from application.usecase.group.group_usecase import GroupUseCase

class FindGroupById(GroupUseCase):
    def __init__(self, repository: GroupRepository):
        super().__init__(repository)

    def execute(self, id:int) -> Group:
        group = self._repository.get_by_id(id)
        return self.__check_group_exists(group)


    def __check_group_exists(self, group: Group) -> Group:
        if not group:
            raise Exception(f"Group with id: {group.id} not found")
        return group
