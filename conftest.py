import pytest
from api.client import APIClient
from faker import Faker

@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api(base_url):
    return APIClient(base_url)

@pytest.fixture
def user_ids():
    return [1, 2, 3, 4]