from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    address: str
    city: str
    state: str
    pincode: str