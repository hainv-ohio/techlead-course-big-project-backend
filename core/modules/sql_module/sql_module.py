from sqlalchemy import create_engine, orm
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine

from core.config import SqlDatabaseSettings

from kink import inject
from loguru import logger

@inject
def connect_database(db_settings: SqlDatabaseSettings) -> None:
    logger.info(f'Connecting to SQL database at {db_settings.DATABASE_URI}')
    engine = create_async_engine(
        db_settings.DATABASE_URI, pool_pre_ping=True, future=True,
        echo=True,
    )
    
    return engine

@inject
async def create_database_tables(engine: AsyncEngine):
    logger.info(f'Creating database tables')
    from core.base.base_sql import BaseSqlOrm
    async with engine.begin() as conn:
        await conn.run_sync(BaseSqlOrm.metadata.create_all)

@inject
def get_async_session_builder(engine: AsyncEngine) -> orm.sessionmaker:
    print('creating session builder')
    factory = orm.sessionmaker(
        engine, class_=AsyncSession, autoflush=False, expire_on_commit=False,
    )
    return factory


def sync_session(url: str) -> orm.scoped_session:
    engine = create_engine(
        url, pool_pre_ping=True, future=True,
    )
    factory = orm.sessionmaker(
        engine, autoflush=False, expire_on_commit=False,
    )
    return orm.scoped_session(factory)
