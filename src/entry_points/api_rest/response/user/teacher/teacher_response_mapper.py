from domain.entities.user.teacher import Teacher
from entry_points.api_rest.response.phone_number.phone_number_response_mapper import \
    PhoneNumberResponseMapper
from entry_points.api_rest.response.role.role_response_mapper import RoleResponseMapper
from entry_points.api_rest.response.user.teacher.teacher_response import TeacherResponse


class TeacherResponseMapper:

    @staticmethod
    def from_domain(domain: Teacher) -> TeacherResponse:

        return TeacherResponse(
            teacher_id=domain.teacher_id,
            full_name=domain.get_full_name(),
            username=domain.username,
            email=domain.email,
            is_active=domain.is_active,
            phone_numbers=[PhoneNumberResponseMapper.from_domain(phone)
                           for phone in domain.phone_numbers],
            role=RoleResponseMapper.from_domain(domain.role),
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            salary=domain.salary
        )

    @staticmethod
    def to_domain(response: TeacherResponse) -> Teacher:

        return Teacher(
            name=Teacher.get_name_from_full_name(response.get_full_name()),
            last_name=Teacher.get_last_name_from_full_name(response.full_name),
            username=response.username,
            email=response.email,
            password=response.password,
            is_active=response.is_active,
            created_at=response.created_at,
            updated_at=response.updated_at,
            phone_numbers=[PhoneNumberResponseMapper.to_domain(phone)
                           for phone in response.phone_numbers],
            role=RoleResponseMapper.to_domain(response.role)
        )