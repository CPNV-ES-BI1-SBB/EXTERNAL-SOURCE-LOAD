from abc import ABC, abstractmethod

'TODO NGY Use standard exception error as parent'
class ErrorInterface(ABC):
    """Interface pour les classes d'erreur personnalisées."""

    @property
    @abstractmethod
    def code(self) -> int:
        """Retourne le code d'erreur."""
        pass

    @property
    @abstractmethod
    def message(self) -> str:
        """Retourne le message d'erreur."""
        pass

    @abstractmethod
    def log_error(self):
        """Méthode pour loguer l'erreur."""
        pass
