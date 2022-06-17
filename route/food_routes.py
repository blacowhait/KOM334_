from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from classes.Food import Food, FoodCreate
from database.db import get_db


router = APIRouter(
    prefix="/food",
    tags=['Food']
)


@router.get('/')
async def buyer_get_all(db: Session = Depends(get_db)):
    return Food.get_all(db)


@router.get('/{id}')
async def buyer_get_one(id: int, db: Session = Depends(get_db)):
    return Food.get_one(id, db)


@router.post('/')
async def buyer_create(request: FoodCreate, response: Response, db: Session = Depends(get_db)):
    try:
        buyer = Food.create(request, db)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something Happened during creating Food")

    response.status_code = status.HTTP_201_CREATED
    return buyer


@router.put('/{id}')
async def buyer_update(id: int, request: FoodCreate, db: Session = Depends(get_db)):
    return Food.update(id, request, db)


@router.delete('/{id}')
async def buyer_delete(id: int,  db: Session = Depends(get_db)):
    drinkid = Food.delete(id, db)
    return {"detail": f"Food with id {drinkid} successfully deleted"}
