# main.py
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from fastapi import FastAPI
from core.config import settings
from fastapi.staticfiles import StaticFiles
from webapps.base import router as web_app_router
from routers.base import router

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def include_router(app):
    app.include_router(router)
    app.include_router(web_app_router)


def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    include_router(app)
    configure_static(app)
    return app


start = start_application()


# @app.get("/") #remove this, It is no longer needed.
# def hello_api():
#     return {"msg":"Hello API"}
