from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime, default=func.now())
    