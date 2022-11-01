from typing import Tuple, List
from abc import abstractmethod
from unicodedata import name
from core.types import failure
from core.types.failure import Failure
from ...domain.repository.cart_repository import CartRepository
from ..dao.cart_dao import CartDao
from ..dao.cart_item_dao import CartItemDao
from ...domain.entities.cart import Cart
from ...domain.entities.cart_item import CartItem
from ...data.orm.cart_item_orm import CartItemORM
from ...data.orm.cart_orm import CartORM
from ...data.dao.item_dao import ItemDAO



class CartRepositoryImpl(CartRepository):
    def __init__(self) -> None:
        super().__init__()
        self.cart_dao = CartDao()
        self.cart_item_dao = CartItemDao()
        self.item_dao = ItemDAO()

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
        item = await self.item_dao.find_one_or_none(id=item_id)
        if item is None:
            return None, Failure(401, "Item is not exist.")

        cart = await self.cart_dao.find_one_or_none(customer_id=customer_id, status=1)
        if cart is not None:
            cart_id = cart.id
            cart_item = CartItemORM(**CartItem(cart_id=str(cart_id), item_id=str(item.id), qty=qty, name=item.name, category_id=int(item.category_id), price=item.price, currency_code=item.currency_code, detail=item.long_description).to_json(keys=['cart_id', 'item_id', 'qty', 'name', 'category_id', 'price', 'currency_code', 'detail']))
            await self.cart_item_dao.save(cart_item)
            return cart_item, None
        # cart = Cart(customer_id=customer_id, status=1)
        cart = CartORM(**Cart(customer_id=customer_id, status=1).to_json(keys=['customer_id', 'status']))
        await self.cart_dao.save(cart)
        cart_id = cart.id
        cart_item = CartItemORM(** CartItem(cart_id=str(cart_id), item_id=str(item.id), qty=qty, name=item.name, category_id=int(item.category_id), price=item.price, currency_code=item.currency_code, detail=item.long_description).to_json(keys=['cart_id', 'item_id', 'qty', 'name', 'category_id', 'price', 'currency_code', 'detail']))
        await self.cart_item_dao.save(cart_item)
        # print('-----cart item -----')
        # print(cart_item)
        return cart_item, None

    @abstractmethod
    async def get_cart_by_customer_id(self, customer_id: str):
        print('-----custom----')
        print(customer_id)
        cart = await self.cart_dao.find_one_or_none(customer_id=customer_id, status=1)
        print('-----cart----')
        print(cart)
        if cart is not None:
            return cart
        return None


            

