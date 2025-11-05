from typing import Tuple

from domain.model.entities.user.admin import Admin
from infraestructure.driven_adapters.SQLModel_repository.mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.driven_adapters.SQLModel_repository.mapper.user_model_mapper import UserModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.admin_model import AdminModel
from infraestructure.driven_adapters.SQLModel_repository.model.user_model import UserModel


class AdminModelMapper:

    @staticmethod
    def to_domain(admin_model: AdminModel, user_model: UserModel) -> Admin:

        return Admin(
            admin_id = admin_model.admin_id,
            name = user_model.name,
            last_name = user_model.last_name,
            username = user_model.username,
            email = user_model.email,
            password = user_model.password,
            is_active = user_model.is_active,
            created_at = user_model.created_at,
            updated_at = user_model.updated_at,
            phone_numbers = [PhoneNumberModelMapper.to_domain(phone)
                             for phone in user_model.phone_numbers],
            role = user_model.role
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
