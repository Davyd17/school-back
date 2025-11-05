from typing import Tuple

from domain.model.entities.user.teacher import Teacher
from .phone_number_model_mapper import PhoneNumberModelMapper
from .role_model_mapper import RoleModelMapper
from .user_model_mapper import UserModelMapper
from ..model.user_model.teacher_model import TeacherModel
from ..model.user_model.user_model import UserModel


class TeacherModelMapper:

    @staticmethod
    def to_domain(teacher_model: TeacherModel, user_model: UserModel) -> Teacher:

        return Teacher(
            teacher_id=teacher_model.teacher_id,
            salary=teacher_model.salary,
            phone_numbers=[PhoneNumberModelMapper.to_domain(phone)
                           for phone in user_model.phone_numbers],
            role=RoleModelMapper.to_domain(user_model.role),
            **user_model.model_dump(exclude={"phone_numbers", "role", "role_id"})
        )

    @staticmethod
    def from_domain(domain: Teacher) -> Tuple[UserModel, TeacherModel]:

        user_model = UserModelMapper.from_domain(domain)

        teacher_model = TeacherModel(
            teacher_id=domain.teacher_id,
            salary=domain.salary,
        )

        return user_model, teacher_model
