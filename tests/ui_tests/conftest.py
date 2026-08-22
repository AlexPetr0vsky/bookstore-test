from typing import Callable, Any
import pytest
from src.pages.main_page import MainPage
from src.api.http_client import HTTPClient
from src.utils.factory import BookFactory

BASE_URL = "http://localhost:5001"


@pytest.fixture
def main_page(page):
    main_page = MainPage(page)
    main_page.navigate(BASE_URL)
    return main_page


@pytest.fixture(scope="class")
def create_books(api_client: HTTPClient) -> Callable[..., list[Any]]:
    def _create_books(count: int = 1):
        books = [api_client.post_book(BookFactory.create_payload()).data for _ in range(count)]
        return books

    return _create_books
