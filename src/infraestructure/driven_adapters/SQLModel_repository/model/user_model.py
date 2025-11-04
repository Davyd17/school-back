from datetime import datetime
from typing import Optional, List, TYPE_CHECKING


from sqlmodel import SQLModel, Field, Relationship

from .phone_number_model import PhoneNumberModel
from .role_model import RoleModel


class UserModel(SQLModel, table=True):
    __tablename__ = "users"

    id : int | None = Field(default=None, primary_key=True)
    name : str
    last_name : str
    username : str
    email : str
    password : str
    is_active : bool
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime | None = Field(default=None)
    phone_numbers: List[PhoneNumberModel] = Relationship(back_populates="user")

    role_id : int = Field(foreign_key="roles.id")
    role : Optional[RoleModel] = Relationship(back_populates="users")
