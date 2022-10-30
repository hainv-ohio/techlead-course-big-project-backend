from ...domain.entities.item import Item


class ItemDAO(Item):
    def __init__(self, id: int, name: str, sku: str, status: int, category_id: int, price: float, currency_code: int,
        sort_description: str, long_description: str, total_sale: int, brand_id: int,
        *args,**kwargs) -> None:
        super().__init__(id, name, sku, status, category_id, price, currency_code, 
        sort_description, long_description, total_sale, brand_id, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Item:
        return Item(
            json_data['id'],
            json_data['name'],
            json_data['sku'],
            json_data['status'],
            json_data['category_id'],
            json_data['price'],
            json_data['currency_code'],
            json_data['sort_description'],
            json_data['long_description'],
            json_data['total_sale'],
            json_data['brand_id']
        )
