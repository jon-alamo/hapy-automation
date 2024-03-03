import pydantic


class Settings(pydantic.BaseSettings):
    ha_url: str
    ha_token: str

    class Config:
        env_file = '.env'


settings = Settings()
