from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.grade_repository_gateway import GradeRepositoryGateway
from domain.model.entities.grade import Grade
from ..mapper.grade_model_mapper import GradeModelMapper
from ..model.grade_model import GradeModel


class GradeRepository(GradeRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = GradeModel

    def get_by_id(self, id: int) -> Optional[Grade]:
        pass

    def get_all(self) -> List[Grade]:

        grades_db = self.session.exec(select(self.model)).all()
        return [GradeModelMapper.to_domain(grade) for grade in grades_db]

    def create(self, entity: Grade) -> Grade:
        pass

    def update(self, id: int, entity: Grade) -> Grade:
        pass

    def delete(self, id: int):
        pass