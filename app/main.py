from fastapi import FastAPI
from app.routes import router
from contextlib import asynccontextmanager
from app.config import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# ciclo de vida da api, cria a tabela de cache no banco caso n exista ainda ao abrir ela
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("abrindo esta bomba")
    yield
    print("fechando esta bomba")
    
app = FastAPI(lifespan=lifespan)
app.include_router(router)

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:5500/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)