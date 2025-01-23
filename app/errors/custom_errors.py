from app.errors.errors import ErrorInterface


class ServiceError(Exception, ErrorInterface):
    """Exception de base pour les erreurs de service."""

    def __init__(self, code: int, message: str = "Une erreur de service est survenue."):
        self._code = code
        self._message = message
        super().__init__(self._message)

    @property
    def code(self) -> int:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    def log_error(self):
        # Utilisation du module logging pour une meilleure gestion des logs
        import logging
        logging.error(f"Error {self.code}: {self.message}")


class InvalidUrl(ServiceError):
    """Exception levée pour les erreurs de validation."""

    def __init__(self, message: str = "URL invalide."):
        super().__init__(code=422, message=message)


class NotFoundError(ServiceError):
    """Exception levée lorsqu'un élément n'est pas trouvé."""

    def __init__(self, message: str = "Élément non trouvé."):
        super().__init__(code=404, message=message)


class NoDataError(ServiceError):
    """Exception levée lorsqu'aucune donnée n'est trouvée."""

    def __init__(self, message: str = "Aucune donnée trouvée."):
        super().__init__(code=404, message=message)


class ValidationError(ServiceError):
    """Exception levée pour les erreurs de validation."""

    def __init__(self, message: str = "Erreur de validation des données."):
        super().__init__(code=500, message=message)


class DataBaseError(ServiceError):
    """Exception levée pour les erreurs de base de données."""

    def __init__(self, message: str = "Erreur de base de données."):
        super().__init__(code=500, message=message)


class EnvironmentVariablesError(ServiceError):
    """Exception levée pour les erreurs d'environnement."""

    def __init__(self, message: str = "Erreur d'environnement."):
        super().__init__(code=500, message=message)


class InternalError(ServiceError):
    """Exception levée pour les erreurs internes."""

    def __init__(self, message: str = "Erreur interne."):
        super().__init__(code=500, message=message)
