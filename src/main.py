from fastapi import FastAPI
from .auth.router import router as auth_router
from .posts.router import router as posts_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(posts_router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL"}
