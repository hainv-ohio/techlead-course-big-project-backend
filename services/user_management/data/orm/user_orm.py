from sqlalchemy import Table, Column, String, TEXT, BOOLEAN, UniqueConstraint
from core.base.base_sql import BaseSqlOrm, get_common_columns, get_common_id_column
from ...domain.entities import User

class UserORM(User, BaseSqlOrm):
    __table__ = Table(
        "users",
        BaseSqlOrm.metadata,
        get_common_id_column(),
        Column("first_name", String(255), nullable=False),
        Column("last_name", String(255), nullable=False),
        Column("phone_number", String(255),
               index=True, nullable=False),
        Column("email", String(255), index=True, nullable=False),
        Column("is_created", BOOLEAN, default=False),
        Column("is_verified", BOOLEAN, default=False),
        Column("profile_image_url", TEXT),
        Column("status", String(50)),
        *get_common_columns(),
        UniqueConstraint( "email","phone_number" )
    )