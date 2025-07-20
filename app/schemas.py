from pydantic import BaseModel, Field
from typing import Optional
import datetime

def current_year():
    return datetime.datetime.now().year

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., ge=0, le=current_year())
    summary: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True 