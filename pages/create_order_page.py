import allure
from playwright.sync_api import Page

from components.create_order.buyer_data_component import BuyerDataComponent
from components.create_order.order_confirmation_modal_component import OrderConfirmationModalComponent
from components.create_order.order_created_successfully_modal_component import OrderCreatedSuccessfullyModalComponent
from components.create_order.rental_data_component import RentalDataComponent
from pages.base_page import BasePage


class CreateOrderPage(BasePage):
    PAGE_PATH = "/order"

    def __init__(self, page: Page):
        super().__init__(page)

        self.buyer_data_component = BuyerDataComponent(self.page)
        self.rental_data_component = RentalDataComponent(self.page)
        self.order_confirmation_modal_component = OrderConfirmationModalComponent(self.page)
        self.order_created_successfully_modal_component = OrderCreatedSuccessfullyModalComponent(self.page)

    @allure.step("Переход на страницу создания заказа")
    def open(self):
        super().open(self.PAGE_PATH)
        self.check_url_contains(self.PAGE_PATH)
