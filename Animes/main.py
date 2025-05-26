from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json

app = FastAPI()

ARQUIVO_DB = 'animes.json' #nome do json onde está sendo salvo os animes

#salvar os animes em um json
def carregar_animes():
    try:
        with open(ARQUIVO_DB, "r", encoding="utf-8") as a:
            return json.load(a)
    except FileNotFoundError:
        return {}

def salvar_animes(db):
    with open(ARQUIVO_DB, "w", encoding="utf-8") as a:
        json.dump(db, a, indent=4, ensure_ascii=False)

# Carrega animes do arquivo
anime_db = carregar_animes()

class Anime(BaseModel):
    titulo: str
    categoria: str
    episodios: int

# Listar todos os animes
@app.get("/animes/")
async def get_all_animes():
    return anime_db

# Buscar anime por ID
@app.get("/animes/{anime_id}")
async def read_anime(anime_id: int):
    anime = anime_db.get(str(anime_id))
    if anime:
        return anime
    raise HTTPException(status_code=404, detail="Anime não encontrado")

# Criar novo anime
@app.post("/animes/", status_code=status.HTTP_201_CREATED)
async def create_anime(anime: Anime):
    novo_id = max(map(int, anime_db.keys()), default=0) + 1
    anime_db[str(novo_id)] = anime.dict()
    salvar_animes(anime_db)
    return {"id": novo_id, **anime.dict()}

# Deletar anime
@app.delete("/animes/deletar/{anime_id}")
async def delete_anime(anime_id: int):
    anime_id_str = str(anime_id)
    if anime_id_str not in anime_db:
        raise HTTPException(status_code=404, detail="Anime que você quer excluir não existe")
    
    anime_removido = anime_db.pop(anime_id_str)
    salvar_animes(anime_db)
    return {
        "anime": anime_removido,
        "mensagem": "Anime removido com sucesso!"
    }

# Atualizar anime
@app.put("/animes/atualizar/{anime_id}")
async def update_anime(anime_id: int, anime: Anime):
    anime_id_str = str(anime_id)
    if anime_id_str in anime_db:
        anime_db[anime_id_str] = anime.dict()
        salvar_animes(anime_db)
        return {"mensagem": "Anime atualizado com sucesso", "anime": anime.dict()}
    raise HTTPException(status_code=404, detail="Anime não encontrado")
