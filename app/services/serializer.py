from abc import ABC, abstractmethod
from typing import Any, Type

from pydantic.types import T


class Serializer(ABC):
    """
    Interface to convert string JSON in Python (dict, list, etc.).
    """
    @abstractmethod
    def serialize(self, json_data: str, model_cls: Type[T]) -> Any:
        pass
