from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    app_title: str = "Quiz game"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
