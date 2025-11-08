from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud
from domain.entities.user.admin import Admin


class AdminRepository(GenericCrud[Admin], ABC):
    pass