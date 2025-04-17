from pydantic import BaseModel
from typing import Optional


class Notes(BaseModel):
    title: str
    content: str

class CreateNote(BaseModel):
    title: str
    content: str

class registerUser(BaseModel):
    name: str
    email: str
    password: str
        
class DataUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None