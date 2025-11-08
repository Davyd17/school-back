from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.grade_repository import GradeRepository
from domain.entities.grade import Grade
from ..mapper.grade_model_mapper import GradeModelMapper
from ..model.grade_model import GradeModel


class GradeRepositoryImpl(GradeRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = GradeModel

    def get_by_id(self, id: int) -> Optional[Grade]:
        pass

    def get_all(self) -> List[Grade]:

        grades_db = self.session.exec(select(self.model)).all()
        return [GradeModelMapper.to_domain(grade) for grade in grades_db]

    def create(self, create: Grade) -> Grade:
        pass

    def update(self, id: int, update: Grade) -> Grade:
        pass

    def delete(self, id: int):
        pass