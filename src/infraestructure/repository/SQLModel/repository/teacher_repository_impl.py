from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.teacher_repository import TeacherRepository
from domain.entities.user.teacher import Teacher
from ..mapper.teacher_model_mapper import TeacherModelMapper
from ..model.user_model.teacher_model import TeacherModel

class TeacherRepositoryImpl(TeacherRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_by_id(self, id: int) -> Optional[Teacher]:

        teacher_model : Optional[TeacherModel]= self.__session.get(TeacherModel, id)
        if teacher_model is None:
            return None

        return TeacherModelMapper.to_domain(teacher_model)

    def get_all(self) -> List[Teacher]:

        teachers_model = self.__session.exec(select(TeacherModel)).all()
        return [TeacherModelMapper.to_domain(teacher) for teacher in teachers_model]

    def create(self, create: Teacher) -> Teacher:
        pass

    def update(self, update: Teacher) -> Teacher:
        pass

    def delete(self, id: int):
        pass
