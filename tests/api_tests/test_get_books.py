import pytest_check as check


def test_get_books(api_client):
    response = api_client.get_books()

    check.equal(response.status_code, 200)
    check.equal(len(response.data), 9)
    for item in range(len(response.data)):
        check.is_not_none(response.data[item].id)
        check.is_not_none(response.data[item].book)
        check.is_not_none(response.data[item].description)
        check.is_not_none(response.data[item].author_id)
        check.is_not_none(response.data[item].icon_book)


def test_create_and_get_book(api_client, created_book):
    book_id = created_book
    response = api_client.get(f"books/{book_id}")
    print(response)