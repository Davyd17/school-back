from pydantic import BaseModel

class PermissionResponse(BaseModel):
    id: int
    name: str