from abc import ABC, abstractmethod


class DatabaseProvider(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
