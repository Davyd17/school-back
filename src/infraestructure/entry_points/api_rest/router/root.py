from fastapi import FastAPI

from infraestructure.entry_points.api_rest.router.teacher_router import router as teacher_router
from infraestructure.entry_points.api_rest.router.admin_router import router as admin_router
from infraestructure.entry_points.api_rest.router.permission_router import router as permission_router
from infraestructure.entry_points.api_rest.router.role_router import router as role_router
from infraestructure.entry_points.api_rest.router.user_route import router as user_router
from infraestructure.entry_points.api_rest.router.phone_number_route import router as phone_number_router

app = FastAPI(root_path="/api/v1/school")

app.include_router(role_router)

app.include_router(permission_router)

app.include_router(user_router)

app.include_router(phone_number_router)

app.include_router(admin_router)

app.include_router(teacher_router)