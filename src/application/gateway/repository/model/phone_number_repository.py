from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud


class PhoneNumberRepository(GenericCrud, ABC):
    pass