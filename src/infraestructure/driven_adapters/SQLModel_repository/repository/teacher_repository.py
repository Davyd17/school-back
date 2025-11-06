from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.teacher_repository_gateway import TeacherRepositoryGateway
from domain.model.entities.user.teacher import Teacher
from ..mapper.teacher_model_mapper import TeacherModelMapper
from ..model.user_model.teacher_model import TeacherModel

class TeacherRepository(TeacherRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = TeacherModel

    def get_by_id(self, id: int) -> Optional[Teacher]:
        pass

    def get_all(self) -> List[Teacher]:

        teachers_model = self.session.exec(select(self.model)).all()
        return [TeacherModelMapper.to_domain(teacher) for teacher in teachers_model]

    def create(self, entity: Teacher) -> Teacher:
        pass

    def update(self, id: int, entity: Teacher) -> Teacher:
        pass

    def delete(self, id: int):
        pass
