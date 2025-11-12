from decimal import Decimal
from typing import Optional, List

from sqlmodel import Field, Relationship, SQLModel

from .user_model import UserModel
from ..group_model import GroupModel


class TeacherModel(SQLModel, table=True):
    __tablename__ = "teachers"

    teacher_id: Optional[int] = Field(default=None,
                                      primary_key=True,
                                      sa_column_kwargs={"name": "id"})

    salary: Decimal = Field(default=None, nullable=False)

    user_id: int = Field(foreign_key="users.id",
                         nullable=False)
    user: Optional[UserModel] = Relationship()

    groups: List[GroupModel] = Relationship(back_populates="teacher")
