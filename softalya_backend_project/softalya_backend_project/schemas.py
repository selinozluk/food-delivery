from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class AddressBase(BaseModel):
    street: str
    city: str

class AddressCreate(AddressBase):
    pass

class CategoryBase(BaseModel):
    name: str
    description: str

class ProductBase(BaseModel):
    name: str
    price: int
    description: str
