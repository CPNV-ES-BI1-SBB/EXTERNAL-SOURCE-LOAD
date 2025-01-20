from abc import ABC, abstractmethod


class IRequestFetcher(ABC):
    """
    Interface to fetch request from the given url
    """
    @abstractmethod
    def fetchRequest(self, url: str) -> str:
        pass
