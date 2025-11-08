from domain.entities.user.student import Student
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
            role_id=domain.role_id,
            group_id= domain.group_id
        )

    @staticmethod
    def to_domain(create: StudentCreate) -> Student:

        return Student(
            name=create.name,
            last_name=create.last_name,
            username=create.username,
            email=create.email,
            password=create.password,
            role_id=create.role_id,
            group_id=create.group.id,
        )
