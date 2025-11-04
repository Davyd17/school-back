from domain.model.entities.phone_number import PhoneNumber
from domain.model.entities.role import Role
from domain.model.entities.user.user import User
from .user_response import UserResponse


class UserResponseMapper:

    @staticmethod
    def from_domain(domain: User) -> UserResponse:
        return UserResponse(
            id = domain.id,
            full_name = domain.get_full_name(),
            username = domain.username,
            email = domain.email,
            is_active = domain.is_active,
            phone_numbers = [str(phone) for phone in domain.phone_numbers],
            role = domain.role.name,
            created_at = domain.created_at,
            updated_at = domain.updated_at,
        )

    @staticmethod
    def to_domain(response: UserResponse) -> User:
        return User(
            id = response.id,
            name= response.full_name.split(" ")[0],
            last_name= response.full_name.split(" ")[1],
            username = response.username,
            email = response.email,
            is_active = response.is_active,
            phone_numbers = [PhoneNumber(phone=phone) for phone in response.phone_numbers],
            role = Role(name=response.role),
            created_at = response.created_at,
            updated_at = response.updated_at,
        )