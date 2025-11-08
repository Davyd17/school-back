from datetime import datetime
from typing import Optional, List


from sqlmodel import SQLModel, Field, Relationship

from infraestructure.repository.SQLModel.model.phone_number_model import PhoneNumberModel
from infraestructure.repository.SQLModel.model.role_model import RoleModel


class UserModel(SQLModel, table=True):
    __tablename__ = "users"

    user_id : int | None = Field(default=None,
                                 primary_key=True,
                                 sa_column_kwargs={"name": "id"})
    name : str
    last_name : str
    username : str
    email : str
    password : str
    is_active : bool | None = Field(default=True)
    created_at : datetime | None = Field(default_factory=datetime.now)
    updated_at : datetime | None = Field(default=None)
    role_id : int = Field(foreign_key="roles.id")

    role : Optional[RoleModel] = Relationship(back_populates="users")
    phone_numbers: List[PhoneNumberModel] = Relationship(back_populates="user")
