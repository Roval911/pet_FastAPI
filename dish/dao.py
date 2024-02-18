from dao.base import BaseDAO
from dish.models import Dish


class DishDAO(BaseDAO):
    model = Dish