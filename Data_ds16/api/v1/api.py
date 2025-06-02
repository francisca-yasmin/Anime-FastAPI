from fastapi import APIRouter

from api.v1.endpoints import profissao

api_router = APIRouter()

#rota para buscar
api_router.include_router(profissao.router, prefix="/profissao", tags=["Profissão"]) #tags, pra separar no swagger