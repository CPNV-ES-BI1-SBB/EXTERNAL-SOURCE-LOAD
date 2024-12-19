from app.errors.http_exception import HTTPException


class NotFound(HTTPException):
    def __init__(self, message="Not Found"):
        super().__init__(404, message)