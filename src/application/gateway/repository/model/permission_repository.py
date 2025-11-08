from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud
from domain.entities.permission import Permission

class PermissionRepository(GenericCrud[Permission], ABC):
    pass