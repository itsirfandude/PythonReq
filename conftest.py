import pytest
from api.client import APIClient


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api(base_url):
    return APIClient(base_url)