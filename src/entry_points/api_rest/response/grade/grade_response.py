from typing import List

from pydantic import BaseModel

class GradeResponse(BaseModel):
    id: int
    level: str