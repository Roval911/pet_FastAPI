from decimal import Decimal

from pydantic import BaseModel, UUID4


class SDishBase(BaseModel):
    title: str
    description: str
    price: Decimal


class SDish(SDishBase):
    id: UUID4


class SDishCreate(SDishBase):
    pass


class SDishUpdate(SDishCreate):
    pass

