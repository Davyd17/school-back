from abc import ABC

from domain.gateway.generic_crud_gateway import GenericCrudGateway


class GroupRepositoryGateway(GenericCrudGateway, ABC):
    pass