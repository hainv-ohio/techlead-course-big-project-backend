from xmlrpc.client import boolean

# from requests import delete
from ...domain.repository.order_repository import OrderRepository
from ...domain.entities.order import Order
from ..models import OrderDao
from ...domain.entities.order import Order
from ...domain.repository import order_repository


class OrderRepositoryImpl(OrderRepository):
    def __init__(self) -> None:
        super().__init__()
            
    def get_order_by_id(self, order_id: str) -> Order:
        # Access db to get Order by order Id
        # Example data
        return {
            'order_id': '1',
            'status': 1,
            'customer_id': '1',
            'shop_id': '1',
            'take_time_start': '1',
            'take_time_end': '1'
        }

    def save(self, order: Order) -> boolean:
        # Save Order to database if save successful return true else return false
        pass

    def delete(self, order: Order) -> boolean:
        # Delete Order if delete successful return true else return false
        pass

    def delete_by_id(self, order_id: str) -> boolean:
        # Delete Order by order_id if delete successful return true else return false
        pass

    def get_list_order_by_customer_id(self, customer_id: str):
        # Get orders by customer_id
        # return array of Order or empty array
        pass

    def get_list_order_by_shop_id(self, shop_id: str):
        # Get list orders by shop_id
        # return array of Order or empty array
        pass
