from pydantic import BaseModel

class PostBase(BaseModel):
    title: str

class PostCreate(PostBase):
    content: str
    
class Post(PostBase):
    id: int

    class Config:
        from_attributes = True