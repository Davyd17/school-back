from application.gateway.repository.model.group_repository import GroupRepository


class GroupUseCase:
    def __init__(self, repository: GroupRepository):
        self._repository = repository