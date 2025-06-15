from fastapi import FastAPI
from app.routes import router
from contextlib import asynccontextmanager
from app.config import Base, engine

# ciclo de vida da api, cria a tabela de cache no banco caso n exista ainda ao abrir ela
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("abrindo esta bomba")
    yield
    print("fechando esta bomba")
    
app = FastAPI(lifespan=lifespan)
app.include_router(router)