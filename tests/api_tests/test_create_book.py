import pytest_check as check
import allure
from conftest import BookFactory


@allure.epic("Bookstore API")
@allure.story("Create Book")
class TestCreateBook:
    @allure.title("Sending POST request and getting 201 response")
    def test_create_book_1(self, api_client):
        with allure.step("Create Book"):
            payload = BookFactory.create_payload()
            response = api_client.post_book(data=payload)

        with allure.step("Checking response with 201"):
            check.equal(response.status_code, 201)
            check.equal(response.data.book, payload.get("book"))
            check.equal(response.data.icon_book, payload.get("icon_book"))
            check.equal(response.data.description, payload.get("description"))
            check.is_not_none(response.data.id)

    @allure.title("Sending POST request with empty body and getting 400 response")
    def test_create_book_2(self, api_client):
        with allure.step("Create Book"):
            payload = {}
            response = api_client.post_book(data=payload)

        with allure.step("Checking response with 400"):
            check.equal(response.status_code, 400)
            check.equal(response.data.error, "Empty request")

    @allure.title("Sending POST request without mandatory field and getting 400 response")
    def test_create_book_3(self, api_client):
        with allure.step("Create Book"):
            payload = BookFactory.create_payload()
            del payload["book"]

            response = api_client.post_book(data=payload)

        with allure.step("Checking response with 400"):
            check.equal(response.status_code, 400)
            check.equal(response.data.error, "Bad request")
