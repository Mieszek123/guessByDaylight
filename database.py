import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Na Railway ustawi się zmienna DATABASE_URL (Postgres).
# Lokalnie jej nie ma, więc leci domyślny fallback na Twój SQLite.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dbddle.db")

# Railway daje URL zaczynający się od "postgres://", a SQLAlchemy 2.x
# wymaga "postgresql://" - trzeba podmienić prefix.
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# connect_args jest potrzebne TYLKO dla SQLite, Postgres go nie chce
connect_args = (
    {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()