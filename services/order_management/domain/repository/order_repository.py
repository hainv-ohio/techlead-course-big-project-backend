"""
Order repository
"""

from xmlrpc.client import boolean

from ..entities.order import Order


class OrderRepository:

    def get_order_by_id(self, order_id: str) -> Order:
        raise NotImplementedError()

    def save(self, order: Order) -> boolean:
        raise NotImplementedError()

    def delete(self, order: Order) -> boolean:
        raise NotImplementedError()

    def delete_by_id(self, order_id: str) -> boolean:
        raise NotImplementedError()

    def get_list_order_by_customer_id(self, customer_id: str):
        raise NotImplementedError()

    def get_list_order_by_shop_id(self, shop_id: str):
        raise NotImplementedError()
    
    async def init(self):
        pass
