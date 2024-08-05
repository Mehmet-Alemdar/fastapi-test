from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.posts.schemas import Post, PostCreate
from src.posts.dependencies import get_db
from src.posts.service import create
from src.auth.utils import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])

@router.get("/get_posts")
def get_posts():
    try:
        posts = {"id": 1, "titl": "Hello, World!", "content": "This is a test post."}
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
      

@router.post("/create_post")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    try:
        return create(db=db, post=post)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An dfdfdfdfdf occurred: {str(e)}")