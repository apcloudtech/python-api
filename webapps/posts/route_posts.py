from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from routers.routers.post import get_posts, get_post
from database import get_db



templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request,db: Session = Depends(get_db)):
    posts = get_posts(db=db)
    return templates.TemplateResponse(
        "general_pages/index.html", {"request": request,"posts":posts}
    )

@router.get("/posts/{id}")             #new
def post_details(id:int,request: Request,db:Session = Depends(get_db)):    
    post = get_post(id=id, db=db)
    return templates.TemplateResponse(
        "posts/detail.html", {"request": request,"post":post}
    )