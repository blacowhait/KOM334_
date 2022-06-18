import enum
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Order_DB, Order_Drink, Order_Food, get_db
from models.Buyer import Buyer
from models.Food import Food
from models.Drink import Drink


# ------------------------ Enum

class ORDER_STATUS(enum.Enum):
    pending = 1
    waiting = 2
    processing = 3
    done = 4


# ------------------------ Schema


class OrderMenu():
    menu_class: str
    menu_id: int


class OrderCreate(BaseModel):
    total_price: int
    drinks: list[int]
    foods: list[int]
    buyer_id: int

    class Config:
        arbitrary_types_allowed = True


class OrderUpdate(BaseModel):
    status: int
    total_price: int
    drinks: list[int]
    foods: list[int]
    buyer_id: int

    class Config:
        arbitrary_types_allowed = True


# ------------------------ Class


class Order():
    status: str
    total_price: int
    drink: list[int]
    food: list[int]
    buyer: Buyer

    def get_all(db: Session = Depends(get_db)):
        orders = db.query(Order_DB).all()
        for order in orders:
            order.buyer = Buyer.get_one(order.buyer_id, db)
            order.foods = Food.get_by_order(order.id, db)
            order.drinks = Drink.get_by_order(order.id, db)
        return orders

    def get_one(id: int, db: Session = Depends(get_db)):
        order = db.query(Order_DB).filter(Order_DB.id == id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Order with id {id} not found")

        order.buyer = Buyer.get_one(order.buyer_id, db)
        order.foods = Food.get_by_order(order.id, db)
        order.drinks = Drink.get_by_order(order.id, db)

        return order

    def create(request: OrderCreate, db: Session = Depends(get_db)):
        exist = Buyer.is_exist(request.buyer_id, db)
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {request.buyer_id} not found")

        for id in request.foods:
            exist = Food.is_exist(id, db)
            if not exist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=f"Food with id {id} not found")

        for id in request.drinks:
            exist = Drink.is_exist(id, db)
            if not exist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail=f"Drink with id {id} not found")

        order = Order_DB(
            status=ORDER_STATUS(1).name,
            total_price=request.total_price,
            buyer_id=request.buyer_id
        )
        db.add(order)
        db.commit()
        db.refresh(order)

        for id in request.foods:
            food = Order_Food(order_id=order.id, food_id=id)
            db.add(food)
            db.commit()

        for id in request.drinks:
            drink = Order_Drink(order_id=order.id, drink_id=id)
            db.add(drink)
            db.commit()

        return Order.get_one(order.id, db)

    def update(id: int, request: OrderUpdate, db: Session = Depends(get_db)):
        order = db.query(Order_DB).filter(Order_DB.id == id)
        exist = order.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} not found")

        request.status = ORDER_STATUS(request.status).name

        food = db.query(Order_Food).filter(Order_Food.order_id == exist.id)
        food.delete()
        drink = db.query(Order_Drink).filter(Order_Drink.order_id == exist.id)
        drink.delete()

        order.update({
            "status": request.status,
            "total_price": request.total_price,
            "buyer_id": request.buyer_id,
        })
        db.commit()

        for id in request.foods:
            food = Order_Food(order_id=exist.id, food_id=id)
            db.add(food)
            db.commit()

        for id in request.drinks:
            drink = Order_Drink(order_id=exist.id, drink_id=id)
            db.add(drink)
            db.commit()

        return Order.get_one(exist.id, db)

    def update_status(id: int, request: int, db: Session = Depends(get_db)):
        order = db.query(Order_DB).filter(Order_DB.id == id)
        exist = order.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} not found")

        request = ORDER_STATUS(request).name
        order.update({"status": request})
        db.commit()

        return Order.get_one(exist.id, db)

    def delete(id: int,  db: Session = Depends(get_db)):
        order = db.query(Order_DB).filter(Order_DB.id == id)
        exist = order.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        order.delete()
        food = db.query(Order_Food).filter(Order_Food.order_id == exist.id)
        food.delete()
        drink = db.query(Order_Drink).filter(Order_Drink.order_id == exist.id)
        drink.delete()
        db.commit()

        return id
