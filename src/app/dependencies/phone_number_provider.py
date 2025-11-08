from fastapi import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.phone_number_repository import PhoneNumberRepository
from application.usecase.phone_number.find_all_phone_numbers import FindALlPhoneNumbers
from infraestructure.repository.SQLModel.repository.phone_number_repository_impl import PhoneNumberRepositoryImpl

def __provide_repository(session: session_dep) -> PhoneNumberRepository:
    return PhoneNumberRepositoryImpl(session)

def provide_find_all_phone_numbers(repository: PhoneNumberRepository = Depends(__provide_repository)):
    return FindALlPhoneNumbers(repository)