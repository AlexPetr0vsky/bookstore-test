import allure
from playwright.sync_api import Page

from src.config.const import Selector
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = "input[name='book']"
        self.search_button = "button[type='submit']"
        self.book_card = ".book-card"

    def search_book(self, query: str):
        with allure.step("Enter book to search"):
            self.page.wait_for_selector("input[name='book']")
            self.page.fill("input[name='book']", query)

        with allure.step("Click button to search"):
            self.page.click("button[type='submit']")
            return self

    def get_book_cards(self):
        return self.page.locator(".product")
