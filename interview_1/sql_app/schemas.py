from typing import List

from pydantic import BaseModel

class UserBase(BaseModel):
    pincode: str

    class Config:
        orm_mode = True

class AddCreate(UserBase):
    address: str


class CityCreate(AddCreate):
    city: str
    
    class Config:
        orm_mode = True