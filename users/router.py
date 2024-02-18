from fastapi import APIRouter, HTTPException

from users.auth import get_password_hash
from users.dao import UserDAO
from users.schemas import SUserRegister

router = APIRouter(
    prefix="/Users",
    tags=["Поьзователи"],
)

router.post('/auth')


@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail='Пользователь с таким email уже существует')
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, title=user_data.title, hashed_password=hashed_password)
