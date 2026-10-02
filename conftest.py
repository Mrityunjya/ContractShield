import pytest

from utils.api_client import APIClient


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_client():
    client = APIClient(BASE_URL)
    yield client
    client.close()