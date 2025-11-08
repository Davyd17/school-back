from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.group_repository import GroupRepository
from domain.entities.group import Group
from infraestructure.repository.SQLModel.mapper.group_model_mapper import GroupModelMapper
from infraestructure.repository.SQLModel.model.group_model import GroupModel


class GroupRepositoryImpl(GroupRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Optional[Group]:
        statement = select(GroupModel).where(GroupModel.id == id)
        return GroupModelMapper.to_domain(self.session.exec(statement).first())

    def get_all(self) -> List[Group]:
        groups_db = self.session.exec(select(GroupModel)).all()
        return[GroupModelMapper.to_domain(group) for group in groups_db]

    def create(self, create: Group) -> Group:
        pass

    def update(self, id: int, update: Group) -> Group:
        pass

    def delete(self, id: int):
        pass