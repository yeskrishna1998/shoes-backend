from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import User, QuickRegister, Booking
from schemas import UserRegister, UserLogin, QuickRegisterSchema, BookingCreate
from auth import hash_password, verify_password
from fastapi.middleware.cors import CORSMiddleware


# ================= CREATE TABLES =================
Base.metadata.create_all(bind=engine)

app = FastAPI()


# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ================= DATABASE SESSION =================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ================= FULL REGISTER =================
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pwd = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password=hashed_pwd,
        address=user.address,
        city=user.city,
        state=user.state,
        pincode=user.pincode
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.id}


# ================= LOGIN =================
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email
        }
    }


# ================= QUICK REGISTER =================
@app.post("/quick-register")
def quick_register(user: QuickRegisterSchema, db: Session = Depends(get_db)):

    new_user = QuickRegister(
        name=user.name,
        email=user.email,
        phone=user.phone,
        address=user.address
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Quick registration successful", "id": new_user.id}


# ================= BOOKING API =================
@app.post("/booking")
def create_booking(data: BookingCreate, db: Session = Depends(get_db)):

    booking = Booking(
        name=data.name,
        email=data.email,
        phone=data.phone,
        address=data.address,
        shoe_type=data.shoeType,
        custom_shoe_type=data.customShoeType,
        shoe_size=data.shoeSize,
        issue_description=data.issueDescription,
        date=data.date,
        time=data.time
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return {"message": "Booking successful", "booking_id": booking.id}


# ================= GET ALL BOOKINGS =================
@app.get("/bookings")
def get_bookings(db: Session = Depends(get_db)):

    return db.query(Booking).all()


# ================= GET ALL USERS =================
@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):

    return db.query(User).all()


# ================= GET QUICK REGISTRATIONS =================
@app.get("/quick-registrations")
def get_quick_registrations(db: Session = Depends(get_db)):

    return db.query(QuickRegister).all()
