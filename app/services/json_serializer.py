from typing import List

from pydantic import BaseModel, ValidationError
from app.models import all_models
from app.errors.errors import BadRequestError


class ModelSerializer:
    """
    Serializer that get all the models from app.models.all_models
    and try to validate the JSON.
    """

    def __init__(self, all_models: List[type]):
        self.all_models = all_models

    def serialize_to_any_model(self, json_data: str) -> BaseModel:
        errors = []

        for model_cls in all_models:
            try:
                obj = model_cls.model_validate_json(json_data)
                return obj
            except ValidationError as val_err:
                errors.append(f"{model_cls.__name__} has fail: {val_err}")

        # In case of not match found, we raise an exception
        error_msg = "No model found to valide this JSON:\n" + "\n".join(errors)
        raise BadRequestError(error_msg)
