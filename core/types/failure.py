

class Failure:
    def __init__(self, code, message) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"