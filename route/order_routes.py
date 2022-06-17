from fastapi import APIRouter


router = APIRouter(
    prefix="/order",
    tags=['Order']
)


@router.get('/')
async def order_get_all():
    return {"Return": "Success"}


@router.get('/{id}')
async def order_get_one(id):
    return {"Return": "Success " + id}


@router.post('/')
async def order_create():
    return {"Return": "Success"}


@router.put('/{id}')
async def order_update(id):
    return {"Return": "Success " + id}


@router.delete('/{id}')
async def order_delete(id):
    return {"Return": "Success " + id}
