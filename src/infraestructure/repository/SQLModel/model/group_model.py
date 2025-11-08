from typing import Optional

from sqlmodel import SQLModel, Field


class GroupModel(SQLModel, table=True):
    __tablename__ = "groups"

    id : Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(nullable=False, unique=True)