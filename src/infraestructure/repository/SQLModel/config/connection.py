from contextlib import contextmanager

from sqlmodel import Session, create_engine


DATABASE_URL = "mysql+pymysql://root:pass@localhost:3306/school"

engine = create_engine(DATABASE_URL, echo=False)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session