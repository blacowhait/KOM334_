import datetime
import enum
from typing import List
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Order_DB, get_db
from models.Buyer import Buyer
from models.Menu import Menu


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
    status: int
    total_price: int
    drink: list[int]
    food: list[int]
    buyer_id: int

    class Config:
        arbitrary_types_allowed = True


# ------------------------ Class


class Order():
    status: str
    total_price: int
    datetime: datetime.datetime
    drink: list[int]
    food: list[int]
    buyer: Buyer

    def get_all(db: Session = Depends(get_db)):
        orders = db.query(Order_DB).all()
        return orders

    # def get_one(id: int, db: Session = Depends(get_db)):
        # order = db.query(Order_DB).filter(Order_DB.id == id).first()
        # if not order:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #                         detail=f"Order with id {id} not found")

        # return order

    def create(request: OrderCreate, db: Session = Depends(get_db)):
        return request
        # order = Order_DB(
        #     status=ORDER_STATUS(request.status).name,
        #     buyer_id=request.buyer_id
        # )
        # db.add(order)
        # db.commit()
        # db.refresh(order)

        # return order

    # def update(id: int, request: OrderCreate, db: Session = Depends(get_db)):
        # order = db.query(Order_DB).filter(Order_DB.id == id).first()
        # if not order:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} not found")

        # order.status = ORDER_STATUS(request.status).name,
        # order.buyer_id = request.buyer_id
        # db.commit()
        # db.refresh(order)

        # return order

    # def delete(id: int,  db: Session = Depends(get_db)):
        # order = db.query(Order_DB).filter(Order_DB.id == id)
        # exist = order.first()
        # if not exist:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        # order.delete()
        # db.commit()

        # return id
