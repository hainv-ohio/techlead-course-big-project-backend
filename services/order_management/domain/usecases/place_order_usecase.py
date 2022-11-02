
import uuid
from datetime import date, datetime
from typing import Tuple

from core.types import Failure
from .base import BaseUsecase
from ..entities.order_item import OrderItem
from ..entities.order import Order



class PlaceOrderUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, store_id, customer_id, take_time_from, take_time_to, items):
        print('----- gererer -----')
        order = await self.repository.save(
            Order(
                id=str(uuid.uuid4()),
                store_id=store_id,
                customer_id=customer_id,
                take_time_from=take_time_from,
                take_time_to=take_time_to,
                status=1,
                created_at=datetime.now(),
                updated_at=datetime.now()
                )
            )

        print('--- Order Info ---')
        print(order)

        items_order = []
        if order is not None:
            for item in items:
                item_order = await self.order_item_repository.save(
                    OrderItem(
                        id=str(uuid.uuid4()),
                        order_id=order.id,
                        item_id=item.item_id,
                        qty=item.qty,
                        price=item.price
                    )
                )

                print('--- Order Items Info ---')
                print(item_order)
                
                items_order.append(item_order)
        if items_order is not None:
            return items_order
        return None

        
        
        
