from passlib.context import CryptContext
from fastapi import HTTPException
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: int) -> str:
    to_encode = data.copy()
    return "fake_access"

def verify_token():
    # raise HTTPException(status_code=401, detail="Invalid token")
    pass