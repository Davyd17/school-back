from domain.model.entities.phone_number import PhoneNumber
from infraestructure.driven_adapters.SQLModel_repository.model.phone_number_model import PhoneNumberModel


class PhoneNumberModelMapper:

    @staticmethod
    def to_domain(model: PhoneNumberModel) -> PhoneNumber:
        return PhoneNumber(
            id=model.id,
            ext=model.ext,
            phone=model.phone,
            is_active=model.is_active,
            contact=model.user
        )

    @staticmethod
    def from_domain(domain: PhoneNumber) -> PhoneNumberModel:
        return PhoneNumberModel(
            id=domain.id,
            ext=domain.ext,
            phone=domain.phone,
            is_active=domain.is_active,
            user_id=domain.contact.admin_id,
            user=domain.contact
        )