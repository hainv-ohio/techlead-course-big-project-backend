from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint, DateTime, ForeignKeyConstraint, TIMESTAMP, Integer, Float
from sqlalchemy.sql import func
from datetime import datetime
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import CartItem


class CartItemORM(CartItem, BaseSqlOrm):
    __table__ = Table(
        "cart_item",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("cart_id", String(255), nullable=False),
        Column("item_id", String(255), nullable=False),
        Column("name", String(255), nullable=False),
        Column("qty", Integer, nullable=False),
        Column("category_id", Integer, nullable=False),
        Column("price", Float, nullable=False),
        Column("currency_code", String(255), nullable=False), 
        Column("detail", String(255), nullable=False),
        UniqueConstraint("id")
    )
