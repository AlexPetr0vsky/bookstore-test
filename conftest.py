from random import randint

import pytest
import logging
from src.api.config import api_config
from src.api.http_client import HTTPClient
from faker import Faker
fake = Faker()

logger = logging.getLogger(__name__)


class BookFactory:
    @staticmethod
    def create_payload(**kwargs):
        return {
            "book": kwargs.get('book') or fake.word() + " " + fake.word(),
            "name": kwargs.get('name') or fake.name(),
            "photo": kwargs.get('photo', "http://example.com/photo.jpg"),
            "wiki": kwargs.get('wiki', "http://example.com/wiki"),
            "description": kwargs.get('description', fake.sentence()),
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
        api_client.delete_book(book.id)
        logger.info(f"Deleted book: {book.id}")

    authors_response = api_client.get_authors()
    for author in authors_response.data.authors:
        api_client.delete_author(author.id)
        logger.info(f"Deleted author: {author.id}")


@pytest.fixture(scope="function")
def create_books(api_client: HTTPClient):
    def _create_books(count: int = 1):
        for _ in range(count):
            api_client.post_book(BookFactory.create_payload())

    return _create_books
