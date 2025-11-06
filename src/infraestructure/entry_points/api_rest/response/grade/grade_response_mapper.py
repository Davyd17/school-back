from http.client import responses

from domain.model.entities.grade import Grade
from .grade_response import GradeResponse
from ..group.group_response_mapper import GroupResponseMapper


class GradeResponseMapper:

    @staticmethod
    def from_domain(domain: Grade) -> GradeResponse:

        return GradeResponse(
            id=domain.id,
            level=domain.level,
            groups=[GroupResponseMapper.from_domain(group)
                    for group in domain.groups]
        )

    @staticmethod
    def to_domain(response: GradeResponse) -> Grade:

        return Grade(
            id=response.id,
            level=response.level,
            groups=[GroupResponseMapper.to_domain(group)
                    for group in response.groups]
        )