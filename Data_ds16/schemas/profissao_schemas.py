from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProfissaoSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    area: str
    formacao: str
    salario: float
    foto: str
    
    #converte o JSON para banco de dados
    class Config:
        orm_mode = True