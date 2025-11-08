from abc import ABC

from application.gateway.repository.generic_crud import GenericCrud
from domain.entities.user.teacher import Teacher


class TeacherRepository(GenericCrud[Teacher], ABC):
    pass