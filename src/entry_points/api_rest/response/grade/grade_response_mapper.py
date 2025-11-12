from domain.entities.grade import Grade
from .grade_response import GradeResponse


class GradeResponseMapper:

    @staticmethod
    def from_domain(domain: Grade) -> GradeResponse:

        return GradeResponse(
            id=domain.id,
            level=domain.level,
        )

    @staticmethod
    def to_domain(response: GradeResponse) -> Grade:

        return Grade(
            id=response.id,
            level=response.level,
        )