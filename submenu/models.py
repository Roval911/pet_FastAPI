from database import Base
from sqlalchemy import Column, ForeignKey, UUID


class Submenu(Base):
    menu_id = Column(UUID, ForeignKey("menus.id"))
