from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from infraestructure.repository.SQLModel.config.connection import get_session


def _provide_session():
    with get_session() as session:
        yield session

session_dep = Annotated[Session, Depends(_provide_session)]