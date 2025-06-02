from core.configs import settings
from core.database import engine
from models import all_model

async def create_tables() -> None:
    print("Criando tabelas no banco")
    
    async with engine.begin() as conn:
        
        # deleta
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        #cria
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        
        print("tabelas criadas com sucesso")
        
if __name__ == "__main__":
    import asyncio
    
    asyncio.run(create_tables())
            
