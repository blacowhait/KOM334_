from fastapi import APIRouter


router = APIRouter(
    prefix="/food",
    tags=['Food']
)


@router.get('/')
async def food_get_all():
    return {"Return": "Success"}


@router.get('/{id}')
async def food_get_one(id):
    return {"Return": "Success " + id}


@router.post('/')
async def food_create():
    return {"Return": "Success"}


@router.put('/{id}')
async def food_update(id):
    return {"Return": "Success " + id}


@router.delete('/{id}')
async def food_delete(id):
    return {"Return": "Success " + id}
