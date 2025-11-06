from fastapi import Depends

from domain.gateway.group_repository_gateway import GroupRepositoryGateway
from domain.usecase.group.group_find_all_usecase import GroupFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.group_repository import GroupRepository


def provide_group_repository(session: session_dep) -> GroupRepositoryGateway:
    return GroupRepository(session)

def provide_group_find_all_usecase(repository: GroupRepositoryGateway
                                   = Depends(provide_group_repository)) -> GroupFindAllUseCase:
    return GroupFindAllUseCase(repository)