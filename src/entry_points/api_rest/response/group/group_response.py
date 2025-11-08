from pydantic import BaseModel


class GroupResponse(BaseModel):
    id : int
    name : str