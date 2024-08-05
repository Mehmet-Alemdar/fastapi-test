from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserLogin
from .utils import get_password_hash, verify_password, create_access_token

def create_user(db: Session, user: UserCreate):
    try:
        db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        access_token = create_access_token(data={"sub": db_user.email}, expires_delta=15)

        return HTTPException(status_code=201, detail={"access_token": access_token, "email": db_user.email})
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while creating the user")

def login_user(db: Session, user: UserLogin):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        
        access_token = create_access_token(data={"sub": db_user.email}, expires_delta=15)

        return HTTPException(status_code=200, detail={"access_token": access_token, "email": db_user.email})
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while logging in the user")
    