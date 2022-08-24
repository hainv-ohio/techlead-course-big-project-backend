from typing import Any, Dict, List

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator

"""
Settings for:
- Logging system
- Service name & Version
"""
class CoreSettings(BaseSettings):
    SERVICE_NAME: str = ''
    VERSION: str = ''

    LOG_LEVEL: str = 'INFO'

    class Config(object):
        case_sensitive = True