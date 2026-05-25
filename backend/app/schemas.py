from pydantic import BaseModel

class UserCreate(BaseModel):
    phone: str
    password: str