
from core.base.base_dao import BaseDao
from ..orm.user_orm import UserORM

class UserDAO(BaseDao):
    model = UserORM
