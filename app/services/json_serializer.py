from typing import Any, List, Optional, Type
from pydantic import ValidationError
from app.models import MODEL_REGISTRY


def detect_model(data: dict) -> Optional[Any]:
    """
    Détecte et instancie le modèle Pydantic approprié basé sur les champs présents.
    Retourne l'objet instancié ou None si aucun modèle ne correspond.
    """
    for model_name, model in MODEL_REGISTRY.items():
        try:
            obj = model(**data)
            return obj
        except ValidationError:
            continue
    return None


def serialize(data: Any) -> List[Any]:
    """
    Parcourt récursivement la structure `data` (dict, list, ou scalars)
    et valide chaque dict contre tous les modèles Pydantic dans MODEL_REGISTRY.
    Retourne une liste de tous les objets validés **au premier niveau**.
    """
    results = []

    if isinstance(data, dict):
        obj = detect_model(data)
        if obj:
            results.append(obj)
            # **Ne pas continuer la récursion pour éviter les objets imbriqués**
            return results
        # Continue la descente dans les valeurs seulement si aucun modèle n'est détecté
        for value in data.values():
            results.extend(serialize(value))

    elif isinstance(data, list):
        for item in data:
            results.extend(serialize(item))

    return results
