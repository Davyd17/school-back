from domain.entities.user.student import Student
from entry_points.api_rest.request.group.group_request import GroupRequest
from entry_points.api_rest.request.group.group_request_mapper import GroupRequestMapper
from entry_points.api_rest.request.role.request.role_request import RoleRequest
from entry_points.api_rest.request.role.request.role_request_mapper import RoleRequestMapper
from entry_points.api_rest.request.user.student.student_create import StudentCreate


class StudentCreateMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentCreate:

        return StudentCreate(
            name=domain.name,
            last_name=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            role_request=RoleRequestMapper.from_domain(domain.role),
            group_request= GroupRequestMapper.from_domain(domain.group)
        )

    @staticmethod
    def to_domain(create: StudentCreate) -> Student:

        return Student(
            name=create.name,
            last_name=create.last_name,
            username=create.username,
            email=create.email,
            password=create.password,
            role=RoleRequestMapper.to_domain(create.role_request),
            group=GroupRequestMapper.to_domain(create.group_request),
        )
