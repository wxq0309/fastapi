from pydantic import BaseModel


class UriLinkBase(BaseModel):
    real_link: str


class CreateUriLink(UriLinkBase):
    pass


class UriLink(UriLinkBase):
    id: int
    short_link: str = "127.0.0.1:8000/ulink/lts/"

    class Config:
        orm_mode = True
