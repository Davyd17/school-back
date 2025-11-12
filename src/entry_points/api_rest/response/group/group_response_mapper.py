from domain.entities.group import Group
from entry_points.api_rest.response.grade.grade_response_mapper import GradeResponseMapper
from entry_points.api_rest.response.group.group_response import GroupResponse
from entry_points.api_rest.response.user.teacher.teacher_response_mapper import TeacherResponseMapper


class GroupResponseMapper:

    @staticmethod
    def from_domain(domain: Group) -> GroupResponse:

        return GroupResponse(
            id = domain.id,
            name = domain.name,
            grade_response= GradeResponseMapper.from_domain(domain.grade),
            teacher_response= TeacherResponseMapper.from_domain(domain.teacher)
        )

    @staticmethod
    def to_domain(response: GroupResponse) -> Group:

        return Group(
            id = response.id,
            name = response.name,
            grade = GradeResponseMapper.to_domain(response.grade_response),
            teacher= TeacherResponseMapper.to_domain(response.teacher_response)
        )