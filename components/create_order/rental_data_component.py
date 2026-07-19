from datetime import date

import allure
import dateparser
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RentalDataComponent(BaseComponent):
    """Экран 'Про аренду'"""

    PAGE_PATH = "/order"

    def __init__(self, page: Page):
        super().__init__(page)

        self.rental_data_title = self.page.locator('//div[text()="Про аренду"]')
        self.select_date_input = self.page.get_by_placeholder('* Когда привезти самокат')
        self.next_month_button = self.page.locator('//*[text()="Next Month"]')
        self.current_month_area = self.page.locator('//div[contains(@class, "current-month")]')

        self.rental_time_input = self.page.locator('//div[text()="* Срок аренды"]')
        self.rental_time_selected_field = self.page.locator('[class="Dropdown-placeholder is-selected"]')

        self.scooter_color_text = self.page.locator('//*[text()="Цвет самоката"]')
        self.black_color_checkbox = self.page.get_by_role("checkbox", name="чёрный жемчуг")
        self.gray_color_checkbox = self.page.get_by_role("checkbox", name="серая безысходность")

        self.comment_for_courier_input = self.page.get_by_placeholder('Комментарий для курьера')
        self.create_order_button = self.page.locator('//*[text()="Заказать"]').last

    @allure.step("Заполнение формы с данными об аренде")
    def fill_rental_data_form(self, year: str, month: str, day_num: int, rental_duration: str,
                              color: str = None, comment: str = None):

        # Выбор даты доставки самоката
        self.select_date_input.click()

        #  Валидация на дату в прошлом
        selected_date = dateparser.parse(f"{year} {month} {day_num}", languages=['ru']).date()
        assert selected_date >= date.today(), f"Выбрана дата в прошлом: {selected_date}, текущая дата: {date.today()}"

        while not (self.current_month_area.inner_text().startswith(
                month) and self.current_month_area.inner_text().endswith(year)):
            self.next_month_button.click()
        self.page.locator(
            f'//div[contains(@aria-label, "{month[:-1]}") and text()="{day_num}"]').click()  # день доставки

        # Выбор срока аренды
        self.rental_time_input.click()
        self.page.locator(f'//*[text()="{rental_duration}"]').click()

        # Выбор цвета
        if color is not None:
            color = self.black_color_checkbox if color.lower() == "black" else self.gray_color_checkbox
            color.check()
        # Заполнение формы с комментарием для курьера
        if comment is not None:
            self.comment_for_courier_input.fill(comment)

    @allure.step("Проверка корректности отображения формы и заполнения её данными об аренде")
    def check_rental_data_form_is_filled(self, year: str, month: str, day_num: int, rental_duration: str,
                                         color: str = None, comment: str = None):

        expect(self.rental_data_title).to_be_visible()

        month_num = dateparser.parse(f"{year} + {month} + {day_num}", languages=['ru']).date().month
        expect(self.select_date_input).to_have_value(f"{day_num:02d}.{month_num:02d}.{year}")
        expect(self.rental_time_selected_field).to_have_text(rental_duration)

        expect(self.scooter_color_text).to_be_visible()
        if color is not None:
            color = self.black_color_checkbox if color.lower() == "black" else self.gray_color_checkbox
            expect(color).to_be_checked()

        if comment is not None:
            expect(self.comment_for_courier_input).to_have_value(comment)

        expect(self.create_order_button).to_be_enabled()

    @allure.step("Нажатие на кнопку создания заказа")
    def click_create_order_button(self):
        self.create_order_button.click()
