import enum
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Food_DB, Order_Food, get_db
from models.Menu import Menu


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

    def get_by_order(order_id: int, db: Session = Depends(get_db)):
        order_foods = db.query(Order_Food).filter(
            Order_Food.order_id == order_id).all()

        foods = []
        for order_food in order_foods:
            food = Food.get_one(order_food.food_id, db)
            foods.append(food)

        return foods

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
        food = db.query(Food_DB).filter(Food_DB.id == id)
        exist = food.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Drink with id {id} not found")

        food.update(request.dict())
        db.commit()

        return food.first()

    def delete(id: int,  db: Session = Depends(get_db)):
        food = db.query(Food_DB).filter(Food_DB.id == id)
        exist = food.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        food.delete()
        db.commit()

        return id

    def is_exist(id: int, db: Session = Depends(get_db)):
        exist = db.query(Food_DB).filter(Food_DB.id == id).first()
        if not exist:
            return False
        return True
