from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password hash (Register ke time use hoga)
def hash_password(password: str):
    return pwd_context.hash(password)


# Password verify (Login ke time use hoga)
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)