"Pydantic Schemas"

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class BaseAuthorSchema(BaseModel):
    """
    Author base schema
    """
    name: str
    born_date: date

    class Config:
        orm_mode = True


class AuthorSchema(BaseAuthorSchema):
    """
    Schema for Author when adding a new Author
    """


class AuthorORMSchema(BaseAuthorSchema):
    """
    Schema for Author to be accessed by API Get request
    """
    id: int

    class Config:
        orm_mode = True


class BaseBookSchema(BaseModel):
    """
    Book base schema
    """
    name: str
    release_year: int
    author_id: int


class BookSchema(BaseBookSchema):
    """
    Schema for Book when adding a new Book
    """


class BookORMSchema(BaseBookSchema):
    """
    Schema for Book to be accessed by API Get request
    """
    id: int

    class Config:
        orm_mode = True

