from domain.entities.group import Group
from infraestructure.repository.SQLModel.model.group_model import GroupModel


class GroupModelMapper:

    @staticmethod
    def from_domain(domain: Group) -> GroupModel:

        return GroupModel(
            id=domain.id,
            name=domain.name
        )

    @staticmethod
    def to_domain(model: GroupModel) -> Group:

        return Group(
            id=model.id,
            name=model.name
        )