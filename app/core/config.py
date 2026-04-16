from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = Field(default="Insurance AI API", alias="APP_NAME")
    env: str = Field(default="dev", alias="ENV")
    debug: bool = Field(default=True, alias="DEBUG")

    database_url: str = Field(
        default="postgresql+psycopg2://postgres:postgres@db:5432/insurance_ai",
        alias="DATABASE_URL",
    )
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")

    chroma_persist_directory: str = Field(default="./chroma_data", alias="CHROMA_PERSIST_DIRECTORY")
    upload_dir: str = Field(default="./uploads", alias="UPLOAD_DIR")

    api_key_header_name: str = Field(default="X-API-Key", alias="API_KEY_HEADER_NAME")
    rate_limit_per_minute: int = Field(default=20, alias="RATE_LIMIT_PER_MINUTE")
    model_name: str = Field(default="gpt-4.1-mini", alias="MODEL_NAME")
    embedding_model: str = Field(default="text-embedding-3-small", alias="EMBEDDING_MODEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True,
    )


settings = Settings()