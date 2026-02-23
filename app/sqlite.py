"""This module sets up the SQLite database connection using SQLAlchemy, defines the base class for models,
 and configures the session maker for database interactions."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_url = "sqlite:///./sqlite.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()