from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session

from application.gateway.repository.model.student_repository import StudentRepository
from domain.entities.user.student import Student
from infraestructure.repository.SQLModel.mapper.student_model_mapper import StudentModelMapper
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_by_id(self, id: int) -> Optional[Student]:

        student_model:Optional[StudentModel] = self.__session.get(StudentModel, id)

        if not student_model:
            return None

        return StudentModelMapper.to_domain(student_model)

    def get_all(self) -> List[Student]:

        students_model = self.__session.exec(select(StudentModel)).all()
        return [StudentModelMapper.to_domain(student) for student in students_model]

    def create(self, create: Student) -> Student:

        try:

            student_model, user_model = StudentModelMapper.from_domain(create)

            self.__session.add(user_model)
            self.__session.flush()

            student_model.user_id = user_model.id

            self.__session.add(student_model)
            self.__session.commit()
            self.__session.refresh(student_model)

            return StudentModelMapper.to_domain(student_model)

        except SQLAlchemyError as e:
            self.__session.rollback()
            raise Exception(f"Database exception when creating: {e}")


    def update(self, update: Student) -> Optional[Student]:
        try:
            new_student_model, new_user_model = StudentModelMapper.from_domain(update)

            self.__session.merge(new_user_model)
            student_merged = self.__session.merge(new_student_model)
            self.__session.commit()
            self.__session.refresh(student_merged)
            self.__session.refresh(student_merged.user)

            return StudentModelMapper.to_domain(student_merged)
        except SQLAlchemyError as e:
            self.__session.rollback()
            raise Exception(f"Database exception when updating {e}")



    def delete(self, student:Student) -> bool:
        try:
            student_model, user_model = StudentModelMapper.from_domain(student)

            self.__session.delete(user_model)
            self.__session.commit()

            return True
        except SQLAlchemyError as e:
            self.__session.rollback()
            raise Exception(f"Database exception when deleting: {e}")


