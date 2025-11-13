from typing import Tuple, Optional

from domain.entities.user.student import Student
from infraestructure.repository.SQLModel.mapper.group_model_mapper import GroupModelMapper
from infraestructure.repository.SQLModel.mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.repository.SQLModel.mapper.role_model_mapper import RoleModelMapper
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel
from infraestructure.repository.SQLModel.model.user_model.user_model import UserModel


class StudentModelMapper:

    @staticmethod
    def from_domain(domain: Student) -> Tuple[StudentModel, UserModel]:

        user_model = UserModel(
            user_id=domain.user_id,
            name=domain.name,
            last_name=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            is_active=domain.is_active,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            role_id=domain.role.id
        )

        student_model = StudentModel(
            student_id = domain.student_id,
            user_id = domain.user_id,
            group_id = domain.group.id
        )

        return student_model, user_model

    @staticmethod
    def to_domain(model: StudentModel) -> Student:

        return Student(
            student_id=model.student_id,
            group=GroupModelMapper.to_domain(model.group),
            role=RoleModelMapper.to_domain(model.user.role),
            phone_numbers=[PhoneNumberModelMapper.to_domain(phone)
                           for phone in model.user.phone_numbers],
            **model.user.model_dump(exclude={"phone_numbers",
                                             "role",
                                             "role_id"})
        )