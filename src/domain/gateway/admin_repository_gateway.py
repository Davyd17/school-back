from abc import ABC

from domain.gateway.generic_crud_gateway import GenericCrudGateway
from domain.model.entities.user.admin import Admin


class AdminRepositoryGateway(GenericCrudGateway[Admin], ABC):
    pass