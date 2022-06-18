from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import Buyer_DB, get_db

# ------------------------ Schema


class BuyerCreate(BaseModel):
    name: str
    email: str
    whatsapp: str


# ------------------------ Class


class Buyer():
    name: str
    email: str
    whatsapp: str

    def get_all(db: Session = Depends(get_db)):
        buyers = db.query(Buyer_DB).all()
        return buyers

    def get_one(id: int, db: Session = Depends(get_db)):
        buyer = db.query(Buyer_DB).filter(Buyer_DB.id == id).first()
        if not buyer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Buyer with id {id} not found")

        return buyer

    def create(request: BuyerCreate, db: Session = Depends(get_db)):
        email_exist = db.query(Buyer_DB).filter(
            Buyer_DB.email == request.email).first()
        if email_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Buyer with email {request.email} already exists")

        buyer = Buyer_DB(
            name=request.name,
            email=request.email,
            whatsapp=request.whatsapp
        )
        db.add(buyer)
        db.commit()
        db.refresh(buyer)

        return {"message" : "Berhasil dibuat!"}

    def update(id: int, request: BuyerCreate, db: Session = Depends(get_db)):
        buyer = db.query(Buyer_DB).filter(Buyer_DB.id == id).first()
        if not buyer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        email_exist = db.query(Buyer_DB).filter(
            Buyer_DB.email == request.email).first()
        if email_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Buyer with email {request.email} already exists")

        buyer.name = request.name
        buyer.email = request.email
        buyer.whatsapp = request.whatsapp
        db.commit()
        db.refresh(buyer)

        return {"message" : "Berhasil diupdate!"}

    def delete(id: int,  db: Session = Depends(get_db)):
        buyer = db.query(Buyer_DB).filter(Buyer_DB.id == id)
        exist = buyer.first()
        if not exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Buyer with id {id} not found")

        buyer.delete()
        db.commit()

        return id

    def is_exist(id: int, db: Session = Depends(get_db)):
        buyer = db.query(Buyer_DB).filter(Buyer_DB.id == id).first()
        if not buyer:
            return False
        return True
