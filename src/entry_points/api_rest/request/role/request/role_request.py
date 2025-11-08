from pydantic import BaseModel


class RoleRequest(BaseModel):
    id: int