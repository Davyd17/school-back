from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from infraestructure.repository.SQLModel.model.grade_model import GradeModel
    from infraestructure.repository.SQLModel.model.user_model.teacher_model import TeacherModel



class GroupModel(SQLModel, table=True):
    __tablename__ = "groups"

    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(nullable=False, unique=True)
    grade_id: int = Field(nullable=False, foreign_key="grades.id")
    teacher_id: int = Field(nullable=True, foreign_key="teachers.id")

    teacher: Optional["TeacherModel"] = Relationship(back_populates="groups")
    grade: Optional["GradeModel"] = Relationship(back_populates="groups")