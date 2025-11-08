from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud
from domain.entities.user.user import User


class UserRepository(GenericCrud[User], ABC):
    pass