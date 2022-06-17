from fastapi import FastAPI
from dotenv import load_dotenv
from route import menu_routes, food_routes, drink_routes, order_routes, buyer_routes

load_dotenv()

app = FastAPI()


@app.get('/')
async def index():
    return "Hello! Welcome to Shop."

app.include_router(menu_routes.router)
app.include_router(food_routes.router)
app.include_router(drink_routes.router)
app.include_router(order_routes.router)
app.include_router(buyer_routes.router)
