from random import randint
import allure

BOOKS_COUNT = 15


@allure.epic("Bookstore UI")
@allure.story("Main Page")
class TestMainPage:
    @allure.title("Main page loads successfully")
    def test_main_page_loads(self, main_page):
        with allure.step("Check main page is loading"):
            main_page.should_have_title("Bookstore")

    @allure.title("Search by book title returns results")
    def test_search_book(self, main_page, create_books):
        books = create_books(count=15)
        book_title = books[randint(1, BOOKS_COUNT)-1].book

        main_page.search_book(book_title)
