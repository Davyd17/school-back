from infraestructure.entry_points.api_rest.response.user.base.user_response import UserResponse


class AdminResponse(UserResponse):
    admin_id: int | None = None