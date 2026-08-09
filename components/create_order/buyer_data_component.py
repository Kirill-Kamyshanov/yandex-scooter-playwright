import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class BuyerDataComponent(BaseComponent):
    """Экран 'Для кого самокат'"""

    PAGE_PATH = "/order"

    def __init__(self, page: Page):
        super().__init__(page)

        self.buyer_data_title = self.page.locator('//div[text()="Для кого самокат"]')
        self.buyer_first_name_field = self.page.get_by_placeholder('* Имя')
        self.buyer_last_name_field = self.page.get_by_placeholder('* Фамилия')
        self.buyer_address_field = self.page.get_by_placeholder('* Адрес: куда привезти заказ')
        self.buyer_metro_station_field = self.page.get_by_placeholder('* Станция метро')
        self.buyer_phone_field = self.page.get_by_placeholder('* Телефон: на него позвонит курьер')
        self.next_button = self.page.get_by_role("button", name="Далее")

    @allure.step("Заполнение формы с данными покупателя")
    def fill_buyer_data_form(self, first_name: str, last_name: str, address: str, metro_station: str,
                             phone_number: str):
        self.buyer_first_name_field.fill(first_name)
        self.buyer_last_name_field.fill(last_name)
        self.buyer_address_field.fill(address)
        self.buyer_phone_field.fill(phone_number)

        # Выбор станции метро
        self.buyer_metro_station_field.click()
        self.page.keyboard.type(metro_station, delay=50)
        self.page.get_by_text(metro_station, exact=True).click()

    @allure.step("Проверка корректности заполнения формы с данными покупателя")
    def check_buyer_data_form_is_filled(self, first_name: str, last_name: str, address: str, metro_station: str,
                                        phone_number: str):
        expect(self.buyer_data_title).to_be_visible()
        expect(self.buyer_first_name_field).to_have_value(first_name)
        expect(self.buyer_last_name_field).to_have_value(last_name)
        expect(self.buyer_address_field).to_have_value(address)
        expect(self.buyer_phone_field).to_have_value(phone_number)
        expect(self.buyer_metro_station_field).to_have_value(metro_station)

    @allure.step("Переход к форме с данными об аренде. Нажатие но кнопку 'Далее'")
    def go_to_rental_data_form(self):
        expect(self.next_button).to_be_enabled()
        self.next_button.click()
        self.check_url_contains(self.PAGE_PATH)
