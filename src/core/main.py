from fastapi import Depends, FastAPI, HTTPException, Response

from infraestructure.entry_points.api_rest.route.permission_router import router as permission_router
from infraestructure.entry_points.api_rest.route.role_router import router as role_router

app = FastAPI(root_path="/api/v1/school")

app.include_router(role_router)

app.include_router(permission_router)