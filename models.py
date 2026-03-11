
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


# ================= USERS TABLE =================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)

    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pincode = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)


# ================= QUICK REGISTER TABLE =================
class QuickRegister(Base):
    __tablename__ = "quick_register"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)


# ================= BOOKING TABLE =================
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    # customer details
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)

    # shoe details
    shoe_type = Column(String, nullable=False)
    custom_shoe_type = Column(String, nullable=True)
    shoe_size = Column(String, nullable=False)

    # issue
    issue_description = Column(String, nullable=False)

    # pickup schedule
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
