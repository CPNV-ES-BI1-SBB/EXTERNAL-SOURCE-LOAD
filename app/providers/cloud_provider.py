from abc import ABC, abstractmethod
from typing import Any


class IDatabaseClient(ABC):
    @abstractmethod
    def insert_data(self, data: Any) -> None:
        pass
