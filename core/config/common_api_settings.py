from typing import Any, Dict, List

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class CommonApiSettings(BaseSettings):
    PORT: int = 8000
    HOST: str = '0.0.0.0'
    JWT_SECRET_KEY: str = ''
    
    SWAGGER_UI_PARAMETERS: Dict[str, Any] = {
        'displayRequestDuration': True,
        'filter': True,
    }

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(
        cls, value,  # noqa: N805, WPS110
    ):
        if isinstance(value, str) and not value.startswith('['):
            return [i.strip() for i in value.split(',')]
        elif isinstance(value, (list, str)):
            return value

        raise ValueError(value)
