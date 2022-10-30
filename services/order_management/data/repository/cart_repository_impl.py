from typing import Tuple, List
from abc import abstractmethod
from unicodedata import name
from core.types.failure import Failure
from ...domain.repository.cart_repository import CartRepository
from ..dao.cart_dao import CartDao
from ..dao.cart_item_dao import CartItemDao
from ...domain.entities.cart import Cart
from ...domain.entities.cart_item import CartItem
from ...data.orm.cart_item_orm import CartItemORM
from ...data.orm.cart_orm import CartORM



class CartRepositoryImpl(CartRepository):
    def __init__(self) -> None:
        super().__init__()
        self.cart_dao = CartDao()
        self.cart_item_dao = CartItemDao()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    @abstractmethod
    async def get_cart_by_id(self, order_id: str) -> Tuple[Cart, Failure]:
        pass

    @abstractmethod
    async def get_all_cart_items(self, cart_id: str):
        cart_items = await self.cart_item_dao.find(cart_id=cart_id)
        return cart_items

    @abstractmethod
    async def add_item_to_cart(self, item_id, customer_id, qty) -> Tuple[CartItem, Failure]:
        item = {
            "id": "123",
            "name": "Test",
            "category_id": 1,
            "price": 10,
            "currency_code": 1,
            "detail": "Lorem sum"
        }
        cart = await self.cart_dao.find_one_or_none(customer_id=customer_id, status=1)
        if cart is not None:
            cart_id = cart.id
            cart_item = CartItemORM(**CartItem(cart_id=str(cart_id), item_id=item_id, qty=qty, name="Test", category_id=1, price=10, currency_code="dollar", detail="Lorem" ).to_json(keys=['cart_id', 'item_id', 'qty', 'name', 'category_id', 'price', 'currency_code', 'detail']))
            await self.cart_item_dao.save(cart_item)
            return cart_item, None
        # cart = Cart(customer_id=customer_id, status=1)
        cart = CartORM(**Cart(customer_id=customer_id, status=1).to_json(keys=['customer_id', 'status']))
        await self.cart_dao.save(cart)
        cart_id = cart.id
        cart_item = CartItemORM(** CartItem(item_id=item_id, qty=qty, name="Test", category_id=1, price=10, currency_code="dollar", detail="Lorem", cart_id=str(cart_id)).to_json(keys=['cart_id', 'item_id', 'qty', 'name', 'category_id', 'price', 'currency_code', 'detail']))
        await self.cart_item_dao.save(cart_item)
        # print('-----cart item -----')
        # print(cart_item)
        return cart_item, None


            

