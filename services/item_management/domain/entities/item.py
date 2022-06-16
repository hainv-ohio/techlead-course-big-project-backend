


class Item:
    def __init__(self,
                id: int,
                name: str,
                category_id: int,
                price: float,
                currency_code: int,
                detail: str,
                *args, **kwargs) -> None:
        self.id = id
        self.name = name
        self.category_id = category_id
        self.price = price
        self.currency_code = currency_code
        self.detail = detail
