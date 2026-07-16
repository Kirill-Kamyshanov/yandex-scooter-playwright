import allure
from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Проверка, что текущий URL содержит переданный путь:'{path}'")
    def check_url_contains(self, path: str, page=None):
        page = self.page if page is None else page
        expect(page).to_have_url(path)
