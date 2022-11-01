from sqlalchemy import Table, Column, String, DECIMAL, Text, Integer, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Item
from sqlalchemy.dialects import postgresql as psql


class ItemORM(Item, BaseSqlOrm):
    __table__ = Table(
        "product_item",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("name", String(255), nullable=False),
        Column("sku", String(255), nullable=False),
        Column("status", Integer, nullable=False, default=1), 
        Column("category_id", Integer, nullable=True),
        Column("price", DECIMAL, default=0),
        Column("currency_code", String(50), nullable=False, default="VND"),
        Column("sort_description", String(255), nullable=True),
        Column("long_description", Text, nullable=True),
        Column("total_sale", Integer, default=0),
        Column("brand_id", String(50), nullable=True),
        UniqueConstraint("id")
    )
