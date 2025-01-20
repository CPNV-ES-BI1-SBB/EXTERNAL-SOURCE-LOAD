from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.models.departure import Departure


class Station(BaseModel):
    name: str
    departures: List[Departure]
    long: float
    lat: float
