from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud


class SubjectRepository(GenericCrud, ABC):
    pass