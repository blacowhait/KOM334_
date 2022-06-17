from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from classes.Buyer import Buyer, BuyerCreate
from database.db import get_db


router = APIRouter(
    prefix="/buyer",
    tags=['Buyer']
)


@router.get('/')
async def buyer_get_all(db: Session = Depends(get_db)):
    return Buyer.get_all(db)


@router.get('/{id}')
async def buyer_get_one(id: int, db: Session = Depends(get_db)):
    return Buyer.get_one(id, db)


@router.post('/')
async def buyer_create(request: BuyerCreate, response: Response, db: Session = Depends(get_db)):
    try:
        buyer = Buyer.create(request, db)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something Happened during creating Buyer")

    response.status_code = status.HTTP_201_CREATED
    return buyer


@router.put('/{id}')
async def buyer_update(id: int, request: BuyerCreate, db: Session = Depends(get_db)):
    return Buyer.update(id, request, db)


@router.delete('/{id}')
async def buyer_delete(id: int,  db: Session = Depends(get_db)):
    buyerid = Buyer.delete(id, db)
    return {"detail": f"Buyer with id {buyerid} successfully deleted"}
