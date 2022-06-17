from fastapi import APIRouter


router = APIRouter(
    prefix="/menu",
    tags=['Menu']
)


@router.get('/')
async def menu_get_all():
    return {"Return": "Success"}


@router.get('/{id}')
async def menu_get_one(id):
    return {"Return": "Success " + id}
