from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated
import random
import string

app = FastAPI()

# The Password Generator API auto-generates random passwords that are incredibly hard to guess.

class FilterParameters (BaseModel):
    length: int = Field(8)
    exclude_numbers: bool = Field(False)
    exclude_special_chars: bool = Field(False)

@app.get("/v1/passwordgenerator/")
async def generator(filter_query: Annotated[FilterParameters, Query()]):
    length = filter_query.length
    allowed_chars=string.ascii_letters
    if (filter_query.exclude_numbers is False):
        allowed_chars += string.digits
    if (filter_query.exclude_special_chars is False):
        allowed_chars += string.punctuation
    random_string = ''.join(random.choices(allowed_chars, k=length))
    
    return random_string