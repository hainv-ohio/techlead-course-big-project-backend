from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint, DateTime, ForeignKeyConstraint, TIMESTAMP, Integer
from sqlalchemy.sql import func
from datetime import datetime
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import Order


class OrderORM(Order, BaseSqlOrm):
    __table__ = Table(
        "order",
        BaseSqlOrm.metadata,
        Column("id", String(255), nullable=False, primary_key=True, index=True),
        Column("store_id", String(255), nullable=False),
        Column("customer_id", String(255), nullable=False),
        Column("status", Integer, nullable=False),
        Column("created_at", TIMESTAMP(timezone=False), server_default=func.now()), 
        Column("updated_at", TIMESTAMP(timezone=False), server_default=func.now()),
        Column("take_time_from", TIMESTAMP(timezone=True), nullable=True),
        Column("take_time_to", TIMESTAMP(timezone=True), nullable=True),
        UniqueConstraint("id")
    )
