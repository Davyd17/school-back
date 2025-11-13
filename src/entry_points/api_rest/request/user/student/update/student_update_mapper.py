from tokenize import group

from domain.entities.user.student import Student
from entry_points.api_rest.request.group.group_request_mapper import GroupRequestMapper
from entry_points.api_rest.request.user.student.update.student_update_request import StudentUpdateRequest


class StudentUpdateMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentUpdateRequest:

        return StudentUpdateRequest(
            name=domain.name,
            last_name=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            is_active=domain.is_active,
            updated_at= domain.updated_at,
            group_request= GroupRequestMapper.from_domain(domain.group)
        )

    @staticmethod
    def to_domain(request: StudentUpdateRequest) -> Student:

        return Student(
            group=GroupRequestMapper.to_domain(request.group_request),
            **request.model_dump(exclude_unset=True, exclude={"group_request"})
        )