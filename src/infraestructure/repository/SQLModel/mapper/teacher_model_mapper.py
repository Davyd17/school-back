from typing import Tuple

from domain.entities.user.teacher import Teacher
from .phone_number_model_mapper import PhoneNumberModelMapper
from .role_model_mapper import RoleModelMapper
from ..model.user_model.teacher_model import TeacherModel
from ..model.user_model.user_model import UserModel


class TeacherModelMapper:

    @staticmethod
    def to_domain(model: TeacherModel) -> Teacher:

        return Teacher(
            teacher_id=model.teacher_id,
            salary=model.salary,
            phone_numbers=[PhoneNumberModelMapper.to_domain(phone)
                           for phone in model.user.phone_numbers],
            role=RoleModelMapper.to_domain(model.user.role),
            **model.user.model_dump(exclude={"phone_numbers", "role_id"})
        )

    @staticmethod
    def from_domain(domain: Teacher) -> Tuple[TeacherModel, UserModel]:

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

        teacher_model = TeacherModel(
            teacher_id=domain.teacher_id,
            salary=domain.salary,
            user_id=domain.user_id,
        )

        return teacher_model, user_model
