from domain.model.entities.role import Role
from .permission_model_mapper import PermissionModelMapper
from ..model.role_model import RoleModel


class RoleModelMapper:

    @staticmethod
    def to_domain(role_model: RoleModel) -> Role:

        return Role(
            id = role_model.id,
            name = role_model.name,
            description = role_model.description,
            permissions = [
                PermissionModelMapper.to_domain(permission_model)
                for permission_model in role_model.permissions
            ]
        )

    @staticmethod
    def to_model(role: Role) -> RoleModel:

        return RoleModel(
            id = role.id,
            name = role.name,
            description = role.description,
            permissions = [
                PermissionModelMapper.from_domain(permission)
                for permission in role.permissions
            ]
        )