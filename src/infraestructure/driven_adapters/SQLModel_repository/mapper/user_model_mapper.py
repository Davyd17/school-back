from domain.model.entities.user.user import User
from infraestructure.driven_adapters.SQLModel_repository.mapper.phone_number_model_mapper import PhoneNumberModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.user_model import UserModel

#TODO: Apply builder pattern for these large entity arguments
class UserModelMapper:

    @staticmethod
    def from_domain(domain: User) -> UserModel:
        return UserModel(
            user_id=domain.user_id,
            name=domain.name,
            lastname=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            is_active=domain.is_active,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            phone_numbers=[PhoneNumberModelMapper.from_domain(phone_number)
                           for phone_number
                           in domain.phone_numbers] if domain.phone_numbers else [],
            role_id=domain.role.id,
            role=domain.role
        )

    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            user_id=model.user_id,
            name=model.name,
            last_name=model.last_name,
            username=model.username,
            email=model.email,
            password=model.password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            phone_numbers=[PhoneNumberModelMapper.to_domain(phone_number)
                           for phone_number
                           in model.phone_numbers] if model.phone_numbers else [],
            role=model.role
        )