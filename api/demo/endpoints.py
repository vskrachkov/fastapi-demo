from pathlib import Path

from fastapi import Header, APIRouter, status

from api.demo.schemas import Number

demo = APIRouter()


@demo.api_route("/", methods=["get"])
async def root():
    return {"message": "Hello World"}


@demo.api_route("/items/{item_id}", methods=["get"])
async def read_item(item_id: int):
    return {"item_id": item_id}


@demo.api_route("/numbers/{number}", methods=["get"])
async def get_numbers(number: Number):
    return {"number": number}


@demo.api_route("/files/{file_path:path}", methods=["get"])
async def get_files(file_path: Path):
    return {
        "file_name": file_path.name,
        "extension": file_path.suffix,
        "root": file_path.root,
    }


@demo.api_route(
    "/read_accept_language",
    methods=["get"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def read_accept_language(accept_language: str = Header(...)):
    pass
