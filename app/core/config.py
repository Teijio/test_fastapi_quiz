from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Quiz game"
    database_url: str
    # POSTGRES_USER: str = "POSTGRES_USER"
    # POSTGRES_PASSWORD: str = "POSTGRES_PASSWORD"
    # POSTGRES_SERVER: str = "POSTGRES_SERVER"
    # POSTGRES_PORT: str = "POSTGRES_PORT"
    # POSTGRES_DB: str = "POSTGRES_DB"
    # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    class Config:
        env_file = ".env"


settings = Settings()
