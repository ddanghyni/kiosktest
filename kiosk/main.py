from fastapi import FastAPI 
from starlette.middleware.cors import CORSMiddleware
from domain.menu import menu_router
from domain.orderer import orderer_router
from domain.order import order_router
from domain.recommendation import menu_reco
from domain.face_detect import face_detect_router


#

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



app.include_router(menu_router.router)
app.include_router(orderer_router.router)
app.include_router(order_router.router)
app.include_router(menu_reco.router)
app.include_router(face_detect_router.router)