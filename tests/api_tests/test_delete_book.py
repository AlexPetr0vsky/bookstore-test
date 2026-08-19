import pytest_check as check

from conftest import BookFactory


class TestDeleteBook:
    def test_delete_book(self, api_client):
        payload = BookFactory.create_payload()
        response = api_client.post_book(data=payload)
        book_id = response.data.id

        response = api_client.delete_book(book_id)

        check.equal(response.status_code, 204)
