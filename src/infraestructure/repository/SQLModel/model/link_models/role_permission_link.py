from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class RolePermissionLink(SQLModel, table=True):
    __tablename__ = "roles_permissions"

    role_id: int = Field(foreign_key="roles.id", primary_key=True)
    permission_id: int = Field(foreign_key="permissions.id", primary_key=True)
