from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "TechGo clone API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = ""
    API_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///techgo.db"

    class Config:
        case_sensitive: True


settings = Settings()
