from decimal import Decimal

from pydantic import BaseModel, UUID4


class SMenuBase(BaseModel):
    title: str
    description: str


class SMenu(SMenuBase):
    id: UUID4


class SMenuCreate(SMenuBase):
    pass


class SMenuUpdate(SMenuCreate):
    pass