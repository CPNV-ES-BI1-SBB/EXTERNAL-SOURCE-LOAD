from app.errors.http_exception import HTTPException


class Forbidden(HTTPException):
    def __init__(self, message="Forbidden"):
        super().__init__(403, message)