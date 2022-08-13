# main.py

from fastapi import FastAPI
from core.config import settings
from fastapi.staticfiles import StaticFiles

from routers import auth, post, user, vote, homepage


def include_router(app):
    app.include_router(auth.router)
    app.include_router(homepage.router)
    app.include_router(post.router)
    app.include_router(user.router)
    app.include_router(vote.router)

def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()


# @app.get("/") #remove this, It is no longer needed.
# def hello_api():
#     return {"msg":"Hello API"}
