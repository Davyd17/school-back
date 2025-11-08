from domain.entities.permission import Permission
from entry_points.api_rest.response.permission.permission_response import PermissionResponse


class PermissionResponseMapper:

    @staticmethod
    def from_domain(domain: Permission) -> PermissionResponse:
        return PermissionResponse(
            id=domain.id,
            name=domain.name
        )

    @staticmethod
    def to_domain(response: PermissionResponse) -> Permission:
        return Permission(
            id=response.id,
            name=response.name
        )