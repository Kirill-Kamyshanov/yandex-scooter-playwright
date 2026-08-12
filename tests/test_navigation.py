import allure
import pytest

from config.application import Application


@pytest.mark.regression
@allure.feature("Navigation")
class TestNavigation(Application):

    @allure.title("Клик на логотип Яндекса")
    def test_click_on_yandex_logo(self):
        self.home_page.open()
        self.home_page.click_on_yandex_logo()

    @allure.title("Переход на страницу оформления заказа")
    @pytest.mark.smoke
    @pytest.mark.parametrize("button", ["top", "bottom"])
    def test_go_to_create_order_from_home_page(self, button):
        self.home_page.open()
        self.home_page.go_to_create_order(button)
        assert False
