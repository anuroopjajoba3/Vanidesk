"""Settings the app reads when it starts.

Each setting has a default, and a line in the ".env" file overrides it.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./vanidesk.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
