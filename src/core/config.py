from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    MAIN_TAG_GROUP: list[str]
    cors_allowed_origins: list[str]

def get_settings() -> Settings:
    return Settings(
        DATABASE_URL="postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres",
        MAIN_TAG_GROUP=["Job CRUD"],
        cors_allowed_origins=["http://localhost:8000"]
    )