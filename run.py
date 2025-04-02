from src.config.env_config import env_config
import uvicorn

if __name__ == "__main__":
    print(
        f" Ambiente: {env_config.NODE_ENV} - Rodando em {env_config.HOST}:{env_config.PORT}"
    )
    uvicorn.run(
        "src.main:app",
        host=env_config.HOST,
        port=env_config.PORT,
        reload=env_config.NODE_ENV == "local",
    )
