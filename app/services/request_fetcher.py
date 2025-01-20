from abc import ABC, abstractmethod


class RequestFetcher(ABC):
    """
    Interface to fetch request from the given url
    """
    @abstractmethod
    def fetchRequest(self, payload: str) -> str:
        pass
