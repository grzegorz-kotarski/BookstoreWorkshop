"Database models"
from sqlalchemy import (Index,
                        String,
                        Column,
                        Integer,
                        ForeignKey,
                        BigInteger,
                        Boolean,
                        Date)
from sqlalchemy.orm import relationship
from .manager import Base


class Author(Base):
    """
    Author database table model class.
    """
    __tablename__ = 'author'
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    born_date = Column(Date)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id='{self.id}', born='{self.born_date}' name='{self.name}')>"


class Book(Base):
    """
    Book database table model class.
    """
    __tablename__ = 'book'
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    release_year = Column(Integer)
    author_id = Column(BigInteger, ForeignKey('author.id'))
    author = relationship("Author", back_populates="books")
   
    __table_args__ = (
            Index('uix_author_book_name', 'author_id', 'name', unique=True),
    )

    def __repr__(self):
        return f"<Book(id='{self.id}', name='{self.name} pages={self.release_year} author={self.author.name}')>"

