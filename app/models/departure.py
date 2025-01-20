from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.models.train import Train


class Departure(BaseModel):
    departureStationName: str
    destinationStationName: str
    viaStationNames: List[str]
    departureTime: datetime
    train: Train
    platform: str
    sector: Optional[str] = None
