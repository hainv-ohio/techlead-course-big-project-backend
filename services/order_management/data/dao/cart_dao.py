from core.base.base_dao import BaseDao
from ..orm.cart_orm import CartORM

class CartDao(BaseDao):
    model = CartORM