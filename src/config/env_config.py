import os
from dotenv import load_dotenv

env = os.getenv("NODE_ENV", "local")
load_dotenv(dotenv_path=f".env.{env}")

class EnvConfig:
    NODE_ENV = env
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "./operadoras.csv")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "*")

env_config = EnvConfig()