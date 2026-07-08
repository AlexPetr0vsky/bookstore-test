import pytest

from src.api.config import api_config
from src.api.http_client import HTTPClient


class BookFactory:
    @staticmethod
    def create_payload(
            book: str = "Test Book",
            name: str = "Test Author",
            photo: str = "http://example.com/photo.jpg",
            wiki: str = "http://example.com/wiki",
            description: str = "Test description",
            icon_book: str = "http://example.com/icon.jpg"
    ) -> dict:
        return {
            "book": book,
            "name": name,
            "photo": photo,
            "wiki": wiki,
            "description": description,
            "icon_book": icon_book
        }

    @staticmethod
    def create_book(api_client: HTTPClient, **kwargs) -> int:
        payload = BookFactory.create_payload(**kwargs)
        response = api_client.post("books", data=payload)
        assert response.status_code == 200

        books = api_client.get_books().data
        book_id = max(b.id for b in books)
        return book_id


@pytest.fixture(scope="session")
def api_client():
    return HTTPClient(api_config.API_URL)


@pytest.fixture
def created_book(api_client):
    book_id = BookFactory.create_book(api_client)
    yield book_id
    api_client.delete_book(book_id)