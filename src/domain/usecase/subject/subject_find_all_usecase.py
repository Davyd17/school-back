from http.cookiejar import request_port
from typing import List

from domain.gateway.subject_repository_gateway import SubjectRepositoryGateway
from domain.model.entities.subject import Subject


class SubjectFindAllUseCase:
    def __init__(self, repository:SubjectRepositoryGateway):
        self.__repository = repository

    def execute(self) -> List[Subject]:
        return self.__repository.get_all()


