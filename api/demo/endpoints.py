from pathlib import Path

from fastapi import Header

from api.demo.schemas import Number


async def root():
    return {"message": "Hello World"}


async def read_item(item_id: int):
    return {"item_id": item_id}


async def get_numbers(number: Number):
    return {"number": number}


async def get_files(file_path: Path):
    return {
        "file_name": file_path.name,
        "extension": file_path.suffix,
        "root": file_path.root,
    }


async def read_accept_language(accept_language: str = Header(...)):
    pass
