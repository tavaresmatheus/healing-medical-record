from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    admin_name: str
    admin_email: str
    admin_password: str

    model_config = SettingsConfigDict(env_file='.env')
