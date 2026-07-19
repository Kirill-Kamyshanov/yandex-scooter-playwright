import allure
import pytest

from config.application import Application
from utils.dates import date_for_test


@pytest.mark.regression
@allure.feature("Orders")
class TestOrder(Application):

    @allure.title("Оформление заказа")
    @pytest.mark.smoke
    @pytest.mark.parametrize("create_button, user_number, rental_duration, color", [
        # ("top", "1", "трое суток", "black"),
        ("bottom", "2", "четверо суток", "gray"),
    ])
    def test_create_order(self, load_test_data, create_button, user_number, rental_duration, color, browser_name):
        if browser_name == "chromium":
            pytest.skip("Не работает кнопка подтверждения создания заказа в chromium")
        day_in_week, month_in_week, year_in_week = date_for_test(days=7)
        user_data = load_test_data["test users"][user_number]
        test_comment = "let`s go"

        self.home_page.open()
        self.home_page.go_to_create_order(create_button)
        self.create_order_page.buyer_data_component.fill_buyer_data_form(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            address=user_data["address"],
            phone_number=user_data["phone_number"],
            metro_station=user_data["metro_station"]
        )
        self.create_order_page.buyer_data_component.check_buyer_data_form_is_filled(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            address=user_data["address"],
            phone_number=user_data["phone_number"],
            metro_station=user_data["metro_station"]
        )
        self.create_order_page.buyer_data_component.go_to_rental_data_form()
        self.create_order_page.rental_data_component.fill_rental_data_form(
            year=year_in_week,
            month=month_in_week,
            day_num=day_in_week,
            rental_duration=rental_duration,
            color=color,
            comment=test_comment
        )

        self.create_order_page.rental_data_component.check_rental_data_form_is_filled(
            year=year_in_week,
            month=month_in_week,
            day_num=day_in_week,
            rental_duration=rental_duration,
            color=color,
            comment=test_comment
        )
        self.create_order_page.rental_data_component.click_create_order_button()
        self.create_order_page.order_confirmation_modal_component.click_confirm_creation_order_button()
        self.create_order_page.order_created_successfully_modal_component.check_order_created()
