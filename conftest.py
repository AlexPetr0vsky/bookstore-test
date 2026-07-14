import pytest
import logging

from src.api.config import api_config
from src.api.http_client import HTTPClient

logger = logging.getLogger(__name__)


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


@pytest.fixture(autouse=True, scope="session")
def cleanup_old_test_authors(api_client):
    def delete_test_authors():
        response = api_client.get_authors()
        if response.status_code != 200:
            return
        for author in response.data:
            if author["name"] == "Test Author":
                api_client.delete_author(author["id"])
                logger.info(f"Deleted author {author['id']} and their books")

    delete_test_authors()
    yield
    delete_test_authors()


@pytest.fixture(scope="session")
def api_client():
    return HTTPClient(api_config.API_URL)


@pytest.fixture
def cleanup(api_client):
    created = []

    def add_ids(book_id, author_id):
        created.append((book_id, author_id))

    yield add_ids

    for book_id, author_id in created:
        try:
            api_client.delete_book(book_id)
            logger.info(f"Book {book_id} deleted")
        except Exception as e:
            logger.error(f"Failed to delete book {book_id}: {e}")

        try:
            api_client.delete_author(author_id)
            logger.info(f"Author {author_id} deleted")
        except Exception as e:
            logger.error(f"Failed to delete author {author_id}: {e}")
