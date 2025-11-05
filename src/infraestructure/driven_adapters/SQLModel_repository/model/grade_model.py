from email.policy import default
from typing import Optional

from fastapi.datastructures import Default
from sqlmodel import SQLModel, Field


class GradeModel(SQLModel, table=True):
    __tablename__ = "grades"

    id: Optional[int] = Field(default=None, primary_key=True)
    level: str = Field(unique=True)
