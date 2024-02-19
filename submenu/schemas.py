from pydantic import BaseModel, UUID4


class SSubMenuBase(BaseModel):
    title: str
    description: str


class SSubMenu(SSubMenuBase):
    id: UUID4


class SSubMenuCreate(SSubMenuBase):
    pass


class SSubMenuUpdate(SSubMenuCreate):
    pass
