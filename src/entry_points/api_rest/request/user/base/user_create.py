from pydantic import BaseModel
from entry_points.api_rest.request.role.request.role_request import RoleRequest


class UserCreate(BaseModel):

    name: str
    last_name: str
    username: str
    email: str
    password: str
    role_request: RoleRequest

