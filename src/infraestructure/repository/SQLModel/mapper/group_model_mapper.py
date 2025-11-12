from domain.entities.group import Group
from infraestructure.repository.SQLModel.mapper.grade_model_mapper import GradeModelMapper
from infraestructure.repository.SQLModel.mapper.teacher_model_mapper import TeacherModelMapper
from infraestructure.repository.SQLModel.model.group_model import GroupModel


class GroupModelMapper:

    @staticmethod
    def from_domain(domain: Group) -> GroupModel:

        return GroupModel(
            id=domain.id,
            name=domain.name,
            grade=domain.grade,
            teacher=domain.teacher
        )

    @staticmethod
    def to_domain(model: GroupModel) -> Group:

        return Group(
            id=model.id,
            name=model.name,
            grade=GradeModelMapper.to_domain(model.grade),
            teacher=TeacherModelMapper.to_domain(model.teacher)
        )