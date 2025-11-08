from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from infraestructure.repository.SQLModel.config.connection import get_session

_session_dep = Annotated[Session, Depends(get_session)]