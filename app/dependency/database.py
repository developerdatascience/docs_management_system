"""Create a Sqllite database  with session"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./documentmanagentsystem.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    """Connects to database

    Yields:
        _type_: database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
