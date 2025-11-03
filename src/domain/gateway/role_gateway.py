from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model.entities.role import Role


class RoleGateway(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Role]:
        pass

    @abstractmethod
    def get_all(self) -> List[Role]:
        pass

    @abstractmethod
    def create(self, role: Role) -> Role:
        pass

    @abstractmethod
    def update(self, id: int, role: Role) -> Role:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass