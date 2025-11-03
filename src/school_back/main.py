from fastapi import Depends, FastAPI, HTTPException, Response
from sqlmodel import Session, Field, create_engine, select, SQLModel

from typing import Annotated, Any, List, Optional
from random import randint

from infraestructure.driven_adapters.SQLModel_repository.database.connection import create_db_and_tables
from infraestructure.entry_points.api_rest.route.role_router import router as role_router

# # Define SQLModel and database connection
# url_connection = 'mysql+pymysql://root:pass@localhost:3306/school'
# engine = create_engine(url_connection)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#         yield session

# session_dep = Annotated[Session, Depends(get_session)]

# #Define Models
# class Role(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     description: str

# class RoleRequest(SQLModel):
#     name: str | Optional[str] = None
#     description: str | Optional[str] = None

# class RoleResponse(SQLModel):
#     id: int 
#     name: str
#     description: str


app = FastAPI(root_path="/api/v1/school")

app.add_event_handler("startup", create_db_and_tables)

app.include_router(role_router)

# @app.post("/roles", response_model=RoleResponse, status_code=201)
# def create_role(request: RoleRequest, session: session_dep):
#     new_role = Role.model_validate(request)
#     session.add(new_role)
#     session.commit()
#     session.refresh(new_role)
#     return new_role

# @app.get("/roles", response_model= List[RoleResponse])
# def read_roles(session: session_dep):
#     roles = session.exec(select(Role)).all()
#     return roles

# @app.get("/roles/{id}", response_model=RoleResponse)
# def read_role(id: int, session: session_dep):
#     role = session.get(Role, id)
#     if not role:
#         raise HTTPException(status_code=404, detail="Role not found")
    
#     return role

# @app.patch("/roles/{id}", response_model=RoleResponse)
# def update_role(id: int, request: RoleRequest, session: session_dep):

#     role_db = session.get(Role, id)

#     if not role_db:
#         raise HTTPException(status_code=404, detail="Role not found")
    
#     role_data = request.model_dump(exclude_unset=True)  
#     role_db.sqlmodel_update(role_data)

#     session.add(role_db)
#     session.commit()
#     session.refresh(role_db)

#     return role_db

# @app.delete("/roles/{id}", status_code=204)
# def delete_role(id: int, session: session_dep):

#     role_db = session.get(Role, id)

#     if not role_db:
#         raise HTTPException(status_code=404, detail="Role not found")
    
#     session.delete(role_db)
#     session.commit()

#     return Response(status_code=204)