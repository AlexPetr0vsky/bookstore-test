import allure
import pytest

from src.config.const import Selector
from tests.ui_tests.conftest import BASE_URL

BOOKS_COUNT = 15


@allure.epic("Bookstore UI")
@allure.story("Main Page")
class TestMainPage:
    @allure.title("Main page loads successfully")
    def test_main_page_1(self, main_page):
        with allure.step("Check main page is loading"):
            main_page.should_have_title("Bookstore")

    @allure.title("Go to Authors / Contacts / Sign in / Register page")
    @pytest.mark.parametrize("selector, page_name", [
        (Selector.NAV_AUTHORS, "authors"),
        (Selector.NAV_CONTACTS, "contacts"),
        (Selector.NAV_SIGN_IN, "sign_in"),
        (Selector.NAV_REGISTER, "register")
    ])
    def test_main_page_2(self, page, main_page, page_name, selector):
        with allure.step("Check main page is loading"):
            page.click(selector)

            main_page.should_have_url(BASE_URL + f"/{page_name}")
