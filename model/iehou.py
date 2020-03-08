from pydantic import BaseModel


class IeHouBase(BaseModel):
    group: str = "某网"
    title: str
    publish_time: str
    content: str

class CreateIeHou(IeHouBase):
    pass


class IeHou(IeHouBase):
    id: int

    class Config:
        orm_mode = True