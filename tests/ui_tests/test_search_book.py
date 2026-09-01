from random import randint
import allure
import pytest

from src.config.const import Selector, SearchConst

BOOKS_COUNT = 15


@allure.epic("Bookstore UI")
@allure.story("Search book")
class TestSearchBook:
    @allure.title("Search by book title returns results")
    def test_search_book_1(self, main_page, create_books):
        books = create_books(count=BOOKS_COUNT)
        book_title = books[randint(1, BOOKS_COUNT)-1].book

        main_page.search_book(book_title)

        main_page.should_contain_text(Selector.H2, book_title)

    @allure.title("Search by empty / wrong book title returns results")
    @pytest.mark.parametrize("book_title", ["", "xyzabc123"])
    def test_search_book_2(self, main_page, create_books, book_title):
        main_page.search_book(book_title)

        main_page.should_contain_text(selector=Selector.H4, expected_text=SearchConst.NOTHING_WAS_FOUND)
