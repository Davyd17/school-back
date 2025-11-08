from domain.entities.phone_number import PhoneNumber
from entry_points.api_rest.response.phone_number.phone_number_response import PhoneNumberResponse


class PhoneNumberResponseMapper:

    @staticmethod
    def from_domain(domain: PhoneNumber) -> PhoneNumberResponse:
        return PhoneNumberResponse(
            id=domain.id,
            full_number=domain.get_full_number(),
            is_active=domain.is_active
        )

    @staticmethod
    def to_domain(response: PhoneNumberResponse) -> PhoneNumber:
        return PhoneNumber(
            id=response.id,
            ext=int(response.full_number.split("-")[0]),
            phone=response.full_number.split("-")[1],
            is_active=response.is_active
        )