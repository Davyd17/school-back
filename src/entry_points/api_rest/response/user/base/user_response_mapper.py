from domain.entities.user.user import User
from .user_response import UserResponse
from entry_points.api_rest.response.phone_number.phone_number_response_mapper import PhoneNumberResponseMapper
from ...role.role_response_mapper import RoleResponseMapper


class UserResponseMapper:

    @staticmethod
    def from_domain(domain: User) -> UserResponse:
        return UserResponse(
            __user_id = domain.user_id,
            full_name = domain.get_full_name(),
            username = domain.username,
            email = domain.email,
            is_active = domain.is_active,
            phone_numbers = [PhoneNumberResponseMapper.from_domain(phone)
                             for phone in domain.phone_numbers],
            role = RoleResponseMapper.from_domain(domain.role),
            created_at = domain.created_at,
            updated_at = domain.updated_at,
        )

    @staticmethod
    def to_domain(response: UserResponse) -> User:
        return User(
            user_id= response.id,
            name= response.full_name.split(" ")[0],
            last_name= response.full_name.split(" ")[1],
            username = response.username,
            email = response.email,
            is_active = response.is_active,
            phone_numbers = [PhoneNumberResponseMapper.to_domain(phone)
                             for phone in response.phone_numbers],
            role = RoleResponseMapper.to_domain(response.role),
            created_at = response.created_at,
            updated_at = response.updated_at,
        )