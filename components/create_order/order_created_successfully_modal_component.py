import allure
from playwright.sync_api import expect

from components.base_component import BaseComponent


class OrderCreatedSuccessfullyModalComponent(BaseComponent):
    """Модальное окно с информацией об успешно созданном заказе"""

    def __init__(self, page):
        super().__init__(page)

        self.order_created_successfully_title = self.page.locator('//div[text()="Заказ оформлен"]')
        self.new_order_data = self.page.locator('//div[contains(text(), "Номер заказа: ")]')
        self.view_order_info_button = self.page.locator('//button[text()="Посмотреть статус"]')

    @allure.step("Проверка отображения модального окна успешно созданного заказа")
    def check_order_created(self):
        expect(self.order_created_successfully_title).to_be_visible()
        expect(self.new_order_data).to_be_visible()
        expect(self.view_order_info_button).to_be_enabled()
