from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker,  Session
from config import config_obj


DATABASE_URL = (
   f"postgresql://{config_obj.db_user}:{config_obj.db_password}@{config_obj.db_host}:{config_obj.db_port}/{config_obj.db_name}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=Session,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
