from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bem-Vindo ao menu de animes!"}

anime_db = {
    1: {"titulo": "Naruto", "categoria": "Shounen", "episodios": 700},
    2: {"titulo": "HunterxHunter", "categoria": "Shounen", "episodios": 148},
    3: {"titulo": "Demon Slayer", "categoria": "Shounen", "episodios": 63},
    4: {"titulo": "Dragon Ball", "categoria": "Shounen", "episodios": 696}
}

class Anime(BaseModel):
    nome: str
    categoria: str
    episodios: int
    
@app.get("/") #rota ou endpoint
async def root():
    return {"message": "Bem-Vindo a minha API de Animes!"}

#listar todos os animes na lista
@app.get("/animes/")
async def get_all_animes():
    return anime_db

#buscar os animes por id
@app.get("/animes/{anime_id}")
async def buscar_anime(anime_id: int):
    anime = anime_db.get(anime_id)
    if anime:
        return anime
    #lança uma exceção HTTP onde a resposta é retornado em formato JSON
    raise HTTPException(status_code=404, detail="Anime não encontrado")

# @app.post("/animes/criar")
# async def create_anime(anime: Anime):
#     for existe in anime_db.values():
#          if existe["titulo"].lower() == anime.titulo.lower(): #verifica se já existe
#  
# raise HTTPException(status_code=404, detail='O anime já existe')
@app.post("/animes/")
async def create_item(anime: Anime):
    return anime
    
    
        

            
            


        



