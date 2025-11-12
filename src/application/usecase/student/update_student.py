from typing import Optional

from application.exception.not_found_exception import NotFoundException
from application.gateway.repository.model.student_repository import StudentRepository
from application.usecase.student.student_usecase import StudentUseCase
from domain.entities.user.student import Student

class UpdateStudent(StudentUseCase):
    def __init__(self, repository: StudentRepository):
        super().__init__(repository)

    def execute(self, id: int, update_request: Student) -> Optional[Student]:

        student_found : Optional[Student] = self.repository.get_by_id(id)

        if student_found is None:
            raise NotFoundException(f"Student with id: {id} not found")

        return self.repository.update(id, update_request)

        



