

from .postgres_module import PostgresModule

class PostgresModuleImpl(PostgresModule):

    def __init__(self) -> None:
        super().__init__()

    def query(self, query_str):
        pass