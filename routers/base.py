from routers.routers import auth, post, user, vote 
from fastapi import APIRouter


router = APIRouter()
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(post.router)
router.include_router(vote.router)                                                   