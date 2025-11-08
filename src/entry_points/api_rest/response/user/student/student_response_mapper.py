from domain.entities.user.student import Student
from entry_points.api_rest.response.phone_number.phone_number_response_mapper import \
    PhoneNumberResponseMapper
from entry_points.api_rest.response.user.student.student_response import StudentResponse


class StudentResponseMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentResponse:

        return StudentResponse(
            student_id=domain.student_id,
            name=domain.name,
            last_name=domain.last_name,
            username=domain.username,
            email=domain.email,
            is_active=domain.is_active,
            phone_numbers=[PhoneNumberResponseMapper.from_domain(phone)
                           for phone in domain.phone_numbers],
            role=domain.role,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            group=domain.group
        )

    @staticmethod
    def to_domain(response: StudentResponse) -> Student:

        return Student(
            student_id=response.student_id,
            group=response.group,
            name=response.name,
            last_name=response.last_name,
            username=response.username,
            email=response.email,
            is_active=response.is_active,
            phone_numbers=[PhoneNumberResponseMapper.to_domain(phone)
                           for phone in response.phone_numbers],
            role=response.role,
            created_at=response.created_at,
            updated_at=response.updated_at
        )