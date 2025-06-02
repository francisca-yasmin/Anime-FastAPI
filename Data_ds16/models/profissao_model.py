from core.configs import settings
from sqlalchemy import Column, Integer, String, Float

class ProfissaoModel(settings.DBBaseModel):
    __tablename__ = "profissao"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: String = Column(String(255))
    area: String = Column(String(255))
    formacao: String = Column(String(255))
    salario: Float = Column(Float())
    foto: str = Column(String(255))
    