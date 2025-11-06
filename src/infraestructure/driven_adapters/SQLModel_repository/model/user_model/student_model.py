from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.driven_adapters.SQLModel_repository.model.group_model import GroupModel
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.user_model import UserModel


class StudentModel(SQLModel, table=True):
    __tablename__ = "students"

    student_id : Optional[int] = Field(default=None,
                                      primary_key=True,
                                      sa_column_kwargs={"name": "id"})
    user_id : int = Field(foreign_key="users.id")
    group_id : int = Field(foreign_key="groups.id")

    user : Optional[UserModel] = Relationship()
    group : Optional[GroupModel] = Relationship()