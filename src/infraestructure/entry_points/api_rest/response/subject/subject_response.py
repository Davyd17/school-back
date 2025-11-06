from pydantic import BaseModel


class SubjectResponse(BaseModel):
    id : int
    name : str
    description : str
    teacher_name :str