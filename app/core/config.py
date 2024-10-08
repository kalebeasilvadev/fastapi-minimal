import os

from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")


if os.getenv('TEST_ENV'):
    settings = Settings(DATABASE_URL="sqlite:///./test.db")
else:
    settings = Settings()
