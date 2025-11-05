from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from infraestructure.driven_adapters.SQLModel_repository.model.group_model import GroupModel
from infraestructure.driven_adapters.SQLModel_repository.model.link_models.group_grade_model_link import \
    GroupGradeModelLink


class GradeModel(SQLModel, table=True):
    __tablename__ = "grades"

    id: Optional[int] = Field(default=None, primary_key=True)
    level: str = Field(unique=True)

    groups: List[GroupModel] = Relationship(
        link_model=GroupGradeModelLink
    )


