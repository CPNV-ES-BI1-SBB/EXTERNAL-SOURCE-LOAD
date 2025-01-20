import requests

from app.services.request_fetcher import IRequestFetcher


class HttpRequestFetcher(IRequestFetcher):
    """
    Implementation of RequestFetcher interface to fetch request from the given url
    """
    def fetchRequest(self, url: str) -> str:
        """
        'url' = URL to fetch.
        return content (str).
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            raise RuntimeError(f"HTTP fetch error: {exc}")