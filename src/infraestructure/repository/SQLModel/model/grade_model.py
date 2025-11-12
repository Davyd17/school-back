from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.repository.SQLModel.model.group_model import GroupModel

class GradeModel(SQLModel, table=True):
    __tablename__ = "grades"

    id: Optional[int] = Field(default=None, primary_key=True)
    level: str = Field(unique=True)

    groups: List["GroupModel"] = Relationship(back_populates="grade")


