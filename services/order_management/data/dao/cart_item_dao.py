from core.base.base_dao import BaseDao
from ..orm.cart_item_orm import CartItemORM

class CartItemDao(BaseDao):
    model = CartItemORM