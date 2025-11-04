from abc import ABC

from domain.gateway.generic_crud_gateway import GenericCrudGateway
from domain.model.entities.user.user import User


class UserRepositoryGateway(GenericCrudGateway[User], ABC):
    pass