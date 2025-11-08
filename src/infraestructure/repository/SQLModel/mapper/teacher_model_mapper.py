from domain.entities.user.teacher import Teacher
from .phone_number_model_mapper import PhoneNumberModelMapper
from .role_model_mapper import RoleModelMapper
from .user_model_mapper import UserModelMapper
from ..model.user_model.teacher_model import TeacherModel

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
    def from_domain(domain: Teacher) -> TeacherModel:

        return TeacherModel(
            teacher_id=domain.teacher_id,
            salary=domain.salary,
            user_id=domain.user_id,
            user=UserModelMapper.from_domain(domain)
        )
