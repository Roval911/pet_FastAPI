from database import Base
from sqlalchemy import Column, DECIMAL, UUID, ForeignKey


class Dish(Base):
    price = Column(DECIMAL, nullable=False)
    submenu_id = Column(UUID, ForeignKey("submenus.id"))