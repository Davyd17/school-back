from fastapi import FastAPI

from .group_router import router as group_router
from .grade_router import router as grade_router
from .teacher_router import router as teacher_router
from .admin_router import router as admin_router
from .permission_router import router as permission_router
from .role_router import router as role_router
from .user_route import router as user_router
from .phone_number_router import router as phone_number_router

app = FastAPI(root_path="/api/v1/school")

app.include_router(role_router)

app.include_router(permission_router)

app.include_router(user_router)

app.include_router(phone_number_router)

app.include_router(admin_router)

app.include_router(teacher_router)

app.include_router(grade_router)

app.include_router(group_router)