from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.auth.schemas import UserCreate, User
from src.auth.models import User as DBUser
from src.auth.dependencies import get_db
from src.auth.service import create_user

router = APIRouter()

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
