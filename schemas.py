from pydantic import BaseModel, EmailStr


# Register Schema
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    address: str
    city: str
    state: str
    pincode: str


# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str