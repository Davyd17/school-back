from typing import List

from application.gateway.repository.model.teacher_repository import TeacherRepository
from domain.entities.user.teacher import Teacher

class FindALlTeachers:
    def __init__(self, repository: TeacherRepository):
        self.teacher = repository

    def execute(self) -> List[Teacher]:
        return self.teacher.get_all()