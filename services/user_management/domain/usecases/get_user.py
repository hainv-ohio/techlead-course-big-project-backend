

class GetUserUseCase:
    def __init__(self, repository) -> None:
        self.repository = repository

    def __call__(self, id):
        return self.repository.get_user_by_id(id)