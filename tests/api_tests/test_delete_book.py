from random import randint
import allure
import pytest_check as check

BOOKS_COUNT = 5


@allure.epic("Bookstore API")
@allure.story("Delete book")
class TestDeleteBook:
    @allure.title("Sending DELETE request to delete book by id, getting 204 response")
    def test_delete_book_1(self, api_client, create_books):
        with allure.step("Create books"):
            books = create_books(count=BOOKS_COUNT)
            book = books[randint(1, BOOKS_COUNT) - 1]

        with allure.step("Sending delete book request"):
            response = api_client.delete_book(book_id=book.id)

        with allure.step("Checking response with 204"):
            check.equal(response.status_code, 204)

        with allure.step("Checking book was deleted successfully"):
            response = api_client.get_books()
            check.is_not_in(book, response.data.books)

    @allure.title("Sending DELETE request with wrong id, getting 404 response")
    def test_delete_book_2(self, api_client, create_books):
        with allure.step("Create books"):
            created_books = create_books(count=BOOKS_COUNT)
            check.greater(len(created_books), 0)

        with allure.step("Sending delete books request"):
            response = api_client.delete_book(book_id=BOOKS_COUNT+1)

        with allure.step("Checking response with 404"):
            check.equal(response.status_code, 404)
            check.equal(response.data.error, "Book not found")
