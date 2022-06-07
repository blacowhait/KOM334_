from fastapi import FastAPI

from schema import CoffeeSchema

app = FastAPI()


@app.get('/')
async def index():
    return "Hello! Welcome to Coffee Shop."


@app.get('/coffee')
async def get_all_coffees():
    # coffee.read_all()
    pass


@app.get('/coffee/{id}')
async def get_coffee(id):
    # coffee.read_one()
    pass


@app.post('/coffee')
async def add_coffee(coffee: CoffeeSchema):
    # coffee.create()
    pass


@app.put('/coffee/{id}')
async def add_coffee(id):
    # coffee.create()
    pass


@app.delete('/coffee/{id}')
async def delete_coffee(id):
    # coffee.delete()
    pass
