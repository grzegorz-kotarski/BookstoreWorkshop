"""
Database management and initialization.
"""
from functools import lru_cache
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

@lru_cache
def get_engine():
    db_url = os.environ.get('WORKSHOP_DB_URL')
    engine = create_engine(db_url)
    return engine

@lru_cache
def get_local_session():
    engine = get_engine()
    return sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_db_tables():
    "Create database tables if not exist"
    engine = get_engine()
    Base.metadata.create_all(bind=engine)

