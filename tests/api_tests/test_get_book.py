from random import randint

import pytest_check as check


class TestGetBook:
    def test_get_books(self, api_client):
        response = api_client.get_books()

        check.equal(response.status_code, 200)
        check.is_not_none(response.data)
        for item in range(len(response.data.books)):
            check.is_not_none(response.data.books[item].id)
            check.is_not_none(response.data.books[item].book)
            check.is_not_none(response.data.books[item].description)
            check.is_not_none(response.data.books[item].author_id)
            check.is_not_none(response.data.books[item].icon_book)

    def test_get_book_by_id(self, api_client):
        books_response = api_client.get_books()
        book_id = randint(1, len(books_response.data.books))
        response = api_client.get_book(book_id)

        check.equal(response.status_code, 200)
        check.equal(response.data.id, book_id)
        check.is_not_none(response.data.book)
        check.is_not_none(response.data.author_id)
        check.is_not_none(response.data.icon_book)
        check.is_not_none(response.data.description)
