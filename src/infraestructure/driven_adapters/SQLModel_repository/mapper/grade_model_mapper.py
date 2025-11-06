from domain.model.entities.grade import Grade
from .group_model_mapper import GroupModelMapper
from ..model.grade_model import GradeModel


class GradeModelMapper:

    @staticmethod
    def from_domain(domain: Grade) -> GradeModel:

        return GradeModel(
            id=domain.id,
            level=domain.level,
            groups=[GroupModelMapper.from_domain(group)
                    for group in domain.groups]
        )


    @staticmethod
    def to_domain(model: GradeModel) -> Grade:

        return Grade(
            id=model.id,
            level=model.level,
            groups=[GroupModelMapper.to_domain(group)
                    for group in model.groups]
        )