from typing import List

from sqlmodel import SQLModel, Field, Relationship

from .link_models.role_permission_link import RolePermissionLink


class PermissionModel(SQLModel, table=True):
    __tablename__ = "permissions"

    id: int = Field(default=None, primary_key=True)
    name: str