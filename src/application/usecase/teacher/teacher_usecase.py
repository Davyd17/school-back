from application.gateway.repository.model.teacher_repository import TeacherRepository


class TeacherUseCase:
    def __init__(self, repository: TeacherRepository):
        self._repository = repository