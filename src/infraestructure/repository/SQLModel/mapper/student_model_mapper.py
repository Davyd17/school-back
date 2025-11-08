from domain.entities.user.student import Student
from infraestructure.repository.SQLModel.mapper.group_model_mapper import GroupModelMapper
from infraestructure.repository.SQLModel.mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.repository.SQLModel.mapper.role_model_mapper import RoleModelMapper
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel


class StudentModelMapper:

    @staticmethod
    def from_domain(domain: Student) -> StudentModel:

        return StudentModel(
            student_id = domain.student_id,
            group_id = domain.group.id,
            group = GroupModelMapper.from_domain(domain.group)
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