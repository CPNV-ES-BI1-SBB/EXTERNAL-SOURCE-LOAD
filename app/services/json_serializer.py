from typing import Any, List, Optional, Type
from pydantic import ValidationError
from app.models import MODEL_REGISTRY


def detect_model(data: dict) -> Optional[Type]:
    """
    Détecte le modèle Pydantic approprié basé sur les champs présents.
    """
    for model_name, model in MODEL_REGISTRY.items():
        try:
            model(**data)
            return model
        except ValidationError:
            continue
    return None


def serialize(data: Any) -> List[Any]:
    """
    Parcourt récursivement la structure `data` (dict, list, ou scalars)
    et valide chaque dict contre tous les modèles Pydantic dans MODEL_REGISTRY.
    Retourne une liste de tous les objets validés.
    """
    results = []

    if isinstance(data, dict):
        model_class = detect_model(data)
        if model_class:
            try:
                obj = model_class(**data)
                print(f"Detected model: {model_class}")
                results.append(obj)
            except ValidationError as ve:
                print(f"ValidationError: {ve}")  # Débogage
                pass
        # Continue la descente dans les valeurs
        for value in data.values():
            results.extend(serialize(value))

    elif isinstance(data, list):
        for item in data:
            results.extend(serialize(item))

        # Ignorer les scalars
    return results
