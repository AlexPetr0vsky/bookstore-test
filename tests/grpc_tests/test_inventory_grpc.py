import allure
import pytest_check as check
from src.grpc import inventory_pb2, inventory_pb2_grpc
from conftest import BookFactory


@allure.epic("Inventory gRPC API")
@allure.story("Check Stock")
class TestInventoryGrpc:
    @allure.title("Get stock for existing book via gRPC")
    def test_get_stock_success(self, grpc_client, api_client):
        with allure.step("Create book via REST with stock=10"):
            payload = BookFactory.create_payload(stock=10)
            book_response = api_client.post_book(data=payload)
            book_id = book_response.data.id

        with allure.step("Call gRPC GetStock"):
            request = inventory_pb2.GetStockRequest(book_id=book_id)
            response = grpc_client.get_stock(request)

        with allure.step("Check stock quantity"):
            check.equal(response.book_id, book_id)
            check.equal(response.quantity, 10)

    @allure.title("Reserve stock decreases quantity")
    def test_reserve_stock_success(self, grpc_client, api_client):
        with allure.step("Create book with stock=10"):
            payload = BookFactory.create_payload(stock=10)
            book_response = api_client.post_book(data=payload)
            book_id = book_response.data.id

        with allure.step("Call gRPC ReserveStock for 3 items"):
            request = inventory_pb2.ReserveStockRequest(book_id=book_id, quantity=3)
            response = grpc_client.reserve_stock(request)
            check.is_true(response.success)

        with allure.step("Check remaining stock via gRPC"):
            request = inventory_pb2.GetStockRequest(book_id=book_id)
            response = grpc_client.get_stock(request)
            check.equal(response.quantity, 7)
