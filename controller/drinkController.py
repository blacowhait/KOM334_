from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from models.Drink import Drink, DrinkCreate
from database.db import get_db


router = APIRouter(
    prefix="/drink",
    tags=['Drink']
)


@router.get('/')
async def buyer_get_all(db: Session = Depends(get_db)):
    return Drink.get_all(db)


@router.get('/{id}')
async def buyer_get_one(id: int, db: Session = Depends(get_db)):
    return Drink.get_one(id, db)


@router.post('/')
async def buyer_create(request: DrinkCreate, response: Response, db: Session = Depends(get_db)):
    try:
        buyer = Drink.create(request, db)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something Happened during creating Drink")

    response.status_code = status.HTTP_201_CREATED
    return buyer


@router.put('/{id}')
async def buyer_update(id: int, request: DrinkCreate, db: Session = Depends(get_db)):
    return Drink.update(id, request, db)


@router.delete('/{id}')
async def buyer_delete(id: int,  db: Session = Depends(get_db)):
    drinkid = Drink.delete(id, db)
    return {"detail": f"Drink with id {drinkid} successfully deleted"}
