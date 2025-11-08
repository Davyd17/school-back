from application.gateway.repository.model.student_repository import StudentRepository
from domain.entities.user.student import Student
from application.usecase.group.find_group_by_id import FindGroupById
from application.usecase.role.find_role_by_id import FindRoleById


class CreateStudent:
    def __init__(self, repository: StudentRepository,
                 find_group_by_id: FindGroupById,
                 find_role_by_id: FindRoleById):
        self.__repository = repository
        self.__find_group_by_id = find_group_by_id
        self.__find_role_by_id = find_role_by_id

    def execute(self, create: Student) -> Student:

        group = self.__find_group_by_id.execute(create.group.id)
        create.group = group

        role = self.__find_role_by_id.execute(create.role.id)
        create.role = role

        return self.__repository.create(create)


