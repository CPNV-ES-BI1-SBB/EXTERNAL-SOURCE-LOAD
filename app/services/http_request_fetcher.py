import requests
from app.errors.custom_errors import InvalidUrl, NotFoundError


def fetchRequest(url: str) -> str:
    """
    'url' = URL to fetch.
    return content (str).
    """
    if not url:
        raise InvalidUrl("URL is required.")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except NotFoundError("Data not found.") as e:
        raise e
