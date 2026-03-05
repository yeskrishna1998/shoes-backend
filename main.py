from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import User
from schemas import UserRegister
from auth import hash_password
from fastapi.middleware.cors import CORSMiddleware

# Create tables (with error handling)
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"⚠️ Database connection failed: {str(e)[:100]}")
    print("Continuing - the database will try to connect when needed")

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register API
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already exists")

        # bcrypt has a maximum input length of 72 bytes; enforce it here
        if len(user.password.encode('utf-8')) > 72:
            raise HTTPException(status_code=400, detail="Password too long (max 72 bytes)")
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
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")