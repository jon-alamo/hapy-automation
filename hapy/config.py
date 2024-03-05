from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ha_url: str
    ha_token: str
    timezone: str = 'CET'

    class Config:
        env_file = '.env'


settings = Settings()
