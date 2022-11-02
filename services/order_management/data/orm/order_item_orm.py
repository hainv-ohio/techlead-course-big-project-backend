from sqlalchemy import Table, Column, String, DECIMAL, Float, Text, Integer, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities.item import Item
from sqlalchemy.dialects import postgresql as psql


class OrderItemORM(Item, BaseSqlOrm):
    __table__ = Table(
        "order_item",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("order_id", String(255), nullable=False),
        Column("item_id", String(255), nullable=False),
        Column("qty", Integer, nullable=False),
        Column("price", Float, nullable=False),
        UniqueConstraint("id")
    )
