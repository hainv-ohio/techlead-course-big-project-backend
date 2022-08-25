import sys
import importlib

from loguru import logger

def main():
    from dotenv import load_dotenv
    load_dotenv()
    
    list_argv = sys.argv
    if len(list_argv) < 2:
        raise Exception("Must have at least target service name")
    
    target_service = list_argv[1]
    args = list_argv[2:]

    logger.debug(f'Args: {args}')

    sub_module = 'main'

    if len(args) > 0:
        sub_module = args[0]
        args = args[1:]

    sub_module =  f"services.{target_service}.{sub_module}"
    logger.debug(f'Using sub module {sub_module}')

    module = importlib.import_module(sub_module)

    if hasattr(module, 'run'):
        logger.debug(f'Calling run with args: {args}')
        module.run(args)


    
if __name__ == "__main__":
    main()