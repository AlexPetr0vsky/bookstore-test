from playwright.sync_api import Page
from pages.base_page import BasePage


class AuthorsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.author_card = ".author-card"

    def get_author_cards(self):
        return self.page.locator(self.author_card)

    def get_author_cards_count(self) -> int:
        return self.get_author_cards().count()
