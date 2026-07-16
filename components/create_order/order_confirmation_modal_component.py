import allure
from playwright.sync_api import expect

from components.base_component import BaseComponent


class OrderConfirmationModalComponent(BaseComponent):
    """Модальное окно с подтверждением создания заказа"""

    def __init__(self, page):
        super().__init__(page)
        self.accept_order_creation_title = self.page.locator('//div[text()="Хотите оформить заказ?"]')
        self.accept_order_creation_button = self.page.locator('//button[text()="Да"]')
        self.cancel_order_creation_button = self.page.locator('//button[text()="Нет"]')

    @allure.step("Нажатие на кнопку подтверждения создания заказа")
    def click_confirm_creation_order_button(self):
        expect(self.accept_order_creation_title).to_be_visible()
        expect(self.accept_order_creation_button).to_be_enabled()
        expect(self.cancel_order_creation_button).to_be_enabled()
        self.accept_order_creation_button.click()
