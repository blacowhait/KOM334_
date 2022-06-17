from fastapi import APIRouter


router = APIRouter(
    prefix="/drink",
    tags=['Drink']
)


@router.get('/')
async def drink_get_all():
    return {"Return": "Success"}


@router.get('/{id}')
async def drink_get_one(id):
    return {"Return": "Success " + id}


@router.post('/')
async def drink_create():
    return {"Return": "Success"}


@router.put('/{id}')
async def drink_update(id):
    return {"Return": "Success " + id}


@router.delete('/{id}')
async def drink_delete(id):
    return {"Return": "Success " + id}
