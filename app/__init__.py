from fastapi import  FastAPI, Depends, Request
from fastapi.responses import HTMLResponse

from .dependencies import get_query_token, get_token_header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .db import SessionLocal, engine
from app.Service.tasks import task_router
app = FastAPI(dependencies=[Depends(get_query_token)])
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

origin = [
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins =origin,
    allow_credentials =True,
    allow_methods =["*"],
    allow_headers=["*"]
)
app.include_router(task_router, prefix='/celerytask')

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()
@app.get('/', response_class=HTMLResponse)
async def index(request: Request, token: str = None):
    return templates.TemplateResponse(request=request, name='index.html')



