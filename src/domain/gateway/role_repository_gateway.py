from abc import ABC

from .generic_crud_gateway import GenericCrudGateway
from ..model.entities.role import Role

class RoleRepositoryGateway(GenericCrudGateway[Role], ABC):
    pass