from fastapi import APIRouter
from submenu.dao import SubmenuDAO

router = APIRouter(
    prefix="/Submenus",
    tags=["Подменю"],
)


@router.get("/")
async def get_submenus():
    return await SubmenuDAO.get_all()
