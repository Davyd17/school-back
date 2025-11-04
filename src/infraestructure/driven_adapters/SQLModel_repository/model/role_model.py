from typing import List, TYPE_CHECKING

from sqlmodel import Field, SQLModel, Relationship

from .link_models.role_permission_link import RolePermissionLink
from .permission_model import PermissionModel

if TYPE_CHECKING:
    from .user_model import UserModel

class RoleModel(SQLModel, table=True):
    __tablename__ = "roles"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str

    permissions: List[PermissionModel] = Relationship(
        link_model=RolePermissionLink
    )

    users: List["UserModel"] = Relationship(back_populates="role")