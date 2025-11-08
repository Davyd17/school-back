from typing import List

from application.gateway.repository.model.student_repository import StudentRepository
from domain.entities.user.student import Student


class FindAllStudents:
    def __init__(self, repository: StudentRepository):
        self.repository__ = repository

    def execute(self) -> List[Student]:
        return self.repository__.get_all()