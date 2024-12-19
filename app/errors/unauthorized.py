from app.errors.http_exception import HTTPException


class Unauthorized(HTTPException):
    def __init__(self, message="Unauthorized"):
        super().__init__(401, message)