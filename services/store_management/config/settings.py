from core.config import CoreSettings, CommonApiSettings, SqlDatabaseSettings
from kink import di

"""
Settings for Store Management Service
"""
class Settings(CoreSettings, CommonApiSettings, SqlDatabaseSettings):
    USER_API_PREFIX: str = ''
    ROLE_API_PREFIX: str = '/role'
    AUTH_API_PREFIX: str = '/auth'
    PERMISSION_API_PREFIX: str = '/permission'

    class Config(object):
        case_sensitive = True


cfg = Settings()

di['cfg'] = cfg
di[Settings] = cfg
di[CoreSettings] = cfg
di[CommonApiSettings] = cfg
di[SqlDatabaseSettings] = cfg