from abc import ABC

from domain.gateway.generic_crud_gateway import GenericCrudGateway


class PhoneNumberRepositoryGateway(GenericCrudGateway, ABC):
    pass