from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ha_url: str
    ha_token: str

    class Config:
        env_file = '.env'


settings = Settings()
