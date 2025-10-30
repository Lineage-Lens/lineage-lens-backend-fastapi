from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int

    database_username: str
    database_password: str
    database_name: str
    database_host: str
    database_port: int

    model_config = SettingsConfigDict(
        env_file=".env",
    )

settings = Settings()