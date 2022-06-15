
class User:
    def __init__(self,
                 full_name: str,
                 phone_number: str,
                 *args, **kwargs) -> None:

        self.full_name = full_name
        self.phone_number = phone_number
        self.status = "ACTIVE"
