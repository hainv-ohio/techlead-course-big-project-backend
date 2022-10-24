

import alembic.config
import pathlib

from loguru import logger
from .data.orm import *

def run(args):
    
    parent_dir = pathlib.Path(__file__).parent.resolve()

    alembicArgs = [
        '--raiseerr',
        '-c', f'{parent_dir}/alembic.ini',
        # 'upgrade', 
        # 'head',
        *args
    ]

    logger.debug(f'Calling alembic with args: {alembicArgs}')
    alembic.config.main(argv=alembicArgs)
