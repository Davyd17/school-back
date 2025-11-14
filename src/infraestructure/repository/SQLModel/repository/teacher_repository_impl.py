from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError
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

        try:

            teacher_model, user_model = TeacherModelMapper.from_domain(create)

            self.__session.add(user_model)
            self.__session.flush()

            teacher_model.user_id = user_model.user_id

            self.__session.add(teacher_model)
            self.__session.commit()
            self.__session.refresh(teacher_model)

            return TeacherModelMapper.to_domain(teacher_model)

        except SQLAlchemyError as e:
            raise Exception(f"Database exception when creating teacher: {e}")

    def update(self, update: Teacher) -> Teacher:

        try:
            new_teacher_model, new_user_model = TeacherModelMapper.from_domain(update)



            self.__session.merge(new_user_model)
            teacher_merged = self.__session.merge(new_teacher_model)
            self.__session.commit()
            self.__session.refresh(teacher_merged)
            self.__session.refresh(teacher_merged.user)

            return TeacherModelMapper.to_domain(teacher_merged)

        except SQLAlchemyError as e:
            raise Exception(f"Database exception when updating teacher: {e}")

    def delete(self, id: int):
        pass
