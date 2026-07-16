import pytest
from playwright.sync_api import Page

from pages.create_order_page import CreateOrderPage
from pages.home_page import HomePage


class Application:
    """Инициализация всех страниц сервиса"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.home_page = HomePage(page)
        self.create_order_page = CreateOrderPage(page)
