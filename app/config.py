from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int

    allowed_origins: list[str]

    google_oauth2_client_id: str

    database_username: str
    database_password: str
    database_name: str
    database_host: str
    database_port: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
    )

settings = Settings()