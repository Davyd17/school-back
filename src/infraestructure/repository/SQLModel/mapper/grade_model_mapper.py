from domain.entities.grade import Grade
from ..model.grade_model import GradeModel


class GradeModelMapper:

    @staticmethod
    def from_domain(domain: Grade) -> GradeModel:

        return GradeModel(
            id=domain.id,
            level=domain.level,
        )


    @staticmethod
    def to_domain(model: GradeModel) -> Grade:

        return Grade(
            id=model.id,
            level=model.level,
        )