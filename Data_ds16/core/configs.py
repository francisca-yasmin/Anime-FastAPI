from pydantic.v1 import BaseSettings #configurações padrão
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'  #colocar isso antes de pesquisar por qualquer coisa na API
    
    #url o nosso banco de dados -> porta do XAMPP
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3308/profissoes"
    
    #vai pegar como herança do mysqlalchemy
    DBBaseModel = declarative_base()
   
#arquivos de configuração fora da alçada do sqlalchemy 
class Config:
    case_sensitive = False
    env_file = "env"
    
settings = Settings()
    
    

