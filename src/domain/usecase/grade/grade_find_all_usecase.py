from typing import List

from ...gateway.grade_repository_gateway import GradeRepositoryGateway
from ...model.entities.grade import Grade


class GradeFindAllUseCase:
    def __init__(self, repository: GradeRepositoryGateway):
        self.repository = repository

    def execute(self) -> List[Grade]:
        return self.repository.get_all()
