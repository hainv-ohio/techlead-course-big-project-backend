from .postgres_module import PostgresModule


def get_postgres_module(use_v2=False) -> PostgresModule:
    if use_v2:
        from .postgres_module_impl_v2 import PostgresModuleImpl
        return PostgresModuleImpl()
    else:
        from .postgres_module_impl import PostgresModuleImpl
        return PostgresModuleImpl()
