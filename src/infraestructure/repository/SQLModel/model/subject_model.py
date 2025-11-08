from datetime import datetime, timezone
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.repository.SQLModel.model.user_model.teacher_model import TeacherModel


class SubjectModel(SQLModel, table=True):
    __tablename__ = "subjects"

    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(unique=True)
    description : str
    created_at : datetime = Field(default_factory=lambda:datetime.now(timezone.utc))
    updated_at : Optional[datetime]
    teacher_id : int = Field(foreign_key="teachers.id")

    teacher : Optional[TeacherModel] = Relationship()

