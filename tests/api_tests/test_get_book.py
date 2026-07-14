from random import randint

import pytest_check as check


class TestGetBook:
    def test_get_books(self, api_client):
        response = api_client.get_books()
        print(response)
        check.equal(response.status_code, 200)
        check.is_not_none(response.data)
        for item in range(len(response.data)):
            check.is_not_none(response.data[item].id)
            check.is_not_none(response.data[item].book)
            check.is_not_none(response.data[item].description)
            check.is_not_none(response.data[item].author_id)
            check.is_not_none(response.data[item].icon_book)

    def test_get_book_by_id(self, api_client):
        all_books_len = len(api_client.get_books().data)
        book_id = randint(1, all_books_len)
        response = api_client.get(f"books/{book_id}")

        check.equal(response.status_code, 200)
        check.equal(response.data["id"], book_id)
        check.is_not_none(response.data["book"])
        check.is_not_none(response.data["author_id"])
        check.is_not_none(response.data["icon_book"])
        check.is_not_none(response.data["description"])