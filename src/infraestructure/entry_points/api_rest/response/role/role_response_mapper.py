from domain.model.entities.role import Role
from ..role.role_response import RoleResponse

class RoleResponseMapper:

    @staticmethod
    def from_domain(role: Role) -> RoleResponse:
        return RoleResponse(
            id=role.id,
            name=role.name,
            description=role.description
        )

    @staticmethod
    def to_domain(role_response: RoleResponse) -> Role:
        return Role(
            id=role_response.id,
            name=role_response.name,
            description=role_response.description
        )

