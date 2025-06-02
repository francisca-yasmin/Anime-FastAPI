from typing import Optional
from pydantic import BaseModel as SCBaseModel

class LocalMOdel (SCBaseModel):
    id: Optional[int]
    nome: str
    relacao: str
    foto: str
    
    class Config:
        orm_mode = True