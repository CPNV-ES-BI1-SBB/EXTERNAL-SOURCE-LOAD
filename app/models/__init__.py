from .station import Station
from .departure import Departure
from .train import Train

# grouping all the models
all_models = [Station, Train, Departure]

# Exporting all the models
__all_model__ = [
    "Station",
    "Train",
    "Departure",
    "all_models"
]
