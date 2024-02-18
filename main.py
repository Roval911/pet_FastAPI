from fastapi import FastAPI
from dish.router import router as dish_router
from menu.router import router as menu_router
from submenu.router import router as submenu_router
from users.router import router as users_router

app = FastAPI()

app.include_router(menu_router)
app.include_router(submenu_router)
app.include_router(dish_router)
app.include_router(users_router)

