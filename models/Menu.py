import enum
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Drink_DB, Food_DB, get_db


class Menu():
    name: str
    description: str
    price: int

    def get_all(db: Session = Depends(get_db)):
        foods = db.query(Food_DB).all()
        drink = db.query(Drink_DB).all()
        return {
            "foods": foods,
            "drink": drink
        }
