from pydantic_settings import BaseSettings
import logging


class Settings(BaseSettings):
    ha_api_url: str
    ha_ws_url: str
    ha_token: str
    timezone: str = 'CET'
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'


settings = Settings()


logging.basicConfig(
    level=settings.log_level.upper(),
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
