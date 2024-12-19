from abc import ABC, abstractmethod


class DatabaseProvider(ABC):
    @abstractmethod
    def connect(self):
        raise InternalServerError("Database connection method not implemented")

    @abstractmethod
    def disconnect(self):
        raise InternalServerError("Database disconnection method not implemented")
