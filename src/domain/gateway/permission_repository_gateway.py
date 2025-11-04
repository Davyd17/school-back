from abc import ABC

from .generic_crud_gateway import GenericCrudGateway
from ..model.entities.permission import Permission

class PermissionRepositoryGateway(GenericCrudGateway[Permission], ABC):
    pass