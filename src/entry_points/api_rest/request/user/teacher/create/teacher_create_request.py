from decimal import Decimal

from pydantic import Field

from entry_points.api_rest.request.user.base.user_create import UserCreate


class TeacherCreateRequest(UserCreate):
    salary : Decimal = Field(ge=0.00)

