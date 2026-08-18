from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Importujemy nasze pliki
import models
import schemas
from database import SessionLocal, engine

# Tworzy tabele w bazie (jeśli jeszcze nie istnieją)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Zależność - otwiera i zamyka sesję bazy przy każdym zapytaniu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Tutaj używamy schemas.Perk żeby FastAPI wiedziało jak mają wyglądać dane na wyjściu
@app.get("/perks", response_model=list[schemas.Perk])
def get_perks(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    # Pobieramy perki z bazy za pomocą modelu SQLAlchemy
    perks = db.query(models.Perk).offset(skip).limit(limit).all()
    return perks

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="static", html=True), name="static")