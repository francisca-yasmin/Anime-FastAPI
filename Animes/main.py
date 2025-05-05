from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json #salvar os animes num arquivo json

app = FastAPI()


anime_db = {
    1: {"titulo": "Naruto", "categoria": "Shounen", "episodios": 700},
    2: {"titulo": "HunterxHunter", "categoria": "Shounen", "episodios": 148},
    3: {"titulo": "Demon Slayer", "categoria": "Shounen", "episodios": 63},
    4: {"titulo": "Dragon Ball", "categoria": "Shounen", "episodios": 696},
    5: {"titulo": "One Piece", "categoria": "Aventura", "episodios": 1128}
}

class Anime(BaseModel):
    nome: str
    categoria: str
    episodios: int
    
#listar todos os animes na lista
@app.get("/animes/")
async def get_all_animes():
    return anime_db

#buscar os animes por id
@app.get("/animes/{anime_id}")
async def read_anime(anime_id: int):
    anime = anime_db.get(anime_id)
    if anime:
        return anime
    raise HTTPException(status_code=404, detail="Anime não encontrado") #lança uma exceção HTTP onde a resposta é retornado em formato JSON

#criar um anime novo
@app.post("/animes/", status_code=201) #201 = created
async def create_anime(anime: Anime):
    novo_id = max(anime_db.keys()) + 1
    anime_db[novo_id] = anime.dict()
    salvar_animes(anime_db)
    return {"id": novo_id, **anime.dict()}
    
#deletar um anime
@app.delete("/animes/deletar/{anime_id}")
async def delete_anime(anime_id: int):
    if anime_id not in anime_db:
        raise HTTPException(status_code=404, detail="Anime que você quer excluir não existe")
    return 

#atualizar anime pela chave primaria    
@app.put("/animes/atualizar/{anime_id}")
async def update_anime(anime_id: int, anime: Anime):
    if anime_id in anime_db:
        anime_db[anime_id] = {
            "titulo": anime.nome,
            "categoria": anime.categoria,
            "episodios": anime.episodios
        }
        return {"mensagem": "Anime atualizado com sucesso", "anime": anime_db[anime_id]}
    raise HTTPException(status_code=404, detail="Anime não encontrado")

        
# +++++++++++++++++++++++++++++++

arquivo_db = 'animes.json'

def carregar_animes():
    try:
        with open(arquivo_db, "r", ecoding="utf-8") as a:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def salvar_animes(db):
    with open(arquivo_db, "w", encoding="utf-8") as a:
        json.dump(db, a, indent=4, ensure_ascii=False)
    
