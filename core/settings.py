from pathlib import Path

from typing import Any, Dict, Optional

from pydantic import Field, validator
from pydantic_settings import BaseSettings

project_root = Path(__file__).parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "CatFinder"
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")

    DATABASE_URL: Optional[str] = None
    
    @validator("DATABASE_URL", pre=True)
    def db_uri_validator(
        cls, val: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(val, str):
            return val
        return(
            f"postgresql://{values.get('DB_USER')}:"
            f"{values.get('DB_PASSWORD')}@"
            f"{values.get('DB_HOST')}:{values.get('DB_PORT')}"
            f"/{values.get('DB_NAME')}"
        )
    

settings = Settings(_env_file=Path(project_root, ".env"), _env_file_encoding="utf-8")
