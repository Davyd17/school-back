from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.group_repository_gateway import GroupRepositoryGateway
from domain.model.entities.group import Group
from infraestructure.driven_adapters.SQLModel_repository.mapper.group_model_mapper import GroupModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.group_model import GroupModel


class GroupRepository(GroupRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = GroupModel

    def get_by_id(self, id: int) -> Optional[Group]:
        pass

    def get_all(self) -> List[Group]:

        groups_db = self.session.exec(select(self.model)).all()

        return[GroupModelMapper.to_domain(group) for group in groups_db]

    def create(self, entity: Group) -> Group:
        pass

    def update(self, id: int, entity: Group) -> Group:
        pass

    def delete(self, id: int):
        pass