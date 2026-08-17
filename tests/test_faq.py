import allure
import pytest

from config.application import Application


@pytest.mark.regression
@allure.feature("FAQ")
class TestFaq(Application):
    @allure.title("Клик на часто задаваемые вопросы")
    @pytest.mark.parametrize("index", ["0", "1", "2", "3", "4", "5", "6", "7"])
    def test_faq(self, index, load_test_data):
        expected_text = load_test_data["FAQ texts"][index]

        self.home_page.open()
        self.home_page.faq_component.click_faq_question_button(index)
        self.home_page.faq_component.check_faq_question_text(index, expected_text)
