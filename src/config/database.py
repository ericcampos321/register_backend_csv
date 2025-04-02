from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
env = os.getenv("NODE_ENV", "local")
load_dotenv(dotenv_path=f".env.{env}")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def connect_db():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print(f"Conectado ao MySQL ({os.getenv('NODE_ENV')})")
    except Exception as e:
        print(f"Erro ao conectar no banco: {e}")
