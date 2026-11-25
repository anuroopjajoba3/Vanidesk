"""Settings the app reads when it starts.

Each setting has a default, and a line in the ".env" file overrides it.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # The name of the product. This is the ONE place it is written.
    # Every page, every page title and the dashboard read it from here,
    # so renaming the product means changing only this line.
    app_name: str = "PolyRing"

    database_url: str = "sqlite:///./receptionist.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
