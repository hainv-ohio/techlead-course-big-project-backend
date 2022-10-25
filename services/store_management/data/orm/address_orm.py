from sqlalchemy import Table, Column, String, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Address
from sqlalchemy.dialects import postgresql as psql


class AddressORM(Address, BaseSqlOrm):
    __table__ = Table(
        "address",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("name", String(255), nullable=False),
        Column("map_name", String(255)),
        Column("lat", String(255)),
        Column("long", String(255)),
        Column("country", String(50)),
        Column("city", String(50)),
        Column("district", String(50)),
        Column("ward", String(50)),
        Column("detail", String(50)),
        *get_common_columns(is_fk_user=False),
    )
