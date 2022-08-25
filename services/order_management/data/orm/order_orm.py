from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint, DateTime, ForeignKeyConstraint, TIMESTAMP
from sqlalchemy.sql import func
from datetime import datetime
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Order


class OrderORM(Order, BaseSqlOrm):
    __table__ = Table(
        "order",
        BaseSqlOrm.metadata,
        Column("order_id", String(35), nullable=False),
        Column("user_id", String(35), nullable=False),
        Column("store_id", String(35), nullable=False),
        Column("status", String(25), nullable=False),
        Column("created_at", TIMESTAMP(timezone=False), server_default=func.now()), 
        Column("updated_at", TIMESTAMP(timezone=False), onupdate=func.now()),
        Column("take_time_from", TIMESTAMP(timezone=True), nullable=True),
        Column("take_time_to", TIMESTAMP(timezone=True), nullable=True),
        UniqueConstraint("order_id")
    )
