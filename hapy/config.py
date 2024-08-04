from pydantic_settings import BaseSettings, SettingsConfigDict
import logging


class Settings(BaseSettings):
    ha_api_url: str
    ha_ws_url: str
    ha_token: str
    timezone: str = 'CET'
    log_level: str = 'INFO'
    auto_reload: bool = True
    repository_url: str = ''
    git_polling_minutes: int = 3

    class Config:
        env_file = '.env'
        extra = 'ignore'


settings = Settings()


logging.basicConfig(
    level=settings.log_level.upper(),
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
