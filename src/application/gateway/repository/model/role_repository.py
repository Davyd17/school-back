from abc import ABC, abstractmethod
from typing import Optional

from application.gateway.repository.generic_crud import GenericCrud
from domain.entities.role import Role

class RoleRepository(GenericCrud[Role], ABC):
    pass