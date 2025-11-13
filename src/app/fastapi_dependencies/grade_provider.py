from fastapi import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.grade_repository import GradeRepository
from application.usecase.grade.find_all_grades import FindAllGrades
from infraestructure.repository.SQLModel.repository.grade_repository_impl import GradeRepositoryImpl


def __provide_repository(session: session_dep) -> GradeRepository:
    return GradeRepositoryImpl(session)

def provide_find_all_grades(repository: GradeRepository
                                   = Depends(__provide_repository)):
    return FindAllGrades(repository)