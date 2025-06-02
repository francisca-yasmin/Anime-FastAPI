from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

#configurações internas do banco de dados

engine: AsyncEngine = create_async_engine(settings.DB_URL)
#configurçaõ padrão da aplicação 
Session: AsyncEngine = sessionmaker(
    autocommit=False, #só vai dar commit com comando e não de forma automatica
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine 
)