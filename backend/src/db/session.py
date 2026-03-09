from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings
from src.core.config import config_obj


DATABASE_URL = (
   f"postgresql://{config_obj.db_user}:{config_obj.db_password}@{config_obj.db_host}:{config_obj.db_port}/{config_obj.db_name}"
)

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,  
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session