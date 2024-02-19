from fastapi import APIRouter, HTTPException, Response, Depends

from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dao import UserDAO
from users.dependencies import get_current_user
from users.models import User
from users.schemas import SUserRegister, SUserLogin

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


@router.post('/login')
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401)
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('access_token', access_token, httponly=True)
    return {'access_token': access_token}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('access_token')


@router.get('/me')
async def read_user(current_user: User = Depends(get_current_user)):
    return current_user
