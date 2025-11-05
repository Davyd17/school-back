from typing import List

from domain.gateway.teacher_repository_gateway import TeacherRepositoryGateway
from domain.model.entities.user.teacher import Teacher

class TeacherFindAllUseCase:
    def __init__(self, repository: TeacherRepositoryGateway):
        self.teacher = repository

    def execute(self) -> List[Teacher]:
        return self.teacher.get_all()