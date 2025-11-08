from domain.entities.permission import Permission
from infraestructure.repository.SQLModel.model.permission_model import PermissionModel


class PermissionModelMapper:

    @staticmethod
    def to_domain(model: PermissionModel) -> Permission:
        return Permission(
            id=model.id,
            name=model.name
        )

    @staticmethod
    def from_domain(domain: Permission) -> PermissionModel:
        return PermissionModel(
            id=domain.id,
            name=domain.name
        )