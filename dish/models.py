from database import Base
from sqlalchemy import Column, DECIMAL, UUID, ForeignKey, String


class Dish(Base):
    price = Column(DECIMAL, nullable=False)
    submenu_id = Column(UUID, ForeignKey("submenus.id"))
    description = Column(String)