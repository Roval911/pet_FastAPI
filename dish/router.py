from fastapi import APIRouter
from dish.dao import DishDAO


router = APIRouter(
    prefix="/dishs",
    tags=["Блюда"],
)


@router.get("/")
async def get_dishes():
    return await DishDAO.get_all()
