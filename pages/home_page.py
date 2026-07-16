import allure
from playwright.sync_api import Page

from components.home_page.faq_component import FaqComponent
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.faq_component = FaqComponent(self.page)

        self.yandex_logo = self.page.locator('[alt="Yandex"]')
        self.make_order_button_top = self.page.get_by_role("button", name="Заказать").nth(0)
        self.make_order_button_bottom = self.page.get_by_role("button", name="Заказать").nth(1)

    @allure.step("клик на указанную кнопку 'создать заказ': '{place}'")
    def go_to_create_order(self, place: str = "top"):
        button = self.make_order_button_top if place.lower() == "top" else self.make_order_button_bottom
        button.click()
        self.check_url_contains("https://qa-scooter.praktikum-services.ru/order")

    @allure.step("Клик на логотип Яндекса на домашней странице")
    def click_on_yandex_logo(self):
        with self.page.context.expect_page() as tab:
            self.yandex_logo.click()
        new_tab = tab.value
        new_tab.wait_for_load_state()
        self.check_url_contains("https://dzen.ru/?yredirect=true", page=new_tab)
