

from abc import abstractmethod
from typing import Tuple, Any
from core.types import Failure

class BaseUseCase:
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Tuple[Any, Failure]: raise NotImplementedError()