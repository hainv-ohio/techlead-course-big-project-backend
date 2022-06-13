import sys

from services import user_management
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from typing import Union
from fastapi import FastAPI


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    from core.modules.postgres_module import get_postgres_module

    postgres_module = providers.Singleton(get_postgres_module, use_v2=False)

    # service = providers.Factory(
    #     Service,
    #     api_client=api_client,
    # )

@inject
def main():
    list_argv = sys.argv
    if len(list_argv) != 2:
        sys.exit(f'Only accept 1 argument as target app name')
    
    __import__(f"services.{list_argv[1]}.main")

    
if __name__ == "__main__":
    # container = Container()
    # container.wire(modules=[__name__])

    main()