from decimal import Decimal
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.repository.SQLModel.model.subject_model import SubjectModel
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel


class StudentSubjectModel(SQLModel, table=True):
    __tablename__ = "student_subject"

    student_id : int = Field(foreign_key="students.id", primary_key=True)
    subject_id : int = Field(foreign_key="subjects.id", primary_key=True)
    average : Decimal = Field(nullable=False, default=0)

    student : Optional[StudentModel] = Relationship()
    subject : Optional[SubjectModel] = Relationship()