from domain.model.entities.role import Role
from infraestructure.driven_adapters.SQLModel_repository.model.role_model import RoleModel


class RoleModelMapper:

    @staticmethod
    def to_domain(role_model: RoleModel) -> Role:

        return Role(
            id = role_model.id,
            name = role_model.name,
            description = role_model.description
        )

    @staticmethod
    def to_model(role: Role) -> RoleModel:

        return RoleModel(
            id = role.id,
            name = role.name,
            description = role.description
        )