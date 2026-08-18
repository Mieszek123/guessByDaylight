from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Plik bazy danych stworzy się w tym samym folderze
SQLALCHEMY_DATABASE_URL = "sqlite:///./dbddle.db"

# connect_args jest potrzebne tylko dla bazy SQLite w FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()