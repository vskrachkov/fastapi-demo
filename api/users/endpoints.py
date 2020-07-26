from typing import Optional, List

from fastapi import Query, Path, APIRouter, status

from api.users.schemas import User, Organization

users = APIRouter()


@users.api_route(
    "/",
    methods=["get"],
    response_model=List[User],
    description="Return users with all applied filters",
)
async def get_users(
    limit: int = 2,
    search: Optional[str] = Query(None, max_length=10),
    age_filter: Optional[List[int]] = Query(None, alias="age"),
) -> List[dict]:
    all_users = (
        {"name": "Karl", "age": 13},
        {"name": "Linda", "age": 14},
        {"name": "Olenka", "age": 35},
        {"name": "Slavko", "age": 25},
    )

    response = all_users

    if age_filter:
        response = list(filter(lambda u: u["age"] in age_filter, response))

    if search:
        response = list(filter(lambda u: search in u["name"], response))

    if limit:
        response = response[:limit]

    return response


@users.api_route(
    "/",
    methods=["post"],
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: User) -> User:
    return user


@users.api_route("/{user_id:int}", methods=["put"], response_model=User)
async def replace_user(user_id: int, user: User) -> User:
    return user


@users.api_route(
    "/organization_users/{organization}",
    methods=["get"],
    response_model=List[User],
)
async def get_organization_users(
    organization: Organization = Path(..., title="The ID of the item to get"),
    search: Optional[str] = None,
) -> List[dict]:
    all_users = {
        "google": ({"name": "Karl"},),
        "apple": ({"name": "Linda"},),
        "super": ({"name": "Olenka"}, {"name": "Slavko"}),
    }

    response = all_users[organization.value]
    if search:
        response = list(filter(lambda u: search in u["name"], response))

    return response
