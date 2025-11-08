from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.repository.SQLModel.model.user_model.user_model import UserModel


class AdminModel(SQLModel, table=True):
    __tablename__ = "admins"

    admin_id: int | None = Field(default=None,
                                 primary_key=True,
                                 sa_column_kwargs={"name": "id"})

    user_id: int = Field(foreign_key="users.id",
                         nullable=False)

    user: Optional[UserModel] = Relationship()