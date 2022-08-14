from webapps.posts import route_posts
from fastapi import APIRouter


router = APIRouter()
router.include_router(route_posts.router, prefix="", tags=["BlogFolio"])