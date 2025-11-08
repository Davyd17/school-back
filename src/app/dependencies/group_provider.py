from fastapi import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.group_repository import GroupRepository
from application.usecase.group.find_group_by_id import FindGroupById
from application.usecase.group.find_all_groups import FindAllGroups
from infraestructure.repository.SQLModel.repository.group_repository_impl import GroupRepositoryImpl


def __provide_repository(session: session_dep) -> GroupRepository:
    return GroupRepositoryImpl(session)

def provide_find_all_groups(repository: GroupRepository
                                   = Depends(__provide_repository)) -> FindAllGroups:
    return FindAllGroups(repository)

def provide_find_group_by_id(repository: GroupRepository
                                   = Depends(__provide_repository)) -> FindGroupById:
    return FindGroupById(repository)