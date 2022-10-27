"Database operations"
from sqlalchemy.orm import Session
from .manager import (
    get_local_session,
)
from .model import (
    Book,
    Author
)
from .schemas import AuthorSchema, BookSchema


def get_db_session():
    "Create and yield database session instance."
    session_local = get_local_session()
    db_session = session_local()
    try:
        yield db_session
    finally:
        db_session.close()


def commit_or_rollback(db_session):
    "Commit transaction, rollback on exception"
    try:
        db_session.commit()
    except Exception:
        db_session.rollback()
        raise


def get_books(db_session: Session, author_id: int, skip: int = 0, limit: int = 100):
    "Get books for given author_id starting specified offset and limited by given limit."
    return db_session.query(Book).filter(Book.author_id==author_id).offset(skip).limit(limit).all()


def get_authors(db_session: Session, skip: int = 0, limit: int = 100):
    "Get books starting specified offset and limited by given limit."
    return db_session.query(Author).offset(skip).limit(limit).all()


def add_author(db_session: Session, author_schema: AuthorSchema) -> Author:
    """
    Find Project instance or create new if not found.
    """
    print(author_schema)
    author = Author(name=author_schema.name, born_date=author_schema.born_date)
    db_session.add(author)
    commit_or_rollback(db_session)
    return author


def add_book(db_session: Session, book_schema: BookSchema) -> Book:
    """
    Find Project instance or create new if not found.
    """
    print(book_schema)
    book = Book(name=book_schema.name, author_id=book_schema.author_id, release_year=book_schema.release_year)
    db_session.add(book)
    commit_or_rollback(db_session)
    return book



