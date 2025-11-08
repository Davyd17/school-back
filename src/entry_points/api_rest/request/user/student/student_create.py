from entry_points.api_rest.request.user.base.user_create import UserCreate


class StudentCreate(UserCreate):
    group_id : int
