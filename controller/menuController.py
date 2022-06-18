from fastapi import APIRouter

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.Menu import Menu
from database.db import get_db


router = APIRouter(
    prefix="/menu",
    tags=['Menu']
)


@router.get('/')
async def buyer_get_all(db: Session = Depends(get_db)):
    return Menu.get_all(db)
