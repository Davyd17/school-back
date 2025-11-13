from fastapi.params import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.subject_repository import SubjectRepository
from application.usecase.subject.find_all_subjects import FindAllSubjects
from infraestructure.repository.SQLModel.repository.subject_repository_impl import SubjectRepositoryImpl


def __provide_repository(session: session_dep) -> SubjectRepository:
    return SubjectRepositoryImpl(session)

def provide_find_all_subjects(repository: SubjectRepository
                                     = Depends(__provide_repository)):
    return FindAllSubjects(repository)