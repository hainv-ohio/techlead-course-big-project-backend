from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Store

class StoreORM(Store, BaseSqlOrm):
    __table__ = Table(
        "store",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("name", String(255), nullable=False),
        Column("phone_number", String(255),
               index=True, nullable=False),
        Column("address_id", String(255), index=True, nullable=False),
        Column("status", String(50)),
        *get_common_columns(),
        UniqueConstraint("phone_number")
    )