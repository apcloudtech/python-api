# config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    PROJECT_NAME: str = "BlogFolio"
    PROJECT_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"


# class Settings:
#     PROJECT_NAME: str = "Job Board"
#     PROJECT_VERSION: str = "1.0.0"


settings = Settings()
