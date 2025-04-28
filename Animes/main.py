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

#criar um anime novo
@app.post("/animes/crar/")
async def create_anime(anime: Anime):
    return anime

    
#deletar um anime
@app.delete("/animes/deletar/")
async def delete_anime(anime: Anime):
    if anime in anime_db:
        removido = anime_db.pop(anime)
        return {'mensagem': 'anime removido com sucesso', 'anime': removido}
    raise HTTPException(status_code=404, detail="Anime que você quer excluir não existe")
    
    
@app.update("/animes/atualizar/")
async def update_anime(anime: Anime):
    return anime
    
    
        

            
            


        



