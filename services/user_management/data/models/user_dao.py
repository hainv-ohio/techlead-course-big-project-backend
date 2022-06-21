from ...domain.entities.user import User


class UserDAO(User):
    def __init__(self, full_name: str, phone_number: str, *args, **kwargs) -> None:
        super().__init__(full_name, phone_number, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> User:
        return User(json_data['name'], json_data['phone'])
