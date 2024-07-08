from pydantic import BaseModel
from typing import Dict

class PostbackBase(BaseModel):
    hash_id: str
    data: Dict

class PostbackCreate(PostbackBase):
    pass

class Postback(PostbackBase):
    class Config:
        orm_mode = True
