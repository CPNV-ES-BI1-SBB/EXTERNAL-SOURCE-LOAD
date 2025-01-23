# models/__init__.py

import pkgutil
import importlib
import inspect
import sys

from pydantic import BaseModel


def _iter_namespace(ns_pkg):
    """Retourne la liste de tous les sous-modules (fichiers .py) du package ns_pkg."""
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


MODEL_REGISTRY = {}

# Parcourt tous les modules du package `models` (train.py, departure.py, station.py, etc.)
for finder, name, ispkg in _iter_namespace(sys.modules[__name__]):
    module = importlib.import_module(name)  # ex: models.train, models.departure, etc.

    # On regarde chaque attribut du module
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        # Si c'est une classe Pydantic (et pas la classe BaseModel elle-même)
        if (
            inspect.isclass(attr)
            and issubclass(attr, BaseModel)
            and attr is not BaseModel
        ):
            # On l'ajoute au registre
            MODEL_REGISTRY[attr_name] = attr

# MODEL_REGISTRY est maintenant un dict du genre :
# {
#   "Train": <class 'models.train.Train'>,
#   "Departure": <class 'models.departure.Departure'>,
#   "Station": <class 'models.station.Station'>,
#   ...
# }
