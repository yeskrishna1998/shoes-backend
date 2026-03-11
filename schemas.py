
from pydantic import BaseModel, EmailStr


# ===== USER REGISTER =====
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    address: str
    city: str
    state: str
    pincode: str


# ===== USER LOGIN =====
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ===== QUICK REGISTER =====
class QuickRegisterSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str


# ===== BOOKING CREATE =====
class BookingCreate(BaseModel):

    name: str
    email: EmailStr
    phone: str
    address: str

    shoeType: str
    customShoeType: str | None = None
    shoeSize: str

    issueDescription: str

    date: str
    time: str


# ===== BOOKING RESPONSE =====
class BookingResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    phone: str
    address: str

    shoe_type: str
    custom_shoe_type: str | None = None
    shoe_size: str

    issue_description: str

    date: str
    time: str

    class Config:
        from_attributes = True
