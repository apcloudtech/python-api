# main.py

from fastapi import FastAPI
from core.config import settings
from routers.homepage import general_pages_router
from routers import auth, post, user, vote


def include_router(app):
    app.include_router(auth.router)
    app.include_router(general_pages_router)
    app.include_router(post.router)
    app.include_router(user.router)
    app.include_router(vote.router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_application()


# @app.get("/") #remove this, It is no longer needed.
# def hello_api():
#     return {"msg":"Hello API"}
