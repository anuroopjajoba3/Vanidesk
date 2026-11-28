"""Settings the app reads when it starts.

Each setting has a default, and a line in the ".env" file overrides it.
"""

import os

from pydantic_settings import BaseSettings, SettingsConfigDict


def default_database_url() -> str:
    """Where the SQLite file lives.

    On your laptop it is receptionist.db in the project folder.
    On Vercel the project folder cannot be written to, only /tmp can,
    so the file goes there. A fresh copy of the app starts with an empty
    /tmp, and app/main.py fills it with the sample calls.
    """
    if os.environ.get("VERCEL"):
        return "sqlite:////tmp/receptionist.db"
    return "sqlite:///./receptionist.db"


class Settings(BaseSettings):
    # The name of the product. This is the ONE place it is written.
    # Every page, every page title and the dashboard read it from here,
    # so renaming the product means changing only this line.
    app_name: str = "Hello"

    database_url: str = default_database_url()

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
