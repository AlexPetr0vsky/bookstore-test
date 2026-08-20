from random import randint
import allure
import pytest_check as check

from conftest import BookFactory


@allure.epic("Bookstore API")
@allure.story("Get book")
class TestGetBooks:
    @allure.title("Sending GET request to get list of books, getting 200 response")
    def test_get_books_1(self, api_client, create_books):
        with allure.step("Create Book"):
            create_books(count=5)

        with allure.step("Sending get books request"):
            response = api_client.get_books()
            print(response)
        # with allure.step("Checking response with 200"):
        #     check.equal(response.status_code, 200)
        #     check.is_not_none(response.data)
        #     for item in range(len(response.data.books)):
        #         check.is_not_none(response.data.books[item].id)
        #         check.is_not_none(response.data.books[item].book)
        #         check.is_not_none(response.data.books[item].description)
        #         check.is_not_none(response.data.books[item].author_id)
        #         check.is_not_none(response.data.books[item].icon_book)

    @allure.title("Sending GET request to get list of books, getting 200 response")
    def test_get_books_2(self, api_client):
        with allure.step("Sending get books request"):
            response = api_client.get_books()

        with allure.step("Checking response with 200"):
            check.equal(response.status_code, 200)
            check.is_not_none(response.data)
            for item in range(len(response.data.books)):
                check.is_not_none(response.data.books[item].id)
                check.is_not_none(response.data.books[item].book)
                check.is_not_none(response.data.books[item].description)
                check.is_not_none(response.data.books[item].author_id)
                check.is_not_none(response.data.books[item].icon_book)

@allure.epic("Bookstore API")
@allure.story("Get book")
class TestGetBook:
    def test_get_book_1(self, api_client):
        books_response = api_client.get_books()
        book_id = randint(1, len(books_response.data.books))
        response = api_client.get_book(book_id)

        check.equal(response.status_code, 200)
        check.equal(response.data.id, book_id)
        check.is_not_none(response.data.book)
        check.is_not_none(response.data.author_id)
        check.is_not_none(response.data.icon_book)
        check.is_not_none(response.data.description)
