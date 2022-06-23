from ...domain.entities.item import Item


class ItemDAO(Item):
    def __init__(self, id: int, name: str, category_id: int, price: float, currency_code: int, detail: str, *args,
                 **kwargs) -> None:
        super().__init__(id, name, category_id, price, currency_code, detail, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Item:
        return Item(
            json_data['id'],
            json_data['name'],
            json_data['category_id'],
            json_data['price'],
            json_data['currency_code'],
            json_data['detail']
        )
