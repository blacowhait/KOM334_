from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from models.Order import Order, OrderCreate
from database.db import get_db

router = APIRouter(
    prefix="/order",
    tags=['Order']
)


@router.get('/')
async def order_get_all(db: Session = Depends(get_db)):
    return Order.get_all(db)


@router.get('/{id}')
async def order_get_one(id: int, db: Session = Depends(get_db)):
    return Order.get_one(id, db)


@router.post('/')
async def order_create(request: OrderCreate, response: Response, db: Session = Depends(get_db)):
    try:
        order = Order.create(request, db)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something Happened during creating Order")

    response.status_code = status.HTTP_201_CREATED
    return order


@router.put('/{id}')
async def order_update(id: int, request: OrderCreate, db: Session = Depends(get_db)):
    return Order.update(id, request, db)


@router.delete('/{id}')
async def order_delete(id: int,  db: Session = Depends(get_db)):
    orderid = Order.delete(id, db)
    return {"detail": f"Order with id {orderid} successfully deleted"}
