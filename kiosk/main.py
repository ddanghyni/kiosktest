from fastapi import FastAPI 
from starlette.middleware.cors import CORSMiddleware
from database import engine
#from models import coffee
from domin.meun import meun_router


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(meun_router.router)
