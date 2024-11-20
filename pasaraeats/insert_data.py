import json
from sqlalchemy.orm import Session
from pasaraeats.database import engine, SessionLocal
from pasaraeats.models import Card
from pasaraeats.cards_data import cards  # Ensure this matches your file name

def insert_data():
    db = SessionLocal()
    for card in cards:
        card_data = {
            "user_id": card["user_id"],
            "containers": card["containers"],  # Use card["containers"] directly
            "location": card["location"],
            "order_type": card["order_type"]
        }
        db_card = Card(**card_data)
        db.add(db_card)
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_data()
