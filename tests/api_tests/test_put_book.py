from random import randint

import allure
import pytest_check as check
from conftest import BookFactory


@allure.epic("Bookstore API")
@allure.story("Put book")
class TestPutBook:
    BOOKS_COUNT = 5

    @allure.title("Sending PUT request to patch book by id, getting 200 response")
    def test_put_book_1(self, api_client, create_books):
        with allure.step("Create books"):
            books = create_books(count=self.BOOKS_COUNT)
            book = books[randint(1, self.BOOKS_COUNT) - 1]

        with allure.step("Create new payload"):
            payload = BookFactory.create_payload(
                book="Project Hail Mary",
                name="Andy Weir",
                photo="Some new photo.jpg",
                wiki="http://wikipedia.org",
                description="New description",
                icon_book=" Some new icon.jpg"
            )

        with allure.step("Sending put request"):
            response = api_client.put_book(book_id=book.id, data=payload)

        with allure.step("Checking response with 200"):
            check.equal(response.status_code, 200)
            check.equal(response.data.book, payload.get("book"))
            check.equal(response.data.icon_book, payload.get("icon_book"))
            check.equal(response.data.description, payload.get("description"))
            check.is_not_none(response.data.id)

    @allure.title("Sending PUT request with wrong id, getting 404 response")
    def test_put_book_2(self, api_client, create_books):
        with allure.step("Create books"):
            created_books = create_books(count=self.BOOKS_COUNT)
            check.greater(len(created_books), 0)

        with allure.step("Sending put request"):
            put_payload = BookFactory.create_payload()
            response = api_client.put_book(book_id=self.BOOKS_COUNT+1, data=put_payload)

        with allure.step("Checking response with 404"):
            check.equal(response.status_code, 404)
            check.equal(response.data.error, "Book not found")
