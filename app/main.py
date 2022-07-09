from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
# no longer needed after implementing alembic. was used to build tables in postgres.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
# https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers: https://www.fastapitutorial.com/blog/fastapi-route/
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "this comes from the ci/cd pipeline!"}
