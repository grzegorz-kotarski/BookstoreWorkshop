"Bookstore Application Service for Intel@PUT workshop"
import logging
from typing import List
from fastapi import Depends, FastAPI
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from .schemas import (
    AuthorORMSchema,
    AuthorSchema,
    BookORMSchema,
    BookSchema
)
from .db import (
    get_local_session,
    get_authors,
    get_books,
    add_author,
    add_book,
)

__version__ = '0.1.0'
app = FastAPI()


def get_db_session():
    "Yield new session instance"
    local_session = get_local_session()
    db_session = local_session()
    try:
        yield db_session
    finally:
        db_session.close()

 
@app.get(f"/api/authors", response_model=List[AuthorORMSchema])
async def api_get_projects(db_session: Session = Depends(get_db_session), skip: int=0, limit: int=100):
    "Return payload for given configuration name"
    return get_authors(db_session, skip=skip, limit=limit)


@app.get(f"/api/books/{{author_id}}", response_model=List[BookORMSchema])
async def api_get_measurements(author_id: int, db_session: Session = Depends(get_db_session), skip: int=0, limit: int=100):
    "Return payload for given configuration name"
    return get_books(db_session, author_id, skip=skip, limit=limit)

@app.post(f"/api/author", response_model=AuthorORMSchema)
async def api_add_author(author_data: AuthorSchema, db_session: Session = Depends(get_db_session)):
    "Return payload for given configuration name"
    return add_author(db_session, author_data)

@app.post(f"/api/book", response_model=BookORMSchema)
async def api_add_book(book_data: BookSchema, db_session: Session = Depends(get_db_session)):
    "Return payload for given configuration name"
    return add_book(db_session, book_data)




# @app.get(f"/api/{SERVICE_API_VERSION}/files/{{measurement}}", response_model=List[FileORMSchema])
# async def api_get_files(measurement: int, db_session: Session = Depends(get_db_session), skip: int=0, limit: int=100):
#     "Return payload for given configuration name"
#     return get_files(db_session, measurement, skip=skip, limit=limit)


# @app.post(f"/api/{SERVICE_API_VERSION}/file")
# async def api_add_file(file_model: FileSchema, db_session: Session = Depends(get_db_session)):
#     "Return payload for given configuration name"
#     add_file(db_session, file_model)


# @app.post(f"/api/{SERVICE_API_VERSION}/files")
# async def api_add_files(files_model: FilesSchema, db_session: Session = Depends(get_db_session)):
#     "Return payload for given configuration name"
#     return add_files(db_session, files_model)


@app.get("/", response_class=PlainTextResponse)
async def root():
    "Return name and version"
    return f'{__doc__} ver.{__version__}'
