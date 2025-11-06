from domain.model.entities.user.student import Student
from infraestructure.entry_points.api_rest.response.phone_number.phone_number_response_mapper import \
    PhoneNumberResponseMapper
from infraestructure.entry_points.api_rest.response.role.role_response_mapper import RoleResponseMapper
from infraestructure.entry_points.api_rest.response.user.student.student_response import StudentResponse


class StudentResponseMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentResponse:

        return StudentResponse(
            student_id=domain.student_id,
            full_name=domain.get_full_name(),
            username=domain.username,
            email=domain.email,
            is_active=domain.is_active,
            phone_numbers=[PhoneNumberResponseMapper.from_domain(phone)
                           for phone in domain.phone_numbers],
            role=RoleResponseMapper.from_domain(domain.role),
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            group_name=domain.group.name
        )

    @staticmethod
    def to_domain(response: StudentResponse) -> Student:

        full_name = response.full_name

        return Student(
            student_id=response.student_id,
            name=Student.get_name_from_full_name(full_name),
            last_name=Student.get_last_name_from_full_name(full_name),
            username=response.username,
            email=response.email,
            is_active=response.is_active,
            phone_numbers=[PhoneNumberResponseMapper.to_domain(phone)
                           for phone in response.phone_numbers],
            role=RoleResponseMapper.to_domain(response.role),
            created_at=response.created_at,
            updated_at=response.updated_at
        )