from domain.entities.user.teacher import Teacher
from entry_points.api_rest.request.role.request.role_request_mapper import RoleRequestMapper
from entry_points.api_rest.request.user.teacher.create.teacher_create_request import TeacherCreateRequest


class TeacherCreateMapper:

    @staticmethod
    def from_domain(domain: Teacher) -> TeacherCreateRequest:

        return TeacherCreateRequest(
            name = domain.name,
            last_name= domain.last_name,
            username= domain.username,
            email= domain.email,
            password=domain.password,
            role_request=RoleRequestMapper.from_domain(domain.role),
            salary=domain.salary
        )

    @staticmethod
    def to_domain(request:TeacherCreateRequest) -> Teacher:

        return Teacher(
            name=request.name,
            last_name=request.last_name,
            username=request.username,
            email=request.email,
            password=request.password,
            role=RoleRequestMapper.to_domain(request.role_request),
            salary=request.salary
        )