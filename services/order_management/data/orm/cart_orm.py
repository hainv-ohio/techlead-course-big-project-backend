from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint, DateTime, ForeignKeyConstraint, TIMESTAMP, Integer
from sqlalchemy.sql import func
from datetime import datetime
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Cart


class CartORM(Cart, BaseSqlOrm):
    __table__ = Table(
        "cart",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("customer_id", String(255), nullable=False),
        Column("status", Integer, nullable=False),
        Column("created_at", TIMESTAMP(timezone=False), server_default=func.now()), 
        Column("updated_at", TIMESTAMP(timezone=False), server_default=func.now()),
        UniqueConstraint("id")
    )
