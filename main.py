from fastapi import FastAPI
from controller import buyerController, drinkController, foodController, menuController, orderController

app = FastAPI()


@app.get('/')
async def index():
    return "Hello! Welcome to Shop."

app.include_router(menuController.router)
app.include_router(foodController.router)
app.include_router(drinkController.router)
app.include_router(orderController.router)
app.include_router(buyerController.router)
