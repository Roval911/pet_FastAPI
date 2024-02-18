from sqlalchemy import Column, String, Integer

from database import Base


class User(Base):
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)