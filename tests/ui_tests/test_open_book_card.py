import allure
from pytest_check import check

from src.config.const import Selector

BOOKS_COUNT = 15


@allure.epic("Bookstore UI")
@allure.story("Search book")
class TestOpenBookCard:
    @allure.title("Open book card")
    def test_open_book_card_1(self, main_page, create_books):
        books = create_books(count=BOOKS_COUNT)
        main_page.page.reload()
        main_page.page.wait_for_selector(".product", timeout=10000)

        book_card = main_page.get_book_cards().first
        book_card_locator = book_card.locator(".product-desc a")
        book_title = book_card_locator.text_content()

        book_card_locator.click()

        main_page.should_contain_text(selector=Selector.H1, expected_text=book_title)
        check.equal(book_title, books[0].book)
