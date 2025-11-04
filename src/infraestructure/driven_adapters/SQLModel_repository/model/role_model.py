from sqlmodel import Field, SQLModel


class RoleModel(SQLModel, table=True):
    __tablename__ = "roles"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str