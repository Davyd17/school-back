from application.gateway.repository.model.student_repository import StudentRepository
from application.usecase.student.student_usecase import StudentUseCase
from domain.entities.user.student import Student

class UpdateStudent(StudentUseCase):
    def __init__(self, repository: StudentRepository):
        super().__init__(repository)

    def execute(self, update: Student) -> Student:
        pass

        



