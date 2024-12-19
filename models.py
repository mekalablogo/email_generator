from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import List
import re

# Define a schema for the input using Pydantic
class InputData(BaseModel):
    email: EmailStr = Field(..., example="kim@possible@gmail.com")
    name: str = Field(..., example="Kim Possible", min_length=1, max_length=100)
    country: str = Field(..., example="India", pattern=r"^[A-Za-z ]+$")
    contact_number: str = Field(..., example="+9111111111", pattern=r"^\+\d{10,15}$")
    message: str = Field(..., example="Need Go and Web developers", min_length=1, max_length=500)
    last_3_pages_visited: List[HttpUrl] = Field(..., example=[
        "https://www.mindinventory.com/golang-development.php",
        "https://www.mindinventory.com/hire-ai-developers.php",
        "https://www.mindinventory.com/healthcare-solutions.php"
    ])