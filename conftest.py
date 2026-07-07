import pytest
from src.api.http_client import HTTPClient
from src.api.config import api_config


@pytest.fixture(scope="session")
def api_client():
    return HTTPClient(api_config.API_URL)
