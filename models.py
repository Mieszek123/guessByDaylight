from sqlalchemy import Column, String, JSON
from database import Base

class Perk(Base):
    __tablename__ = "perks"

    # id to teraz String (np. "A_Nurse's_Calling")
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    side = Column(String)
    character = Column(String, nullable=True)
    description = Column(String)
    
    # SQLAlchemy potrafi automatycznie konwertować pythonowe listy na JSON w bazie
    categories = Column(JSON)
    
    # Zostawiam opcjonalne pole na ścieżkę do obrazka
    image_path = Column(String, nullable=True)