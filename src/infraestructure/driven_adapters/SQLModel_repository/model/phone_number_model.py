from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

class PhoneNumberModel(SQLModel, table=True):
    __tablename__ = "phone_numbers"

    id: int | None = Field(default=None, primary_key=True)
    ext: int | None
    phone: str
    is_active: bool = True
    user_id: int = Field(foreign_key="users.id")
    user: Optional["UserModel"] = Relationship(back_populates="phone_numbers")