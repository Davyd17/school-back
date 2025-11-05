from typing import Tuple

from domain.model.entities.user.admin import Admin

from .phone_number_model_mapper import PhoneNumberModelMapper
from .role_model_mapper import RoleModelMapper

from .user_model_mapper import UserModelMapper
from ..model.user_model.admin_model import AdminModel
from ..model.user_model.user_model import UserModel


class AdminModelMapper:

    @staticmethod
    def to_domain(admin_model: AdminModel, user_model: UserModel) -> Admin:

        return Admin(
            admin_id = admin_model.admin_id,
            phone_numbers = [PhoneNumberModelMapper.to_domain(phone)
                             for phone in user_model.phone_numbers],
            role = RoleModelMapper.to_domain(user_model.role),
            **user_model.model_dump(exclude={"phone_numbers",
                                             "role",
                                             "role_id",
                                             "user_id"})
        )

    @staticmethod
    def from_domain(domain: Admin) -> Tuple[UserModel, AdminModel]:

        user_model = UserModelMapper.from_domain(domain)

        admin_model = AdminModel(
            admin_id = domain.admin_id,
            user_id = user_model.user_id,
            user = user_model
        )

        return user_model, admin_model
