from sqlmodel import SQLModel, Field


class GroupGradeModelLink(SQLModel, table=True):
    __tablename__ = "groups_grades"

    group_id : int = Field(foreign_key="groups.id", primary_key=True)
    grade_id : int = Field(foreign_key="grades.id", primary_key=True)