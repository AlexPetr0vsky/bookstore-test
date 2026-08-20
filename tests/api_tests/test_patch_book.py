import pytest_check as check

from conftest import BookFactory


class TestPatchBook:
    def test_patch_book_200ok(self, api_client):
        payload = BookFactory.create_payload()
        response = api_client.post_book(data=payload)
        book_id = response.data.id

        patch_payload = {"description": "Updated description"}
        response = api_client.patch_book(book_id=book_id, data=patch_payload)

        check.equal(response.status_code, 200)
        check.equal(response.data.book, payload.get("book"))
        check.equal(response.data.icon_book, payload.get("icon_book"))
        check.equal(response.data.description, patch_payload.get("description"))
        check.is_not_none(response.data.id)
