from playwright.sync_api import Page, expect
from .base_page import BasePage


class BookPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_selector = "h1"
        self.description_selector = ".description"
        self.author_selector = ".author"
        self.back_button = "a:has-text('Back')"

    def get_title(self):
        return self.page.locator(self.title_selector)

    def get_description(self):
        return self.page.locator(self.description_selector)

    def get_author(self):
        return self.page.locator(self.author_selector)

    def click_back(self):
        self.page.click(self.back_button)
        return self
