import json
from database import SessionLocal
import models

def load_perks_to_db():
    db = SessionLocal()

    try:
        with open('perks.json', 'r', encoding='utf-8') as file:
            perks_data = json.load(file)
    except FileNotFoundError:
        print("Nie znaleziono pliku perks.json!")
        return

    # Zabezpieczenie: jeśli JSON okazałby się jednym obiektem (słownikiem) 
    # zamiast listą, pakujemy go w listę, żeby pętla zadziałała poprawnie.
    if isinstance(perks_data, dict):
        perks_data = [perks_data]

    added_count = 0

    for item in perks_data:
        # Zabezpieczenie: jeśli item nie jest słownikiem (np. jest stringiem), pomiń go
        if not isinstance(item, dict):
            continue

        # item.get("id") nie wywali błędu. Jeśli "id" nie istnieje, zwróci None.
        perk_id = item.get("id")
        
        if not perk_id:
            # Wypisujemy w konsoli, co dokładnie skrypt pominął
            print(f"Pominięto element w JSON (brak pola 'id'): {item.get('name', 'Brak nazwy')}")
            continue

        # Tutaj używamy bezpiecznej zmiennej perk_id
        existing_perk = db.query(models.Perk).filter(models.Perk.id == perk_id).first()
        
        if not existing_perk:
            db_perk = models.Perk(
                id=perk_id,
                name=item.get("name"),
                side=item.get("side"),
                character=item.get("character"),
                description=item.get("description"),
                categories=item.get("categories", [])
            )
            db.add(db_perk)
            added_count += 1

    db.commit()
    db.close()

    print(f"Gotowe! Dodano {added_count} nowych perków do bazy danych.")

if __name__ == "__main__":
    load_perks_to_db()