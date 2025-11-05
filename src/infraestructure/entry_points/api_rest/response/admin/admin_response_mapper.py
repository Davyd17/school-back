from domain.model.entities.user.admin import Admin
from .admin_response import AdminResponse
from ..phone_number.phone_number_response_mapper import PhoneNumberResponseMapper
from ..role.role_response_mapper import RoleResponseMapper


class AdminResponseMapper:

    @staticmethod
    def from_domain(domain: Admin) -> AdminResponse:

        return AdminResponse(
            admin_id=domain.admin_id,
            full_name=domain.get_full_name(),
            username=domain.username,
            email=domain.email,
            is_active=domain.is_active,
            phone_numbers=[PhoneNumberResponseMapper.from_domain(phone)
                           for phone in domain.phone_numbers],
            role=RoleResponseMapper.from_domain(domain.role)
        )

    @staticmethod
    def to_domain(response: AdminResponse) -> Admin:

        return Admin(
            admin_id=response.admin_id,
            name=response.full_name.split(" ")[0],
            last_name=" ".join(response.full_name.split(" ")[1:]),
            username=response.username,
            email=response.email,
            is_active=response.is_active,
            phone_numbers=[PhoneNumberResponseMapper.to_domain(phone)
                           for phone in response.phone_numbers],
            role=RoleResponseMapper.to_domain(response.role)
        )

