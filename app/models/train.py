from pydantic import BaseModel


class Train(BaseModel):
    type: str
    line: str
