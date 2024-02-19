from datetime import datetime

from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from config import settings
from users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="token")
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        pyload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=401, detail="JWTError")
    expire: str = pyload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail="exp")
    user_id: str = pyload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="userid")
    user = await UserDAO.get_by_id(str(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="user")
    return user