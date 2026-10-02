import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.get(url, timeout=10)

    def close(self):
        self.session.close()