from fastapi import  FastAPI, Depends
from .dependencies import get_query_token, get_token_header
from fastapi.middleware.cors import CORSMiddleware
from .db import SessionLocal, engine
from app.Service.tasks import task_router
app = FastAPI(dependencies=[Depends(get_query_token)])
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
@app.get('/')
async def index(token: str = None):
    return [{"message" : "this is the index page for FastAPI web application"}]



