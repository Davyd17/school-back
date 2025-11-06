from domain.model.entities.user.student import Student
from infraestructure.driven_adapters.SQLModel_repository.mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.driven_adapters.SQLModel_repository.mapper.role_model_mapper import RoleModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.student_model import StudentModel

class StudentModelMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentModel:

        return StudentModel(
            student_id = domain.student_id,
            group_id = domain.group.id,
            group = domain.group
        )

    @staticmethod
    def to_domain(model: StudentModel) -> Student:

        return Student(
            student_id=model.student_id,
            group=model.group,
            phone_numbers=[PhoneNumberModelMapper.to_domain(phone)
                           for phone in model.user.phone_numbers],
            role=RoleModelMapper.to_domain(model.user.role),
            **model.user.model_dump(exclude={"phone_numbers",
                                             "role",
                                             "role_id"})
        )