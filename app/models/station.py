from pydantic import BaseModel
from typing import List

from app.models.departure import Departure


class Station(BaseModel):
    name: str
    long: float
    lat: float
    departures: List[Departure]
