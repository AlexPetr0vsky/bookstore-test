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

    def should_have_title(self, title):
        with allure.step("Check if title is equal to '{}'".format(title)):
            return expect(self.page).to_have_title(title)
