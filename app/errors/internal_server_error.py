from app.errors.http_exception import HTTPException


class InternalServerError(HTTPException):
    def __init__(self, message="Internal Server Error"):
        super().__init__(500, message)