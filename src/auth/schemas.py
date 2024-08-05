from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    
class UserLogin(UserBase):
    password: str
    
class LoginAndRegisterResponseDetail(BaseModel):
    access_token: str
    email: str

class LoginAndRegisterResponse(BaseModel):
    status_code: int
    detail: LoginAndRegisterResponseDetail
    headers: Optional[dict] = None

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True
