from sqlalchemy.orm import Session
from .models import Post
from .schemas import PostCreate


def create(db: Session, post: PostCreate):
  try:
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
  except Exception as e:
    raise e