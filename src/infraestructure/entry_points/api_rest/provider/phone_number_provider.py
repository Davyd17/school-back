from fastapi import Depends

from domain.gateway.phone_number_repository_gateway import PhoneNumberRepositoryGateway
from domain.usecase.phone_number.phone_number_find_all_usecase import PhoneNumberFindAllUseCase
from ....driven_adapters.SQLModel_repository.database.connection import session_dep
from ....driven_adapters.SQLModel_repository.repository.phone_number_repository import PhoneNumberRepository


def get_phone_number_repository(session: session_dep) -> PhoneNumberRepositoryGateway:
    return PhoneNumberRepository(session)

def get_phone_number_find_all_usecase(repository: PhoneNumberRepositoryGateway = Depends(get_phone_number_repository)):
    return PhoneNumberFindAllUseCase(repository)