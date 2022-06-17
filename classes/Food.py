import enum
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Food_DB, get_db
from classes.Menu import Menu


# ------------------------ Enum


class FOOD_CATEGORY(enum.Enum):
    main_course = 1
    dessert = 2
    appetizer = 3
    others = 4


# ------------------------ Schema


class FoodCreate(BaseModel):
    name: str
    description: str
    price: int
    category: int


# ------------------------ Class


class Food(Menu):
    category: FOOD_CATEGORY

    def get_all(db: Session = Depends(get_db)):
        foods = db.query(Food_DB).all()
        return foods

    def get_one(id: int, db: Session = Depends(get_db)):
        food = db.query(Food_DB).filter(Food_DB.id == id).first()
        if not food:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Drink with id {id} not found")

        return food

    def create(request: FoodCreate, db: Session = Depends(get_db)):
        food = Food_DB(
            name=request.name,
            description=request.description,
            price=request.price,
            category=FOOD_CATEGORY(request.category).name,
        )
        db.add(food)
        db.commit()
        db.refresh(food)

        return food

    def update(id: int, request: FoodCreate, db: Session = Depends(get_db)):
        food = db.query(Food_DB).filter(Food_DB.id == id).first()
        if not food:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Drink with id {id} not found")

        food.name = request.name,
        food.description = request.description,
        food.price = request.price,
        food.category = FOOD_CATEGORY(request.category).name,
        print("1")
        db.commit()
        print("2")
        db.refresh(food)
        print("3")

        return food

    def delete(id: int,  db: Session = Depends(get_db)):
        food = db.query(Food_DB).filter(Food_DB.id == id)
        exist = food.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        food.delete()
        return id
