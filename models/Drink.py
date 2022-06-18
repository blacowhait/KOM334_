import enum
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Drink_DB, Order_Drink, get_db
from models.Menu import Menu


# ------------------------ Enum


class DRINK_CATEGORY(enum.Enum):
    coffee = 1
    tea = 2
    others = 3


class DRINK_TYPE(enum.Enum):
    hot = 1
    cold = 2


class DRINK_SIZE(enum.Enum):
    small = 1
    medium = 2
    large = 3


# ------------------------ Schema


class DrinkCreate(BaseModel):
    name: str
    description: str
    price: int
    category: int
    type: int
    size: int


# ------------------------ Class


class Drink(Menu):
    category: DRINK_CATEGORY
    type: DRINK_TYPE
    size: DRINK_SIZE

    def get_all(db: Session = Depends(get_db)):
        drinks = db.query(Drink_DB).all()
        return drinks

    def get_one(id: int, db: Session = Depends(get_db)):
        drink = db.query(Drink_DB).filter(Drink_DB.id == id).first()
        if not drink:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Drink with id {id} not found")

        return drink

    def get_by_order(order_id: int, db: Session = Depends(get_db)):
        order_drinks = db.query(Order_Drink).filter(
            Order_Drink.order_id == order_id).all()

        drinks = []
        for order_drink in order_drinks:
            drink = Drink.get_one(order_drink.drink_id, db)
            drinks.append(drink)

        return drinks

    def create(request: DrinkCreate, db: Session = Depends(get_db)):
        drink = Drink_DB(
            name=request.name,
            description=request.description,
            price=request.price,
            category=DRINK_CATEGORY(request.category).name,
            type=DRINK_TYPE(request.type).name,
            size=DRINK_SIZE(request.size).name
        )
        db.add(drink)
        db.commit()
        db.refresh(drink)

        return {"message" : "Berhasil dibuat!"}

    def update(id: int, request: DrinkCreate, db: Session = Depends(get_db)):
        drink = db.query(Drink_DB).filter(Drink_DB.id == id)
        exist = drink.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Drink with id {id} not found")

        drink.update(request.dict())
        db.commit()

        return {"message" : "Berhasil diupdate!"}

    def delete(id: int,  db: Session = Depends(get_db)):
        drink = db.query(Drink_DB).filter(Drink_DB.id == id)
        exist = drink.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        drink.delete()
        db.commit()

        return {"message" : "Berhasil dihapus!"}

    def is_exist(id: int, db: Session = Depends(get_db)):
        exist = db.query(Drink_DB).filter(Drink_DB.id == id).first()
        if not exist:
            return False
        return True
