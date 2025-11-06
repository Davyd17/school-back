from decimal import Decimal
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.driven_adapters.SQLModel_repository.model.subject_model import SubjectModel
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.student_model import StudentModel


class StudentSubjectModel(SQLModel, table=True):
    __tablename__ = "student_subject"

    student_id : int = Field(foreign_key="students.id", primary_key=True)
    subject_id : int = Field(foreign_key="subjects.id", primary_key=True)
    average : Decimal = Field(nullable=False, default=0)

    student : Optional[StudentModel] = Relationship()
    subject : Optional[SubjectModel] = Relationship()