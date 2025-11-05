from abc import ABC

from domain.gateway.generic_crud_gateway import GenericCrudGateway, T
from domain.model.entities.user.teacher import Teacher


class TeacherRepositoryGateway(GenericCrudGateway[Teacher], ABC):
    pass