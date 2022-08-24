from typing import Any

from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import ForeignKey, Column, BOOLEAN, TIMESTAMP, text,  inspect, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import (
    declarative_base,
)

BaseSqlOrm = declarative_base()

def get_common_id_column():
    return Column("id", psql.UUID(as_uuid=True),
            server_default=text('gen_random_uuid()'),
            primary_key=True,
            index=True
           )

def get_user_fk_column(col_name: str, *args, **kwargs):
    return get_fk_column(col_name, 'users.id', psql.UUID(as_uuid=True), *args, **kwargs)

def get_id_fk_column(col_name: str, target_col: str, *args, **kwargs):
    return get_fk_column(col_name, target_col, psql.UUID(as_uuid=True), *args, **kwargs)

def get_fk_column(col_name: str, target_col: str, col_type: Any, *args, **kwargs):
    return Column(col_name, col_type, ForeignKey(target_col), *args, **kwargs)


def get_common_columns(is_fk_user=True):
    return [
        Column("created_at", TIMESTAMP(timezone=False), server_default=func.now()),
        get_user_fk_column("created_by") if is_fk_user else Column("created_by", psql.UUID(as_uuid=True)),
        Column("updated_at", TIMESTAMP(timezone=False), onupdate=func.now()),
        get_user_fk_column("updated_by") if is_fk_user else Column("updated_by", psql.UUID(as_uuid=True)),
        Column("deleted_at", TIMESTAMP(timezone=False)),
        get_user_fk_column("deleted_by") if is_fk_user else Column("deleted_by", psql.UUID(as_uuid=True)),
        Column("is_deleted", BOOLEAN, default=False)
    ]

def get_common_language_column():
    return Column("language", String(10))