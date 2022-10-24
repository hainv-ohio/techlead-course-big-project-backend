from sqlalchemy import Table, Column, String, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Store
from sqlalchemy.dialects import postgresql as psql


class StoreORM(Store, BaseSqlOrm):
    __table__ = Table(
        "store",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("name", String(255), nullable=False),
        Column("phone_number", String(255), nullable=False),
        Column("address_id", String(255), nullable=False),
        Column("status", String(50)),
        Column("time_open", String(50)),
        Column("time_close", String(50)),
        *get_common_columns(is_fk_user=False),
        UniqueConstraint("phone_number")
    )
