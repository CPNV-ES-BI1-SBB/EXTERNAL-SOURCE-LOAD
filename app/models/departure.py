from pydantic import BaseModel
from typing import List


from app.models.train import Train


class Departure(BaseModel):
    destinationStationName: str
    viaStationNames: List[str]
    departureTime: int
    train: Train
    platform: str
    sector: str
