from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Train(BaseModel):
    type: str = Field(alias="g")
    number: str = Field(alias="l")
