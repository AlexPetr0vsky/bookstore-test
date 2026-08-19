import pytest
import logging
from src.api.config import api_config
from src.api.http_client import HTTPClient

logger = logging.getLogger(__name__)


class BookFactory:
    @staticmethod
    def create_payload(**kwargs):
        return {
            "book": f"Test {kwargs.get('book', 'Book')}",
            "name": f"Test {kwargs.get('name', 'Author')}",
            "photo": kwargs.get('photo', "http://example.com/photo.jpg"),
            "wiki": kwargs.get('wiki', "http://example.com/wiki"),
            "description": kwargs.get('description', "Test description"),
            "icon_book": kwargs.get('icon_book', "http://example.com/icon.jpg")
        }


@pytest.fixture(scope="session")
def api_client():
    return HTTPClient(api_config.API_URL)


@pytest.fixture(autouse=True)
def clean_db(api_client):
    yield
    books_response = api_client.get_books()
    for book in books_response.data.books:
        if book.book.startswith("Test"):
            api_client.delete_book(book.id)

    authors_response = api_client.get_authors()
    for author in authors_response.data.authors:
        if author.name.startswith("Test"):
            api_client.delete_author(author.id)
