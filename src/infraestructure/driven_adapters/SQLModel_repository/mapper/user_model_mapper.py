from typing import List

from domain.model.entities.user.user import User
from infraestructure.driven_adapters.SQLModel_repository.model.user_model import UserModel

#TODO: Apply builder pattern for this large entity arguments
class UserModelMapper:

    @staticmethod
    def from_domain(domain: User) -> UserModel:
        return UserModel(
            id=domain.id,
            name=domain.name,
            lastname=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            is_active=domain.is_active,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            #phone_numbers=domain.phone_numbers,
            role_id=domain.role.id,
            role=domain.role
        )

    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            name=model.name,
            last_name=model.last_name,
            username=model.username,
            email=model.email,
            password=model.password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            #phone_numbers=model.phone_numbers,
            phone_numbers=[],
            role=model.role
        )