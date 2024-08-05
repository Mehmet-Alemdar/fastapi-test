from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserLogin
from .utils import get_password_hash, verify_password

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, user: UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return db_user
    