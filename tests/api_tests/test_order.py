import allure
import pytest_check as check
from conftest import BookFactory


@allure.epic("Bookstore API")
@allure.story("Create Order")
class TestCreateOrder:
    @allure.title("Sending POST request and getting 201 response")
    def test_create_order_success(self, api_client):
        with allure.step("Create a book"):
            payload = BookFactory.create_payload()
            book_response = api_client.post_book(data=payload)
            book_id = book_response.data.id

        with allure.step("Create Order for 2 books"):
            order_payload = {"book_id": book_id, "quantity": 2}
            response = api_client.post_order(data=order_payload)

        with allure.step("Checking response with 201"):
            check.equal(response.status_code, 201)
            check.equal(response.data.book_id, book_id)
            check.equal(response.data.quantity, 2)
            check.equal(response.data.status, "pending")
            check.is_not_none(response.data.id)

    @allure.title("Create order with insufficient stock")
    def test_create_order_not_enough_stock(self, api_client):
        with allure.step("Create a book with stock=1"):
            payload = BookFactory.create_payload(stock=1)
            book_response = api_client.post_book(data=payload)
            book_id = book_response.data.id

        with allure.step("Try to order 5 books"):
            order_payload = {"book_id": book_id, "quantity": 5}
            response = api_client.post_order(data=order_payload)

        with allure.step("Checking response with 400"):
            check.equal(response.status_code, 400)
            check.equal(response.data.error, "Not enough books in stock")
