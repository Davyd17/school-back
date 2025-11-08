from typing import List

from application.gateway.repository.model.subject_repository import SubjectRepository
from domain.entities.subject import Subject


class FindAllSubjects:
    def __init__(self, repository:SubjectRepository):
        self.__repository = repository

    def execute(self) -> List[Subject]:
        return self.__repository.get_all()


