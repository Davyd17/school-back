from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud


class StudentRepository(GenericCrud, ABC):
    pass