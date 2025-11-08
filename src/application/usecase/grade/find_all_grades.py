from typing import List

from application.gateway.repository.model.grade_repository import GradeRepository
from domain.entities.grade import Grade


class FindAllGrades:
    def __init__(self, repository: GradeRepository):
        self.repository = repository

    def execute(self) -> List[Grade]:
        return self.repository.get_all()
