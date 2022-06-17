from fastapi import Depends
from sqlalchemy.orm import Session
from database.db import Drink_DB, Food_DB, get_db


class Menu():
    name: str
    description: str
    price: int

    def get_all(db: Session = Depends(get_db)):
        foods = db.query(Food_DB).all()
        drinks = db.query(Drink_DB).all()
        return {
            "foods": foods,
            "drinks": drinks
        }
