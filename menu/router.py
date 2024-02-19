from fastapi import APIRouter
from menu.dao import MenuDAO

router = APIRouter(
    prefix="/Menus",
    tags=["Меню"],
)


@router.get("/")
async def get_menus():
    return await MenuDAO.get_all()
