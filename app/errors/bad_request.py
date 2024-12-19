from app.errors.http_exception import HTTPException


class BadRequest(HTTPException):
    def __init__(self, message="Bad Request"):
        super().__init__(400, message)