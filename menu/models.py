from sqlalchemy import Column, String

from database import Base


class Menu(Base):
    description = Column(String)
