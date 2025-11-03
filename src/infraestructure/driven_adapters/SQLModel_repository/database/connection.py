from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine


DATABASE_URL = "mysql+pymysql://root:pass@localhost:3306/school"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_session)]