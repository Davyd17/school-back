from application.gateway.repository.model.teacher_repository import TeacherRepository
from application.usecase.teacher.teacher_usecase import TeacherUseCase
from domain.entities.user.teacher import Teacher


class CreateTeacher(TeacherUseCase):
    def __init__(self, repository: TeacherRepository):
        super().__init__(repository)

    def execute(self, teacher_create: Teacher) -> Teacher:
        return self._repository.create(teacher_create)