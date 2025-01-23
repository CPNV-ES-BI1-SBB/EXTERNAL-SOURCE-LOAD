import pytest
from pydantic import BaseModel, ValidationError
from app.services.json_serializer import serialize
from app.errors.custom_errors import ValidationError


# Optionnel : si vous voulez éviter de charger TOUTES les classes
# déclarées dans __all_model__, vous pouvez mocker l'import dynamique.
# Sinon, assurez-vous que Station, Train, Departure existent vraiment
# et sont des sous-classes de BaseModel dans app.models.

def test_serialize_valid_json():
    """
    Test avec un JSON correspondant à une classe Station,
    pour vérifier que ça se valide correctement.
    """
    raw_data = {
        "name": "Lausanne",
        "long": 6.629087,
        "lat": 46.516795,
        "departures": [
            {
                "destinationStationName": "Vallorbe",
                "viaStationNames": [
                    "Prilly-Malley",
                    "Renens VD",
                    "Bussigny",
                    "Vufflens-la-Ville",
                    "Cossonay-Penthalaz",
                    "La Sarraz",
                    "Arnex",
                    "Croy-Romainmôtier",
                    "Le Day",
                    "Vallorbe"
                ],
                "departureTime": 1705014120,
                "train": {
                    "type": "R",
                    "line": "4"
                },
                "platform": "",
                "sector": "8"
            },
            {
                "destinationStationName": "Palézieux",
                "viaStationNames": [
                    "Pully-Nord",
                    "La Conversion",
                    "Grandvaux",
                    "Puidoux",
                    "Moreillon",
                    "Palézieux"
                ],
                "departureTime": 1705014120,
                "train": {
                    "type": "R",
                    "line": "6"
                },
                "platform": "",
                "sector": "1"
            },
            {
                "destinationStationName": "St-Maurice",
                "viaStationNames": [
                    "Pully",
                    "Lutry",
                    "Cully",
                    "Vevey",
                    "La Tour-de-Peilz",
                    "Burier",
                    "Clarens",
                    "Montreux",
                    "Villeneuve VD",
                    "Aigle",
                    "Bex",
                    "St-Maurice"
                ],
                "departureTime": 1705014540,
                "train": {
                    "type": "R",
                    "line": "4"
                },
                "platform": "",
                "sector": "6"
            },
        ]
    }
    # Exemple JSON

    # Appel
    result = serialize(raw_data)

    # Vérification
    # result doit être une instance de la classe Station (si c'est elle qui matche).
    # On ne sait pas laquelle a matché si plusieurs modèles sont compatibles,
    # mais on peut tester la valeur des champs, etc.
    assert result[0].name == "Lausanne"
    assert result[0].long == 6.629087
    # Contrôler plus profondément les valeurs des départs
    assert result[0].departures[0].destinationStationName == "Vallorbe"
    assert result[0].departures[1].viaStationNames == [
        "Pully-Nord",
        "La Conversion",
        "Grandvaux",
        "Puidoux",
        "Moreillon",
        "Palézieux"
    ]


def test_serialize_json_no_match():
    """
    Test avec un JSON ne correspondant à aucun modèle,
    on s'attend à lever BadRequestError.
    """
    raw_data = {
        "name": "Yverdon-les-Bains",
        "unnomatch": [
            {
                "departureStationName": "Yverdon-les-Bains",
                "destinationStationName": "Lausanne",
                "viaStationNames": [
                    ""
                ],
                "departureTime": "2024-12-09T08:00:00",
                "train": {
                    "g": "IC",
                    "l": "5"
                },
                "platform": "2",
                "sector": "B"
            }]}

    with pytest.raises(ValidationError) as exc_info:
        serialize(raw_data)

    # Vérifie que le message d'erreur contient "No model found"
    assert "No model found" in str(exc_info.value)


def test_serialize_empty_data():
    """
    Test avec un raw_data vide,
    on s'attend à lever BadRequestError("No data to serialize")
    """
    raw_data = {}

    with pytest.raises(ValidationError) as exc_info:
        serialize(raw_data)

    assert "No data to serialize" in str(exc_info.value)
