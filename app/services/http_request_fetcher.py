import requests

from app.services.request_fetcher import RequestFetcher


class HttpRequestFetcher(RequestFetcher):
    """
    Implementation of RequestFetcher interface to fetch request from the given url
    """
    def fetchRequest(self, payload: str) -> str:
        """
        'payload' = URL to fetch.
        return content (str).
        """
        try:
            response = requests.get(payload, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            raise RuntimeError(f"HTTP fetch error: {exc}")