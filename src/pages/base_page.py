import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
        return self

    def get_title(self) -> str:
        with allure.step("Get title of page"):
            return self.page.title()

    def should_contain_text(self, selector: str, expected_text: str):
        with allure.step(f"Check if '{selector}' contains text '{expected_text}'"):
            return expect(self.page.locator(selector)).to_contain_text(expected_text)

    def should_have_url(self, url):
        with allure.step("Check if url is equal to '{}'".format(url)):
            return expect(self.page).to_have_url(url)
