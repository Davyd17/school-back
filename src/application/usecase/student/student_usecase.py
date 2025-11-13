from application.gateway.repository.model.student_repository import StudentRepository


class StudentUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository