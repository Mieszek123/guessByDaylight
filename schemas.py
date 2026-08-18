from pydantic import BaseModel

class PerkBase(BaseModel):
    id: str
    name: str
    side: str
    character: str | None = None
    description: str
    categories: list[str] = []
    
    # Opcjonalne pole na zdjęcie
    image_path: str | None = None

class PerkCreate(PerkBase):
    pass

class Perk(PerkBase):
    # Ponieważ dziedziczymy z PerkBase, to 'id' już tu jest.
    # Włączamy tylko czytanie z modeli ORM (SQLAlchemy).
    model_config = {"from_attributes": True}