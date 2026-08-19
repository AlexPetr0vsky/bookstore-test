import pytest_check as check

from conftest import BookFactory


class TestPutBook:
    def test_put_book(self, api_client):
        payload = BookFactory.create_payload()
        response = api_client.post_book(data=payload)
        book_id = response.data.id

        payload = BookFactory.create_payload(
            book="Project Hail Mary",
            name="Andy Weir",
            photo="Some new photo.jpg",
            wiki="http://wikipedia.org",
            description="New description",
            icon_book=" Some new icon.jpg"
        )
        response = api_client.put_book(book_id=book_id, data=payload)

        check.equal(response.status_code, 200)
        check.equal(response.data.book, payload.get("book"))
        check.equal(response.data.icon_book, payload.get("icon_book"))
        check.equal(response.data.description, payload.get("description"))
        check.is_not_none(response.data.id)