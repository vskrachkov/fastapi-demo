from fastapi import APIRouter

from api.users.endpoints import (
    get_users,
    create_user,
    replace_user,
    get_organization_users,
)

users = APIRouter()

users.add_api_route("/", get_users, methods=["get"])
users.add_api_route("/", create_user, methods=["post"])
users.add_api_route("/{user_id:int}", replace_user, methods=["put"])
users.add_api_route(
    "/organization_users/{organization}", get_organization_users, methods=["get"]
)
