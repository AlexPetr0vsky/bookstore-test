import pytest

def test_get_books(api_client):
    response = api_client.get_books()

    assert response.status_code == 200