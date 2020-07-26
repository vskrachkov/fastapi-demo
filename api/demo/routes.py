from fastapi import APIRouter

from api.demo.endpoints import (
    root,
    read_item,
    get_numbers,
    get_files,
    read_accept_language,
)

demo = APIRouter()

demo.add_api_route("/", root, methods=["get"])
demo.add_api_route(
    "/read_accept_language", read_accept_language, methods=["get"]
)
demo.add_api_route("/items/{item_id}", read_item, methods=["get"])
demo.add_api_route("/numbers/{number}", get_numbers, methods=["get"])
demo.add_api_route("/files/{file_path:path}", get_files, methods=["get"])
