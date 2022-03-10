from typing import Optional, Union, Any

from pydantic import BaseModel


class BaseSchemaModel(BaseModel):
    class Config:
        orm_mode = True


class OutPutSchemaModel(BaseModel):
    code: int = 0
    msg: Optional[str] = None
    data: Union[Any, None] = []
