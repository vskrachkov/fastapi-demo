from typing import Optional, List

from fastapi import Query, Path

from api.users.schemas import User, Organization


async def get_users(
    limit: int = 2,
    search: Optional[str] = Query(None, max_length=10),
    age_filter: Optional[List[int]] = Query(None, alias="age"),
):
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


async def create_user(user: User) -> User:
    return user


async def replace_user(user_id: int, user: User) -> User:
    return user


async def get_organization_users(
    organization: Organization = Path(..., title="The ID of the item to get"),
    search: Optional[str] = None,
):
    users = {
        "google": ({"name": "Karl"},),
        "apple": ({"name": "Linda"},),
        "super": ({"name": "Olenka"}, {"name": "Slavko"}),
    }

    response = users[organization.value]
    if search:
        response = list(filter(lambda u: search in u["name"], response))

    return response
