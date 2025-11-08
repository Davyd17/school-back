from domain.entities.role import Role
from entry_points.api_rest.request.role.request.role_request import RoleRequest


class RoleRequestMapper:

    @staticmethod
    def from_domain(domain: Role) -> RoleRequest:

        return RoleRequest(
            id=domain.id
        )

    @staticmethod
    def to_domain(request: RoleRequest) -> Role:

        return Role(
            id=request.id
        )