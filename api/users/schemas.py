from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Organization(str, Enum):
    google = "google"
    apple = "apple"
    super = "super"


class Address(BaseModel):
    country_code: str = Field(
        ...,
        title="The country code (ISO 3166-1 alpha-2)",
        max_length=2,
        min_length=2,
        example="UA",
    )
    city: str = Field(..., max_length=50, example="Kyiv")


class User(BaseModel):
    name: str
    age: Optional[int] = None
    address: Optional[Address] = None
