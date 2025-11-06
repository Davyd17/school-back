from typing import List

from domain.gateway.student_repository_gateway import StudentRepositoryGateway
from domain.model.entities.user.student import Student


class StudentFindAllUsecase:
    def __init__(self, repository: StudentRepositoryGateway):
        self.repository__ = repository

    def execute(self) -> List[Student]:
        return self.repository__.get_all()