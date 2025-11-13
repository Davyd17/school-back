from typing import Optional, TypeVar, Type

from application.exception.not_found_exception import NotFoundException

T = TypeVar("T")

def step_validate_entity_exists_by_id(entity_to_check: Optional[T],
                                      entity_class: Type[T],
                                      id: int):

    if entity_to_check is None:
        raise NotFoundException(f"{entity_class.__name__} with id: {id} not found")