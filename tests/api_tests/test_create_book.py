import pytest_check as check

from conftest import BookFactory


class TestCreateBook:
    def test_create_book(self, api_client, cleanup):
        payload = BookFactory.create_payload()
        response = api_client.post("/books", data=payload)
        book_id = response.data["id"]
        author_id = response.data["author_id"]
        cleanup(book_id, author_id)

        check.equal(response.status_code, 201)
        check.equal(response.data["book"], payload.get("book"))
        check.equal(response.data["icon_book"], payload.get("icon_book"))
        check.equal(response.data["description"], payload.get("description"))
        check.is_not_none(response.data["id"])
